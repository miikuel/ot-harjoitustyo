from ui.login_view import LoginView
from ui.tasks_view import TasksView
from ui.create_user_view import CreateUserView

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self.show_login_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_login_view(self, success=None):
        self.hide_current_view()

        self.current_view = LoginView(
            self.root,
            self.show_tasks_view,
            self.show_create_user_view,
            success
        )

        self.current_view.pack()

    def show_tasks_view(self):
        self.hide_current_view()

        self.current_view = TasksView(self.root, self.show_login_view)

        self.current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()

        self.current_view = CreateUserView(
            self.root,
            self.show_login_view
        )

        self.current_view.pack()