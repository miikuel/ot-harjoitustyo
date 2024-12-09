from tkinter import ttk, constants, font, StringVar
from services.studytracker_service import studytracker_service


class TaskListView:

    def __init__(self, root, tasks, handle_set_task_done, handle_set_task_not_done):

        self.root = root
        self.tasks = tasks
        self.handle_set_task_done = handle_set_task_done
        self.handle_set_task_not_done = handle_set_task_not_done
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize_task_item(self, task):
        item_frame = ttk.Frame(master=self.frame)
        topic = ttk.Label(master=item_frame, text=task.topic)
        category = ttk.Label(master=item_frame, text=task.category)
        deadline = ttk.Label(master=item_frame, text=task.deadline)

        if not task.done:
            style = ttk.Style()
            style.configure(
                "set_done.TButton",
                font=("Helvetica", 11, "bold"),
                foreground="white",
                background="green"
            )
            style.map(
                "set_done.TButton",
                background=[("active", "white")],
                foreground=[("active", "green")]
            )
            set_done_button = ttk.Button(
                master=item_frame,
                text="Merkkaa tehdyksi",
                style="set_done.TButton",
                command=lambda: self.handle_set_task_done(task.task_id)
            )
            set_done_button.grid(
                row=0,
                column=3,
                padx=5,
                pady=5,
                sticky=constants.EW
            )
        else:
                style = ttk.Style()
                style.configure(
                    "set_not_done.TButton",
                    font=("Helvetica", 11, "bold"),
                    foreground="white",
                    background="red"
                )
                style.map(
                    "set_not_done.TButton",
                    background=[("active", "white")],
                    foreground=[("active", "red")]
                )

                set_not_done_button = ttk.Button(
                master=item_frame,
                text="Palauta tekemättömäksi",
                style="set_not_done.TButton",
                command=lambda: self.handle_set_task_not_done(task.task_id)
                )
                set_not_done_button.grid(
                    row=0,
                    column=3,
                    padx=5,
                    pady=5,
                    sticky=constants.EW
                )

        topic.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)
        category.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)
        deadline.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1, minsize=300)
        item_frame.grid_columnconfigure(1, weight=1, minsize=200)
        item_frame.grid_columnconfigure(2, weight=1, minsize=200)
        item_frame.grid_columnconfigure(3, weight=1, minsize=200)
        item_frame.pack(fill=constants.X)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        for task in self.tasks:
            # if not task.done:
            self.initialize_task_item(task)


class TasksView:

    def __init__(self, root, handle_logout):
        self.root = root
        self.handle_logout = handle_logout
        self.user = studytracker_service.get_logged_user()
        self.frame = None
        self.create_task_entry = None
        self.task_list_frame = None
        self.task_list_view = None
        self.error_variable = None
        self.error_label = None
        self.task_filter = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def logout_handler(self):
        studytracker_service.logout()
        self.handle_logout()

    def handle_set_task_done(self, task_id):
        studytracker_service.set_task_done(task_id)
        self.initialize_task_list()
        self.hide_error()

    def handle_set_task_not_done(self, task_id):
        studytracker_service.set_task_not_done(task_id)
        self.initialize_task_list()
        self.hide_error()

    def initialize_task_list(self):
        if self.task_list_view:
            self.task_list_view.destroy()

        if self.task_filter.get() == "Tekemättömät":
            tasks = studytracker_service.find_users_tasks()
            tasks = list(filter(lambda task: task.done == 0, tasks))
        elif self.task_filter.get() == "Tehdyt":
            tasks = studytracker_service.find_users_tasks()
            tasks = list(filter(lambda task: task.done, tasks))
        else:
            tasks = studytracker_service.find_users_tasks()

        self.task_list_view = TaskListView(
            self.task_list_frame,
            tasks,
            self.handle_set_task_done,
            self.handle_set_task_not_done
        )

        self.task_list_view.pack()

    def initialize_header(self):
        bold_font = font.Font(family="Helvetica", size=12, weight="bold")
        user_label = ttk.Label(
            master=self.frame,
            text=f"Kirjautunut sisään käyttäjätunnuksella {self.user.username}",
            foreground="blue"
        )

        logout_button = ttk.Button(
            master=self.frame,
            text="Kirjaudu ulos",
            command=self.logout_handler
        )

        topic_label = ttk.Label(
        master=self.frame,
        text="Aihe",
        font=bold_font
        )

        category_label = ttk.Label(
        master=self.frame,
        text="Kategoria",
        font=bold_font
        )

        deadline_label = ttk.Label(
        master=self.frame,
        text="Deadline",
        font=bold_font
        )

        self.task_filter = StringVar()
        choices = ["Tekemättömät", "Tehdyt", "Kaikki"]
        self.task_filter.set(choices[0])
        self.task_filter.trace_add("write", lambda *args: self.initialize_task_list())
        style = ttk.Style()
        style.configure(
            "task_filter.TMenubutton",
            font=("Helvetica", 11, "bold"),
            foreground="black",
            background="darkgrey"
        )
        style.map(
            "task_filter.TMenubutton",
            background=[("active", "white")],
            foreground=[("active", "black")]
        )

        separator = ttk.Separator(master=self.frame, orient="horizontal")
        separator.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky=constants.EW)
        separator_2 = ttk.Separator(master=self.frame, orient="horizontal")
        separator_2.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=constants.EW)

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)
        topic_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.E)
        category_label.grid(row=2, column=1, padx=5, pady=5, sticky=constants.E)
        deadline_label.grid(row=2, column=2, padx=5, pady=5, sticky=constants.E)
        dropdown = ttk.OptionMenu(self.frame, self.task_filter, self.task_filter.get(), *choices, style="task_filter.TMenubutton")
        dropdown.grid(row=2, column=3, padx=5, pady=5, sticky=constants.E)
    

        logout_button.grid(
            row=0,
            column=3,
            padx=5,
            pady=5,
            sticky=constants.EW
        )



    def handle_create_task(self):
        topic = self.create_task_topic_entry.get()
        category = self.create_task_category_entry.get()
        deadline = self.create_task_deadline_entry.get()

        try:
            studytracker_service.create_task(topic, category, deadline)
            self.initialize_task_list()
            self.create_task_topic_entry.delete(0, constants.END)
            self.create_task_category_entry.delete(0, constants.END)
            self.create_task_deadline_entry.delete(0, constants.END)
            self.hide_error()
        except ValueError as e:
            self.show_error(e)


    def initialize_footer(self):
        self.create_task_topic_entry = ttk.Entry(master=self.frame)
        self.create_task_category_entry = ttk.Entry(master=self.frame)
        self.create_task_deadline_entry = ttk.Entry(master=self.frame)

        separator = ttk.Separator(master=self.frame, orient="horizontal")
        separator.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky=constants.EW)


        create_task_button = ttk.Button(
            master=self.frame,
            text="Lisää",
            command=self.handle_create_task
        )

        self.create_task_topic_entry.grid(
            row=6,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        self.create_task_category_entry.grid(
            row=6,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        self.create_task_deadline_entry.grid(
            row=6,
            column=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )     

        create_task_button.grid(
            row=6,
            column=3,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def hide_error(self):
        self.error_label.grid_remove()

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground="red"
        )

        self.error_label.grid(row=7, padx=5, pady=5, sticky=constants.W)

        self.task_list_frame = ttk.Frame(master=self.frame)

        self.initialize_header()
        self.initialize_task_list()
        self.initialize_footer()

        self.task_list_frame.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky=constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)
        self.frame.grid_columnconfigure(1, weight=1, minsize=200)
        self.frame.grid_columnconfigure(2, weight=1, minsize=200)
        self.frame.grid_columnconfigure(3, weight=1, minsize=200)
        self.hide_error()