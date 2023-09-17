import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import instaloader

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Welcome to the Instagram Media Downloader Bot! Send me the link to an Instagram post and I will download the media for you.')

# Define the command handler for the /download command
def download(update: Update, context: CallbackContext) -> None:
    """Download the media from the given Instagram post URL."""
    url = update.message.text.split(' ')[1]
    try:
        # Create an instance of Instaloader
        L = instaloader.Instaloader()
        # Download the media from the given URL
        L.download_post(url, target='media/')
        update.message.reply_text('Media downloaded successfully!')
    except Exception as e:
        update.message.reply_text(f'Error: {str(e)}')

def main() -> None:
    """Start the bot."""
    # Create an instance of Updater and pass your bot token
    updater = Updater('YOUR_BOT_TOKEN')

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('download', download))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
