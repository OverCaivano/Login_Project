from models.user_model import UserModel
from views.login_view import LoginView
from controllers.login_controller import LoginController
from strategies.auth_strategy import PasswordAuth, TokenAuth

if __name__ == "__main__":
    model = UserModel()
    view = LoginView()

    # Podemos elegir estrategia
    strategy = PasswordAuth()  # o TokenAuth()

    controller = LoginController(model, view, strategy)
    controller.login()
