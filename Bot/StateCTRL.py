from abc import ABC, abstractmethod


class StateCTRL(ABC):

    def __init__(self, target: str):
        self.target = target

    def __str__(self):
        return f"{self.__class__.__name__}(target={self.target})"

    @abstractmethod
    def check_state(self, state: str) -> bool:
        pass


class IdState(StateCTRL):
    def check_state(self, state: str) -> bool:
        return state in self.target


class AnyState(StateCTRL):
    def __init__(self):
        super().__init__(None)

    def check_state(self, state: str) -> bool:
        True
