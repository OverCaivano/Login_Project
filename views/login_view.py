class LoginView:
    def get_credentials(self):
        username = input("Usuario: ")
        password = input("Contraseña: ")
        return username, password

    def show_result(self, success):
        if success:
            print("✅ Login exitoso")
        else:
            print("❌ Login fallido")
