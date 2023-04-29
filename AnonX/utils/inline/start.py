from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☃ Aᴅᴅ Mᴇ ɪɴ Yᴏᴜʀ Gʀᴏᴜᴘ ☃",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⁂ Cᴏᴍᴍᴀɴᴅs ⁂", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="♡ Oᴡɴᴇʀ ♡", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="■ sᴜᴘᴘᴏʀᴛ ■",
                url=f"https://t.me/CAREERPOWER",
            ),
            InlineKeyboardButton(
                text="□ ɢʀᴏᴜᴘ □",
                url=f"https://t.me/CAREERPOWER",
            )
        ],
        [
            InlineKeyboardButton(
                text="● ᴄʀᴇᴀᴛᴏʀ ●",
                url=f"https://t.me/ChampuXD",
            )
        ]
     ]
    return buttons