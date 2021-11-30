#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from script import Script


@trojanz.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    await message.reply_text(
        text=Script.START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_data"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "⭕️ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ⭕️", url="https://t.me/Z_Bots")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start_data"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "⭕️ sᴜᴘᴘᴏʀᴛ ⭕️", url="https://t.me/z_bots_support7")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    await message.reply_text(
        text=Script.ABOUT_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help_data"),
                    InlineKeyboardButton("sᴛᴀʀᴛ", callback_data="start_data"),
                ],
                [
                    InlineKeyboardButton(
                        "sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴏᴜʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ", url="https://youtube.com/channel/UCBNR3HdxF8qQUqsMtfyxojQ")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )
