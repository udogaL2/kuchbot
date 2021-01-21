import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('1522582454:AAGK3_IIqjkFzQR1VsezBMku3a181vU3mq0')


@bot.message_handler(commands=['start'])
def welcome(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Где куч?")
    item2 = types.KeyboardButton("Через сколько придет куч?")

    markup.add(item1, item2)
    bot.send_message(msg.chat.id,
                     'Добро пожаловать, {0.first_name}!\nМеня зовут <b>"{1.first_name} - бот"</b>. Я расскажу тебе всё о местоположении куча на данный момент.😊'.format(
                         msg.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def ans(msg):
    if msg.chat.type == 'private':
        if msg.text == 'Где куч?':
            bot.send_message(msg.chat.id, 'Он скоро придёт.')
        elif msg.text == 'Через сколько придет куч?':
            s = randint(1, 3)
            l = 'ы'
            if s == 1:
                l = 'у'
            bot.send_message(msg.chat.id, 'Он придёт через {} секунд{}.'.format(str(s), l))
        else:
            bot.send_message(msg.chat.id, 'Зачем мне писать что-то, кроме сообщений о местоположении куча?')


bot.polling(none_stop=True)
