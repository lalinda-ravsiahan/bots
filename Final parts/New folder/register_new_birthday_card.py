from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,ReplyKeyboardMarkup
import re
from helper_regex import*
from drive import*

async def kok(client,message,app):
    await message.reply("we are assigning your birthday card to this telegram account")
    keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Press This Button To Enter Card Name", callback_data="new_card_name")]
            ])
    await message.reply("see below", reply_markup=keyboard)

    def dynamic_data_filter(data):
        async def func(flt, _, query):
            return flt.data == query.data
        return filters.create(func, data=data)

    @app.on_callback_query(dynamic_data_filter("new_card_name"))
    async def prompt_text_input(client, query):
        await query.message.reply("Please enter your new card name ends with card like(UCSC21_card):")
    
    @app.on_message(filters.text & filters.private & filters.create(card_pattern))
    async def handle_card(client, message):
        await message.reply("You entered card name!", reply_markup=ReplyKeyboardRemove())

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Pres This Button to Enter Your Birthday Template", callback_data="card_template")]
            ])
        await message.reply("see below", reply_markup=keyboard)
    
    @app.on_callback_query(dynamic_data_filter("card_template"))
    async def prompt_text_input(client, query):
        await query.message.reply("Enter Birthday card Template Now")
    
    @app.on_message(filters.photo)
    async def handle_photo(client, message):
        # Download the photo
        file_path = await message.download()
        print(f"Photo downloaded to: {file_path}")

        os.remove(file_path)

        # we want to save the file path and the all saved in a dictionary then use them at the end
        # Prepare the file for Google Drive
        file_name = f"{message.photo.file_unique_id}.jpg"
        folder_id ="1Sozo47GnwbzBgG0nUJdpLtuizgkjSQNZ"

        # Respond to the user
        await message.reply_text("Photo received!")
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Press this button to enter your photo width and position", callback_data="dp_details")]
            ])
        await message.reply("see below", reply_markup=keyboard)
    @app.on_callback_query(dynamic_data_filter("dp_details"))
    async def prompt_text_input(client, query):
        await query.message.reply("Enter your photo width and position like 100px_x=45_y=56")
    
    @app.on_message(filters.text & filters.private & filters.create(dp_photo))
    async def handle_card(client, message):
        await message.reply("You entered dp deatils!", reply_markup=ReplyKeyboardRemove())

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Pres This Button to Enter person name details", callback_data="name_details")]
            ])
        await message.reply("see below", reply_markup=keyboard)
    
    @app.on_callback_query(dynamic_data_filter("name_details"))
    async def prompt_text_input(client, query):
        await query.message.reply("Enter your name font,(regular,bold,italic),font size,name position(y coordinates)")
    

    @app.on_message(filters.text & filters.private & filters.create(name_text))
    async def handle_card(client, message):
        await message.reply("You entered dp deatils!", reply_markup=ReplyKeyboardRemove())

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Pres This Button to Enter How Many responses do you need  ", callback_data="form_responses")]
            ])
        await message.reply("see below", reply_markup=keyboard)

    @app.on_callback_query(dynamic_data_filter("form_responses"))
    async def prompt_text_input(client, query):
        await query.message.reply("Enter the number of responses you want now like 100_res")
    
    @app.on_message(filters.text & filters.private & filters.create(responses))
    async def handle_card(client, message):
        await message.reply("You entered required google form responses successfully!", reply_markup=ReplyKeyboardRemove())

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Pres This Button to Enter Your details to the database and start the service  ", callback_data="start_service")]
            ])
        await message.reply("see below", reply_markup=keyboard)
    
    @app.on_callback_query(dynamic_data_filter("form_responses"))
    async def prompt_text_input(client, query):

        #enter the user data to databse and generade the google form and give him the register number

        await query.message.reply("Enter the number of responses you want now like 100_res")