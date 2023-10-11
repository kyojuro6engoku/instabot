import os
from pyrogram import Client, filters

python
from pyrogram import Client, filters
import os

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

Client("my_bot", api_id, api_hash, bot_token=bot_token)

@Client.on_message(filters.text & ~filters.command)
async def download_reels(client, message):
    # Check if the message contains a link
    if "https://www.instagram.com/reel/" in message.text:
        # Download the reel
        reel_url = message.text.split()[0]
        os.system(f"instaloader --no-metadata-json --no-compress-json --no-captions --no-videos --no-pictures --no-video-thumbnails --no-post-metadata --no-story-items --no-stories --no-profile-pic --no-highlights --no-feed --no-saved --no-tagged --no-tagged-posts --no-tagged-posts-full --no-tagged-feed --no-tagged-feed-full --no-tagged-stories --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tagged-stories-full --no-tag


    # Download the reel using the instaloader library
    from instaloader import Instaloader, Post
    loader = Instaloader()
    post = Post.from_url(loader.context, reel_url)
    loader.download_post(post, target="reels")

    # Send a message to the user with the downloaded reel
    message.reply_document("reels/" + post.shortcode + ".mp4")

# Start the bot
bot.run()
