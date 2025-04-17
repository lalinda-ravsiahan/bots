from pyrogram import Client,filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
import asyncio

app=Client("my bot",
           api_id=19778892,
           api_hash="4dd7e1b7d22ec89dd9e9058fcd35af8b",
           bot_token="7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8"
           )


# Handle the /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    await message.reply("Welcome! This bot can automate your birthday wishes.")

@app.on_message(filters.command("start"))
async def buttons():
    async with app:
        await app.send_message(
            f"l_w_ravishan",  # Edit this
            "This is a ReplyKeyboardMarkup example",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["A", "B", "C", "D"],  # First row
                    ["E", "F", "G"],  # Second row
                    ["H", "I"],  # Third row
                    ["J"]  # Fourth row
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )

async def main():
    await app.start()
    await buttons()

if __name__ == "__main__":
    app.run(main())