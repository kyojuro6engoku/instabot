import os
from pyrogram import Client, filters

api_id = "8914119"
api_hash = "652bae601b07c928b811bdb310fdb4b0"
bot_token = "6390496152:AAElWXKiIeMSYJZ4InTVAexWJOkqeraEenA"

bot = Client("my_bot", api_id, api_hash, bot_token=bot_token)

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the Instagram Reel Downloader bot! Send me an Instagram Reel link, and I'll download it for you.")

@Client.on_message(filters.text & ~filters.command)
def your_message_handler(client, message):
    # Your message handling code here

    # Check if the message contains a link
    if "https://www.instagram.com/reel/" in message.text:
        # Rest of your code for downloading reels

# Start the bot
        app = Bot()
        app.run()
