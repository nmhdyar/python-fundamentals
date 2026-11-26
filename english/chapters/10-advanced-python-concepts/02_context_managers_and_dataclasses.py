from contextlib import contextmanager
from dataclasses import dataclass


@dataclass
class User:
    username: str
    active: bool = True


@contextmanager
def temporary_flag(settings: dict[str, bool], key: str):
    previous = settings.get(key, False)
    settings[key] = True
    try:
        yield
    finally:
        settings[key] = previous


settings = {"maintenance": False}
with temporary_flag(settings, "maintenance"):
    print(settings["maintenance"])
print(User("nima"))
