import time
from enum import Enum
from typing import Type

from Components.BinaryInput import BinaryInput
from Components.Component import Component
from Components.Toggle import Toggle
from Tasks.Task import Task


class Performance(Task):
    class States(Enum):
        START = 0

    @staticmethod
    def get_components() -> dict[str, list[Type[Component]]]:
        return {
            "output": [Toggle],
            "input": [BinaryInput],
            "test": [BinaryInput]
        }

    def main_loop(self) -> None:
        active = self.input.check()
        self.test.check()
        if active == BinaryInput.ENTERED:
            self.output.toggle(True)
        elif active == BinaryInput.EXIT:
            self.output.toggle(False)

    def init_state(self) -> Enum:
        return self.States.START

    def is_complete(self) -> bool:
        return self.time_elapsed() > 100
