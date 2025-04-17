import asyncio
from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)

api_id = 19778892
api_hash = "4dd7e1b7d22ec89dd9e9058fcd35af8b"
bot_token = "7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8"

app = Client("lalinda",
             api_hash=api_hash,
             api_id=api_id,
             bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    await message.reply("Welcome! You've started the bot.")
    await app.send_message(
            f"{user_id}",  # Edit this
            "enter",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["Register As A New User", "Logging As A Existing User"],  # First row
                    
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )
    
app.run()