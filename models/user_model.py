class UserModel:
    def __init__(self):
        # simulamos base de datos
        self.users = {
            "juan": {"password": "1234", "token": "abcd"},
            "maria": {"password": "5678", "token": "efgh"},
        }

    def get_user(self, username):
        return self.users.get(username)
