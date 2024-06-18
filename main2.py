from random import choice, randint
from telebot import TeleBot 

TOKEN = '7167303470:AAHSYTncF0PTAWpP4AgJVTqtiRR30rwyRgI'
bot = TeleBot(TOKEN)

game_choice = ['камень', 'ножницы', 'бумага']

class Game:
    user = 0
    comp = 0

    def update(self, user_winner):
        if user_winner:
            self.user += 1
            return 'Победил'
        self.comp += 1
        return 'Проиграл'
    def reset(self):
        self.user = 0
        self.comp = 0

gm = Game()

@bot.message_handler(func=lambda x: x.text.lower() in game_choice)
def game(message):
    user_choice = message.text.lower()
    bot_choice = choice(game_choice)
    bot.send_message(message.chat.id, bot_choice)
    
    if user_choice == 'камень' and bot_choice == 'ножницы':
        msg = gm.update(user_winner=True)

    elif user_choice == 'ножницы' and bot_choice == 'бумага':
        msg = gm.update(user_winner=True)

    elif user_choice == 'бумага' and bot_choice == 'камень':
        msg = gm.update(user_winner=True)

    elif user_choice == bot_choice:
        msg = 'Ничья'
    
    else:
        msg = gm.update(user_winner=False)
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['points'])
def points(message):
    img = open('play.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.send_message(message.chat.id, f"бот: {gm.comp} игрок: {gm.user}")

@bot.message_handler(commands=['reset'])
def reset(message):
    user_poinsts = 0
    bot_poinsts = 0
    bot.send_message(message.chat.id, 'Очки обнулены')


@bot.message_handler(commands = ['lootbox'])
def lootbox(message):
    if gm.user == 0:
        bot.send_message(message.chat.id, 'У вас недостаточно очков, чтобы играть')
        return
    gm.user -= 1
    number = randint(1,100)
    if number <= 80:
        image = 'common.jpg'
    elif number <= 95:
        image = 'rare.jpg'
    else:
        image = 'super_rare.jpg'
    img = open('play.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.send_message(message.chat.id, f"Осталось очков: {gm.user}")

if __name__ == '__main__':
    bot.polling(non_stop=True)