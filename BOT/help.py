import asyncio
import schedule
from pyrogram import Client, filters
from datetime import datetime


# Replace 'my_bot' with your bot's name and add your API credentials
app = Client("my_bot", api_id=19778892, api_hash="4dd7e1b7d22ec89dd9e9058fcd35af8b", bot_token="7459345245:AAG-1jFLfdst5ca3iaZLcrLE95P4kblqZQ8")

async def daily_task():
    # Define the task you want to run at 12:00 PM every day
    chat_id = "l_w_ravishan"  # Replace with your chat ID
    message = "This is a scheduled message sent at 12:00 PM"
    await app.send_message(chat_id, message)

def schedule_tasks():
    schedule.every().day.at("18:51").do(lambda: asyncio.create_task(daily_task()))

async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Bot started!")

# Main function to run the bot and scheduler
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