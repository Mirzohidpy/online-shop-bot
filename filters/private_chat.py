from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import BoundFilter

class IsPrivate(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE