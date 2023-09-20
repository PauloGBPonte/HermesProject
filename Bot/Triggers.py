from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import MessageHandler, BaseHandler, filters


class Trigger(ABC):

    def __init__(self, target):
        self.target = target

    def __str__(self):
        return f"{self.__class__.__name__}(target={self.target})"

    @abstractmethod
    def check_condition(self, update: Update) -> bool:
        pass

    @abstractmethod
    def build_handler(self) -> BaseHandler:
        pass


class LiteralTrigger(Trigger):
    def check_condition(self, update: Update) -> bool:
        return self.target == update.message.text

    def build_handler(self, cb) -> BaseHandler:
        return MessageHandler(filters=filters.TEXT, callback=cb)


triggers = {"literal": LiteralTrigger}
