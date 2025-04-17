from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,ReplyKeyboardMarkup
from datetime import datetime, timedelta
from admin_database import *
import re
import asyncio
import schedule
from form_query import*
from user_databse import*

# Initialize the client with your API credentials
app = Client(
    "my_bot",
    api_id=19778892,
    api_hash="4dd7e1b7d22ec89dd9e9058fcd35af8b",
    bot_token="7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8"
)

# In-memory storage for user states
user_states = {}
admin_lst=[]

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
                    ["/Register_As_A_NewUser", "/Check_google_form_status"],  # First row
                    
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
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Click Here To Enter Your Reference Number", callback_data="reference")]
        ])
    await message.reply("Press the button to enter reference number:", reply_markup=keyboard)

#Filtering Command line path for "Logging as a existing user"
@app.on_message(filters.command("Check_google_form_status"))
async def echo_command(client, message):
    await message.reply(f"I've got this {message.text}")

    #run a query to see how many responses we've got for that form
    admin_id = message.from_user.id

    #get the google form link of particular admin
    data = await get_form_drive_link(admin_id)    
    responses=get_form_responses(data)

    num_of_responses=len(responses["responses"])
    required_responses=get_required_responses(admin_id)

    if num_of_responses==required_responses:
        if not search_table(admin_id):
            create_birthday_table(admin_id)
            for data in responses:

                name = data["answers"]["5bd21089"]["textAnswers"]["answers"][0]["value"]
                birthday=data["answers"]["5ccd54f1"]["textAnswers"]["answers"][0]["value"]
                photo_drive_link=data["answers"]["18cc91e4"]["fileUploadAnswers"]["answers"][0]["fileId"]

                insert_birthday_data()
        else:
            message.reply("Your database completed already")

    else:
        await message.reply(f"You Do Not Have Required responses ({num_of_responses}/{required_responses}) available")



# Function to create a dynamic data filter for callback queries
def dynamic_data_filter(data):
    async def func(flt, _, query):
        return flt.data == query.data
    return filters.create(func, data=data)

# Callback query handler to entering refernce number
@app.on_callback_query(dynamic_data_filter("reference"))
async def prompt_text_input(client, query):
    await query.message.reply("Please enter your reference number now: like 456_id")
    # Save the user ID and chat ID to use in the message handler
    user_states[query.from_user.id] = {}
    admin_lst.append(query.message.chat.id)
    print(user_states)

# Specific text handler for the responses count
@app.on_message(filters.text & filters.private & filters.create(lambda _, __, message: message.text.lower() == "2002_id")) 
async def handle_admin_reference(client, message):
    await message.reply("OK You Registered Successfully", reply_markup=ReplyKeyboardRemove())
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Click Here To Enter Required Responses For Your Form", callback_data="responses")]
        ])
    await message.reply("SEE BELOW", reply_markup=keyboard)    

# Callback query handler to entering number of responses that need to the google form
@app.on_callback_query(dynamic_data_filter("responses"))
async def prompt_text_input(client, query):
    await query.message.reply("Please enter your Requires Responses Now:(eg:-256_res)")
    

async def res_regex(_,__,text):
    num=re.findall(r"^/d+_res$",text)
    if num:
        return True
    return False

@app.on_message(filters.text & filters.private & filters.create(res_regex)) 
async def handle_admin_reference(client, message):
    user_states[message.from_user.id]["required_responses"]=re.search(r'^\d+$', message.text).group() # record required responses in a dictionary temporary
    user_states[message.from_user.id]["form_drive_link"]=None #record drive form link temporary
    user_states[message.from_user.id]["template_drive_link"]=None #record template drive link temporary

    await message.reply("Your Data recorded Successfully", reply_markup=ReplyKeyboardRemove())
    
    await insert_admin_data(message.from_user.id,user_states[message.from_user.id]["required_responses"],user_states[message.from_user.id]["form_drive_link"],user_states[message.from_user.id]["template_drive_link"])

    #enter that dictionary streaght to the admin data table


'''

                             Send scheduled birthday card

'''


async def scheduled_send_birthday_cards():
    await app.send_photo(chat_id="chat_id",photo="photo_path",caption="caption")
    today=datetime.date.today()
    current_day=today.day
    current_month=today.month

async def daily_task():
    # Define the task you want to run at 12:00 PM every day
    chat_id = "l_w_ravishan"  # Replace with your chat ID
    message = "This is a scheduled message sent at 12:00 PM"
    await app.send_message(chat_id, message)

def schedule_tasks():
    schedule.every().day.at("18:57").do(lambda: asyncio.create_task(daily_task()))

async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def main():
    
        # Schedule tasks
        schedule_tasks()
        
        # Run both the bot and the scheduler
        await asyncio.gather(
            app.start(),
            scheduler()
        )

# Run the bot using the existing event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())