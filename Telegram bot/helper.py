from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import re
'''
# Initialize the client with your API credentials
app = Client(
    "my_bot",
    api_id=19778892,
    api_hash="4dd7e1b7d22ec89dd9e9058fcd35af8b",
    bot_token="7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8"
)

# In-memory storage for user states
user_states = {}

# Command handler to send a message with an inline keyboard button
@app.on_message(filters.command("start"))
async def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Enter Text", callback_data="enter_text")]
    ])
    await message.reply("Press the button to enter some text:", reply_markup=keyboard)

# Function to create a dynamic data filter for callback queries
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

# Specific text handler for the input "go"
@app.on_message(filters.text & filters.private & filters.create(lambda _, __, message: message.text.lower() == "go"))
async def handle_go(client, message):
    await message.reply("You entered 'go'!", reply_markup=ReplyKeyboardRemove())
    # Clear the saved user ID if needed
    user_states.pop(message.from_user.id, None)

# General text handler for any other text input
@app.on_message(filters.text & filters.private)
async def capture_text(client, message):
    user_id = message.from_user.id
    if user_id in user_states:
        user_input = message.text
        await message.reply(f"You entered: {user_input}", reply_markup=ReplyKeyboardRemove())
        # Clear the saved user ID
        del user_states[user_id]

# Start the bot
app.run()'''

def card_pattern(message):
    num = re.findall(r"^[a-zA-Z0-9]{6}_card$",message)
    print(num)

card_pattern("UCSC21_card")