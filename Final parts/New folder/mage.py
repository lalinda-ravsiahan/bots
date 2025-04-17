from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,ReplyKeyboardMarkup
from register_new_birthday_card import *


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
    user_id = message.from_user.id
    await message.reply("Welcome! You've started the bot.")
    await app.send_message(
            f"{user_id}",  # Edit this
            "enter",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["/Register_As_A_NewUser", "/Logging_As_A_ExistingUser"],  # First row
                    
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )

#Filtering Command line path for "Register as a new user"
@app.on_message(filters.command("Register_As_A_NewUser"))
async def echo_command(client, message):
    await message.reply(f"""Welcome To abw_system New User Registering Wizard 
                            You Need To Follow The Below Steps To Register As A new User 
                        """,reply_markup=ReplyKeyboardRemove())
    await kok(client,message,app)   #importing new birthday card system 


#Filtering Command line path for "Logging as a existing user"
@app.on_message(filters.command("Logging_As_A_ExistingUser"))
async def echo_command(client, message):
    await message.reply(f"I've got this {message.text}")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Click Here To Enter Your Reference Number", callback_data="reference")]
        ])
    await message.reply("Welcome! Press the button to enter reference number:", reply_markup=keyboard)

# Function to create a dynamic data filter for callback queries
def dynamic_data_filter(data):
    async def func(flt, _, query):
        return flt.data == query.data
    return filters.create(func, data=data)

# Callback query handler to entering refernce number
@app.on_callback_query(dynamic_data_filter("reference"))
async def prompt_text_input(client, query):
    await query.message.reply("Please enter your reference number now:")
    # Save the user ID and chat ID to use in the message handler
    user_states[query.from_user.id] = query.message.chat.id
    print(user_states)


# Specific text handler for the input "go"
@app.on_message(filters.text & filters.private & filters.create(lambda _, __, message: message.text.lower() == "go")) #sql bas eke query ekk run karala balanna badu theeda kiyla theena yanna

async def handle_go(client, message):

    # reference number eke pattern ekath balanna oona
    await message.reply("You entered 'go'!", reply_markup=ReplyKeyboardRemove())
    #methendi mn mage database eke balanna oona me reference number ekata adalawa data thiyeda kiyala.
    #nattanm kenlinma exit
    #thibenm
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Check Google Form Status", callback_data="form"),InlineKeyboardButton("Create New Form For This Existing Account", callback_data="new_existing")],
        [InlineKeyboardButton("Check Birthdays Today", callback_data="bithday")]
        ])
    await message.reply("Welcome! Press the button to enter some text:", reply_markup=keyboard)
       
    # Clear the saved user ID if needed
    user_states.pop(message.from_user.id, None)

#Handle google form status inline button
@app.on_callback_query(dynamic_data_filter("form"))
async def prompt_text_input(client, query):
    #chech whether users all google forms got all the expected responses.so we must run a query throu all his birthday cards and check  their forms complete or not
    #then if completed add button to  add that particular card's form data to the database
    #if the cards data added already display your form responses added to the database
    #if some card doesnot complete thier expected responses count disply how many responses corded from expected responses
    ...
    
#handle create a new form for the existing account button
@app.on_callback_query(dynamic_data_filter("new_existing"))
async def prompt_text_input(client, query):
    #create new form for this registered accout number
    ...
    

#handle all the check birthday button and give all the birth that under this user(under all the accounts of that user by telling which form name has which person birthday)
@app.on_callback_query(dynamic_data_filter("birthday"))
async def prompt_text_input(client, query):
    #run a query through this users all birthday cards databases and check whether today he has birthdays or not
    ...
    


# Start the bot
app.run()