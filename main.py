import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot('1522582454:AAGK3_IIqjkFzQR1VsezBMku3a181vU3mq0')


@bot.message_handler(commands=['start'])
def welcome(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Где куч?")
    item2 = types.KeyboardButton("Через сколько придет куч?")
    item3 = types.KeyboardButton("Сколько времени куч будет в классе?")

    markup.add(item1, item2, item3)
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
        elif msg.text == 'Сколько времени куч будет в классе?':
            mas = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3]
            s = choice(mas)
            m = 'Упс... Не могу проанализировать это.'
            if s == 0:
                m = 'Куч будет в классе 0 секунд. Вам повезло! Шанс равен 20%.'
            elif s == 1:
                m = 'Куч будет в классе 1 секунду. Обычное время нахождения куча. Шанс равен 45%.'
            elif s == 2:
                m = 'Куч будет в классе 2 секунды. Больше, чем обычно. Шанс равен 30%'
            elif s == 3:
                m = 'Куч будет в классе 3 секунды. Вам не повезло! Молитесь, чтоб не было Черниковой рядом... Шанс равен 5%.'
            bot.send_message(msg.chat.id, m)
        else:
            bot.send_message(msg.chat.id, 'Зачем мне писать что-то, кроме сообщений о местоположении куча?')


bot.polling(none_stop=True)
