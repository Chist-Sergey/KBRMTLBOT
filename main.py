import telegram
import telegram.ext
import os
import dotenv
dotenv.load_dotenv()


async def main(
    update: telegram.Update,
    context: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:
    """Removes any existing reply keyboard from a group chat."""
    await context.bot.send_message(
        text='Deleted.',
        chat_id=update.effective_chat.id,
        reply_markup=telegram.ReplyKeyboardRemove(),
    )


if __name__ == '__main__':
    bot = telegram.ext.ApplicationBuilder(
    ).token(os.getenv('TOKEN')).build()

    bot.add_handler(telegram.ext.CommandHandler('start', main))

    bot.run_polling(poll_interval=5)
