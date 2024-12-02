from tkinter import ttk, StringVar, constants
from services.studytracker_service import studytracker_service #, UsernameExistsError


class CreateUserView:

    def __init__(self, root, handle_show_login_view):

        self.root = root
        self.handle_show_login_view = handle_show_login_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def create_user_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            studytracker_service.create_user(username, password)
            self.handle_show_login_view(success=True)
        except ValueError as e:
            self.show_error(e)

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize_username_field(self):
        username_label = ttk.Label(master=self.frame, text="Käyttäjätunnus")

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def initialize_password_field(self):
        password_label = ttk.Label(master=self.frame, text="Salasana")

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground="red"
        )

        self.error_label.grid(padx=5, pady=5, sticky=constants.W)

        self.initialize_username_field()
        self.initialize_password_field()

        create_user_button = ttk.Button(
            master=self.frame,
            text="Luo käyttäjätunnus",
            command=self.create_user_handler
        )

        login_button = ttk.Button(
            master=self.frame,
            text="Takaisin",
            command=self.handle_show_login_view
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.hide_error()