from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext


def resolve_text_parameters(text: str, update: Update):
    return text\
        .replace("@datetime@", str(update.message.date))\
        .replace("@client_f_name@", update.message.from_user.first_name)


class Response(ABC):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return f"{self.__class__.__name__}(response={self.response})"

    @abstractmethod
    def do_response(self, update: Update, context: CallbackContext) -> bool:
        pass


class TextResponse(Response):
    async def do_response(self, update: Update, context: CallbackContext) -> bool:
        await update.message.reply_text(resolve_text_parameters(self.response, update))


responses = {"text": TextResponse}
