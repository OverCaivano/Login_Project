class LoginController:
    def __init__(self, model, view, strategy):
        self.model = model
        self.view = view
        self.strategy = strategy

    def login(self):
        username, password = self.view.get_credentials()
        data = self.model.get_user(username)

        if not data:
            self.view.show_result(False)
            return

        success = self.strategy.authenticate(
            type("User", (), data),
            password
        )
        self.view.show_result(success)
