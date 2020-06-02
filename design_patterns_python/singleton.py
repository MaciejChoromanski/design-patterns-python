# Example of 'Singleton' design pattern (thread-safe version)

from __future__ import annotations

from threading import Lock, Thread
from typing import Optional


class UserMeta(type):
    """Meta class for the Singleton"""

    _instance: Optional[User] = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class User(metaclass=UserMeta):
    """Singleton"""

    def __init__(self, login: str) -> None:
        self.login = login

    def __str__(self) -> str:
        return f'User: {self.login}'


def create_user(login: str) -> None:
    user = User(login)
    print(user)


if __name__ == '__main__':
    process_one = Thread(target=create_user, args=('__SuperJoe__',))
    process_two = Thread(target=create_user, args=('__NotSoSuperJoe__',))

    process_one.start()
    process_two.start()
