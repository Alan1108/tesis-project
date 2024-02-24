from typing import Any
import os


class VariablesMeta(type):

    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Variables(metaclass=VariablesMeta):

    def __init__(self) -> None:
        self.ROBO_API_KEY = os.environ.get("ROBO_API_KEY") or ""
        self.ROBO_WORKSPACE = os.environ.get("ROBO_WORKSPACE") or ""
        self.ROBO_PROJECT_NAME = os.environ.get("ROBO_PROJECT_NAME") or ""
