import os
from pyrogram import Client, filters

# Create a Telegram bot client
bot = Client("reel_downloader_bot")

# Define the command handler for downloading reels
@bot.on_message(filters.command("download_reel"))
def download_reel(client, message):
    # Get the reel URL from the message
    reel_url = message.text.split()[1]

    # Download the reel using the instaloader library
    from instaloader import Instaloader, Post
    loader = Instaloader()
    post = Post.from_url(loader.context, reel_url)
    loader.download_post(post, target="reels")

    # Send a message to the user with the downloaded reel
    message.reply_document("reels/" + post.shortcode + ".mp4")

# Start the bot
bot.run()
