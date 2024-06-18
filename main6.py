from time import time
from telebot import TeleBot, types

TOKEN = from telebot import TeleBot, types
from time import time
from random import randint



TOKEN = ваш токен
bot = TeleBot(TOKEN)



with open("bad_words.txt", 'r', encoding='utf-8') as f:
    data = [word.strip().lower() for word in f.readlines()]


sum_check = 0

def is_group(message):
    return message.chat.type in ('group', 'supergroup')


@bot.message_handler(commands=["check"])
def default_test(message):
    global sum_check
    keyboard = types.InlineKeyboardMarkup()
    numbers = ["один", "два", "три", "четыре", "пять",
               "шесть", "семь", "восемь", "девять", "десять"]
    keys = []
bot = TeleBot(TOKEN)

def is_group(message):
    return message.chat.type in ('group', 'supergroup')

@bot.message_handler(func=lambda message: message.entities is not None and is_group(message))
def delete_links(message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            bot.delete_message(message.chat.id, message.message_id)

with open ('bad_words.txt', 'r', encoding='utf-8') as f:
    data = [word.strip().lower() for word in f.readlines()]

def has_bad_words(text):
    message_words = text.split(' ')
    for word in message_words:
        if word in data:
            return True
    return False

@bot.message_handler(func=lambda message: has_bad_words(message.text.lower()) and is_group(message))
def bad_bad_words(message):
    bot.restrict_chat_member(
        message.chat.id,
        message.from_user.id,
        until_date=time()+20)

    bot.send_message(message.chat.id, text='Тебе бан на 20 cек',
                     reply_to_message_id=message.message_id)
    bot.delete_message(message.chat.id, message.message_id)

if __name__ == "__main__":
    bot.polling(non_stop=True)