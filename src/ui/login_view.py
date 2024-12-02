from tkinter import ttk, StringVar, constants
from services.studytracker_service import studytracker_service


class LoginView:

    def __init__(self, root, handle_login, handle_show_create_user_view, success=None):

        self.root = root
        self.handle_login = handle_login
        self.handle_show_create_user_view = handle_show_create_user_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None
        self.success = success
        self.success_variable = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def login_handler(self):
        self.hide_success()
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            studytracker_service.login(username, password)
            self.handle_login()
        except ValueError as e:
            self.show_error(e)

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def show_success(self):
        self.success_variable.set("Käyttäjätunnus luotu")
        self.success_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def hide_success(self):
        self.success_label.grid_remove()
        self.success = None

    def initialize_username_field(self):
        username_label = ttk.Label(master=self.frame, text="Käyttäjätunnus")

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(columnspan=2, padx=5, pady=5, sticky=constants.W)
        self.username_entry.grid(columnspan=2, padx=5, pady=5, sticky=constants.EW)

    def initialize_password_field(self):
        password_label = ttk.Label(master=self.frame, text="Salasana")

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(columnspan=2, padx=5, pady=5, sticky=constants.W)
        self.password_entry.grid(columnspan=2, padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground="red"
        )

        self.error_label.grid(padx=5, pady=5, sticky=constants.W)

        self.success_variable = StringVar(self.frame)

        self.success_label = ttk.Label(
        master=self.frame,
        textvariable=self.success_variable,
        foreground="green"
        )

        self.success_label.grid(padx=5, pady=5, sticky=constants.W)

        self.initialize_username_field()
        self.initialize_password_field()

        login_button = ttk.Button(
            master=self.frame,
            text="Kirjaudu sisään",
            command=self.login_handler
        )

        create_user_button = ttk.Button(
            master=self.frame,
            text="Siirry luomaan käyttäjätili",
            command=self.handle_show_create_user_view
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=200)
        self.frame.grid_columnconfigure(1, weight=1, minsize=200)

        login_button.grid(row=6, column=0, padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(row=6, column=1, padx=5, pady=5, sticky=constants.EW)

        self.hide_error()
        if self.success:
            self.show_success()
        else:
            self.hide_success()
