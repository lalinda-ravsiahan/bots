import asyncio
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton

# Initialize the client with your API credentials
app = Client(
    "my_bot",
    api_id=19778892,
    api_hash="4dd7e1b7d22ec89dd9e9058fcd35af8b",
    bot_token="7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8"
)

# Dictionary to store user states
user_states = {}

@app.on_message(filters.text)
async def handle_text(client, message):
    user_id = message.from_user.id

    # Check if user has a state
    if user_id not in user_states:
        user_states[user_id] = None

    # Handle different states
    if user_states[user_id] == "awaiting_first_choice":
        if message.text == "Register As A New User":
            await message.reply("You selected Option 1", reply_markup=ReplyKeyboardRemove())
            
           

            
        elif message.text == "Logging As A Existing User":
            await message.reply("You selected Option 2", reply_markup=ReplyKeyboardRemove())
            
            keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Enter Your Reference Number", callback_data="enter_text")]
            ])

            await message.reply("Press the button to enter some text:", reply_markup=keyboard)
            
        else:
            await message.reply("Please provide a valid answer")
    
    
    else:
        # Handle initial commands
        await message.reply(
            "Welcome! Choose an option from the keyboard below.",
            reply_markup=ReplyKeyboardMarkup(
                [["Register As A New User", "Logging As A Existing User"]],
                resize_keyboard=True
            )
        )
        user_states[user_id] = "awaiting_first_choice"

def dynamic_data_filter(data):
    async def func(flt, _, query):
        return flt.data == query.data
    return filters.create(func, data=data)

# Callback query handler to prompt user for text input
@app.on_callback_query(dynamic_data_filter("enter_text"))
async def prompt_text_input(client, query):
    await query.message.reply("Please enter your text:")
    # Save the user ID and chat ID to use in the message handler
    user_states[query.from_user.id] = query.message.chat.id

# Message handler to capture and respond to the user's input
@app.on_message(filters.text & filters.private)
async def capture_text(client, message):
    user_id = message.from_user.id
    if user_id in user_states:
        user_input = message.text
        await message.reply(f"You entered: {user_input}", reply_markup=ReplyKeyboardRemove())
        # Clear the saved user ID
        del user_states[user_id]

# Main function to start the bot
async def main():
    async with app:
        await app.send_message(
            "l_w_ravishan",
            "Bot started"
        )
        await asyncio.Event().wait()  # Keeps the bot running

if __name__ == "__main__":
    app.run(main())
