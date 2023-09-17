import telegram
from telegram.ext import Updater, CommandHandler
import instaloader

def start(update, context):
         chat_id = update.effective_chat.id
         welcome_message = "Hello! Send me the Instagram URL for the media you want to download."
         context.bot.send_message(chat_id=chat_id, text=welcome_message)

def download_media(update, context):
         chat_id = update.effective_chat.id
         url = update.message.text  # Get the Instagram URL from the user's message
         # Download the media using Instaloader
         loader = instaloader.Instaloader()
         try:
             loader.download_profile(url, profile_pic_only=False)
             success_message = "Media downloaded successfully!"
             context.bot.send_message(chat_id=chat_id, text=success_message)
         except Exception as e:
             error_message = f"An error occurred: {str(e)}"
             context.bot.send_message(chat_id=chat_id, text=error_message)

  def main():
         updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
         dispatcher = updater.dispatcher
         # Add command handlers
         dispatcher.add_handler(CommandHandler("start", start))
         dispatcher.add_handler(MessageHandler(Filters.text, download_media))
         # Start the bot
         updater.start_polling()
         updater.idle()
     if __name__ == '__main__':
         main()
