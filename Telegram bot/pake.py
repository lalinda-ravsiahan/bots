import asyncio
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove

# Initialize the client with your API credentials
app = Client(
    "my_bot",
    api_id=19778892,
    api_hash="4dd7e1b7d22ec89dd9e9058fcd35af8b",
    bot_token="7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8"
)

# Handle the /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    await message.reply("Welcome! This bot can automate your birthday wishes.")
    await buttons(client, message)


# Function to send a message with buttons
async def buttons(client, message):
    await client.send_message(
        message.chat.id,  # Send to the chat where the /start command was received
        "Select Something Below",
        reply_markup=ReplyKeyboardMarkup(
            [               
                ["Register As A New User", "Logging As A Existing User"]  # Second row               
            ],
            resize_keyboard=True  # Make the keyboard smaller
        )
    )


@app.on_message(filters.text)
async def handle_text(client, message):

    #if user choose Register As A New User Option
    if message.text == "Register As A New User":

        await message.reply("You selected Option 1", reply_markup=ReplyKeyboardRemove())
        await app.send_message(
            f"{message.chat.id}",  # Edit this
            "This is a InlineKeyboardMarkup example",
            reply_markup=InlineKeyboardMarkup(
                [
                    [  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            "Button",
                            callback_data="data"
                        ),
                        InlineKeyboardButton(  # Opens a web URL
                            "URL",
                            url="https://docs.pyrogram.org"
                        ),
                    ]   
                ]
            )
        )

    # if user choose Logging As a Existing User
    elif message.text == "Logging As A Existing User":
        await message.reply("You selected Option 2",reply_markup=ReplyKeyboardRemove())
        await client.send_message(
            message.chat.id,  # Send to the chat where the /start command was received
            "Select",
            reply_markup=ReplyKeyboardMarkup(
                [               
                    ["Check Google Form Status", "Check Birthdays Today Manually"]  # Second row               
                ],
                resize_keyboard=True  # Make the keyboard smaller
        )    )

    else:
        await message.reply("please provide a valid answer")

# Main function to start the bot
async def main():
    async with app:
        await asyncio.Event().wait()  # Keeps the bot running

if __name__ == "__main__":
    app.run(main())
