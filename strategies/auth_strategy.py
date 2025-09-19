from abc import ABC, abstractmethod

class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, user, password) -> bool:
        pass


class PasswordAuth(AuthStrategy):
    def authenticate(self, user, password) -> bool:
        return user.password == password


class TokenAuth(AuthStrategy):
    def authenticate(self, user, token) -> bool:
        return user.token == token
