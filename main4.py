import json
from telebot import TeleBot, types

TOKEN = '7026607213:AAHJSkdcb2eR8cFaYlgsrSdQfjhnXobT6nA'
bot = TeleBot(TOKEN)

with open('quizz.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)

game = False
indx = 0
points = 0

def get_question(data, indx):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(4):
        button = types.KeyboardButton(data[indx]['вариант'][i])
        markup.add(button)
    markup.add(types.KeyboardButton('Выход'))
    return markup

@bot.message_handler(commands=['quizz'])
def quizz(message):
    global game
    global indx
    game = True
    markup = get_question(data, indx)
    bot.send_message(message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)

@bot.message_handler()
def victorinas(message):
    global game
    global indx
    global points
    if game:
        if message.text == data[indx]['ответ']:
            bot.send_message(message.chat.id, 'Правильно')
            points += 1
        elif message.text == 'Выход':
            game = False
            bot.send_message(message.chat.id, 'Пока')
            return
        else:
            bot.send_message(message.chat.id, f'Неправильно! Правильный ответ - {data[indx]['ответ']}')
        indx += 1

        markup = get_question(data,indx)
        bot.send_message(message.chat.id, text = data[indx]['вопрос'], reply_markup=markup)
        bot.send_message(message.chat.id, f"Заработано очков: {points}")




if __name__ == '__main__':
    bot.polling(non_stop=True)
