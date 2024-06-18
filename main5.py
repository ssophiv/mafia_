import json
from random import choice
from telebot import TeleBot, types

TOKEN = '7026607213:AAHJSkdcb2eR8cFaYlgsrSdQfjhnXobT6nA'
bot = TeleBot(TOKEN)

with open('cities.txt', 'r', encoding='utf-8') as f:
    cities = []
    for line in f.readlines():
        cities.append(line.strip().lower())

game = False
used_cities = []
letter = ''
points = 0
leaderboard = {}

def select_letter(text):
    i = 1
    while text[-1*i] in ('ь', 'ы', 'й'):
        i += 1
    return text[-1*i]

@bot.message_handler(commands=['cities'])
def start_game(message):
    global game
    global letter
    game = True
    city = choice(cities)
    letter = select_letter(city)
    bot.send_message(message.chat.id, text = city)

@bot.message_handler(commands=['leaderboard'])
def leaderboad(message):
    with open('scores.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    leaders_str = ''
    for user, user_points in data.items():
        leaders_str += user + ' ' + str(user_points) + '\n'
    bot.send_message(message.chat.id, text=leaders_str)

@bot.message_handler(commands=['save'])
def save(message):
    with open('scores.json', 'w', encoding='utf-8') as f:
        json.dump(leaderboard, f)
    bot.send_message(message.chat.id, 'Прогресс сохранён!')

@bot.message_handler()
def g(message):
    global used_cities
    global letter
    global game
    global points
    if game:
        if message.text.lower() in used_cities:
            bot.send_message(message.chat.id, 'Этот город уже был')
            return

        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id, 'Не то слово')
            return
        
        if message.text.lower() in cities:
            if message.from_user.first_name in leaderboard:
                leaderboard[message.from_user.first_name] += 1
            else:
                leaderboard[message.from_user.first_name] = 1
            letter = select_letter(message.text.lower())
            used_cities.append(message.text.lower())
            for city in cities:
                if city[0] == letter and city not in used_cities:
                    letter = select_letter(city)
                    bot.send_message(message.chat.id, city)
                    used_cities.append(city)
                    return
            bot.send_message(message.chat.id, 'Я проиграл')
            game = False
            return

        bot.send_message(message.chat.id, 'Такого города не существует')

if __name__ == '__main__':
    bot.polling(non_stop=True)

