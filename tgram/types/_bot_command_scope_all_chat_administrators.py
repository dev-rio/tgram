import tgram
from .type_ import Type_

from typing import Optional


class BotCommandScopeAllChatAdministrators(Type_):
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    Telegram Documentation: https://core.telegram.org/bots/api#botcommandscopeallchatadministrators

    :param type: Scope type, must be all_chat_administrators
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`tgram.types.BotCommandScopeAllChatAdministrators`
    """

    def __init__(
        self, type: "str" = None, me: "tgram.TgBot" = None, json: "dict" = None
    ):
        super().__init__(me=me, json=json)
        self.type = type

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.BotCommandScopeAllChatAdministrators"]:
        return (
            BotCommandScopeAllChatAdministrators(me=me, json=d, type=d.get("type"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
