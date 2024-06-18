from random import randint, choice
from telebot import TeleBot 

TOKEN = '7107554675:AAFHCZuoC3oT6G9zmrdtl-A9TMBx37G0YZk'
bot = TeleBot(TOKEN)

jokes=['-Как называют человека, который продал свою печень? -Обеспеченный.',
       '-В какой стране продаётся только оригинальная продукция? -В Непале',
       '-Что сказал слепой, войдя в бар? -Всем привет, кого не видел.']

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['sum'])
def sum (message):
    vals = message.text.split(' ')
    number = int(vals[1]) + int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=['mult'])
def mult (message):
    vals = message.text.split(' ')
    number = int(vals[1]) * int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=['dl'])
def dl (message):
    vals = message.text.split(' ')
    number = int(vals[1]) / int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=['deduct'])
def deduct (message):
    vals = message.text.split(' ')
    number = int(vals[1]) - int(vals[2])
    bot.send_message(message.chat.id, number)



@bot.message_handler()
def start(message):
    if message.text == 'Пошути':
        bot.send_message(message.chat.id, choice(jokes))
        return
    
    if message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Хорошо, а у тебя?')
        return
    
    if message.text == 'Что делаешь?':
        bot.send_message(message.chat.id, 'Бип...Бип...')
        return
    
    bot.send_message(message.chat.id, message.text)
    
if __name__ == '__main__':
    bot.polling(none_stop = True)

