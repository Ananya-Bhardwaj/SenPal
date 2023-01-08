import os
from telegram import Update #upm package(python-telegram-bot)
from telegram.ext import *
import keys
import webbrowser

print('Starting up bot.........')


def start_command(update, context):
  update.message.reply_text('''Hello there! I am there for your assistance!
    What do you want? You can do the following with me: 
        1. Type /medicine to get medical assistance 
        2. Type /grocery to order Groceries 
        3. Type /game to play games 
    ''')


def help_command(update, context):
  update.message.reply_text('I am there for you')


def medicine_command(update, context):
  webbrowser.open('https://telegram.me/icliniqBot')


def game_command(update, context):
  webbrowser.open('https://telegram.me/gamebot')


def grocery_command(update, context):
  webbrowser.open('https://telegram.me/grocerylistbot')

def songmov_command(update, context):
  webbrowser.open('https://t.me/youtube')


def news_command(update, context):
  webbrowser.open('https://t.me/youtube')


def shopping_command(update, context):
  webbrowser.open('https://t.me/shopbot')


#takes a string and ->returns a string
def handle_response(text: str) -> str:
  if 'help' in text:
    return '''What do you want? You can do the following with me: 
        1. Type /medicine to get medical assistance 
        2. Type /grocery to order Groceries 
        3. Type /game to play games '''

  if 'how are you' in text:
    return 'I am fine'

  if 'bored' or 'bore' in text:
    return ''' What can I do for you? 
      1. Open game /game
      2. Play songs 
      3. Send news '''

  #if none of the above if statements work return idk
  return 'idk'


def handle_message(update, context):
  message_type = update.message.chat.type
  text = str(update.message.text).lower()

  response = handle_response(text)

  update.message.reply_text(response)


if __name__ == '__main__':
  updater = Updater(keys.token, use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler('start', start_command))
  dp.add_handler(CommandHandler('help', help_command))
  dp.add_handler(CommandHandler('medicine', medicine_command))
  dp.add_handler(CommandHandler('game', game_command))
  dp.add_handler(CommandHandler('grocery', grocery_command))
  dp.add_handler(CommandHandler('song', songmov_command))
  dp.add_handler(CommandHandler('news', news_command))
  dp.add_handler(CommandHandler('shop', shopping_command))


  dp.add_handler(MessageHandler(Filters.text, handle_message))

  #check for updates every one second
  updater.start_polling(1.0)
  updater.idle()
