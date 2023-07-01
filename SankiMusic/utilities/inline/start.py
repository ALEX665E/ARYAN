from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="≽ ᴄᴏᴍᴍᴀɴᴅs ≼",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ sᴇᴛᴛɪɴɢs ✮", callback_data="settings_helper"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝗖𝗵𝗮𝗻𝗻𝗲𝗹❱", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="❰𝗚𝗿𝗼𝘂𝗽❱", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", url="https://t.me/DEViL_iZ_BACK"
            )
        ]
     ]
    return buttons
