import telebot
from telebot import types
from random import randint, choice
from create_user import make_user
import time
from multiprocessing import *
import schedule
from get_id import get_id

bot = telebot.TeleBot('1522582454:AAGK3_IIqjkFzQR1VsezBMku3a181vU3mq0')
# ________________________________

main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Где куч?")
item2 = types.KeyboardButton("Через сколько придет куч?")
item3 = types.KeyboardButton("Сколько времени куч будет в классе?")
item4 = types.KeyboardButton("Хто я?")

main_markup.add(item1, item2, item3, item4)

# ________________________________


# ________________________________
# Ответы

WHERE_IS_KUCH_ANS = {'У завуча.': ['Зачем?'], 'Играет в телефон.': ['Во что?'], 'Занимается с Ксюшей.': ['Чем?'],
                     'Курит.': ['Что?'], 'Отчитывает ' + str(randint(5, 11)) + ' класс.': ['Зачем?'],
                     'Заваривает кофе.': ['Зачем?'], 'Пьёт кофе.': ['Для чего?'],
                     'Гуляет с собакой.': ['Где?', 'Зачем?'], 'Лечит глаза.': ['Зачем?'],
                     'На почте.': ['С какой целью?'], 'В поликлинике.': ['С какой целью?'],
                     'Печатает варианты.': ['Кому?'], 'Спит.': ['С кем?'], 'Смотрит фильм.': ['Какой?'],
                     'Разговаривает по телефону.': ['С кем?']}

NAMES = ['Ты обослтус!', 'Дармоед', 'Бездельник', 'Лодырь', 'Тунеядец', 'Двоечник', 'Питонист', 'Хам',
         'Разгильдяй']


# ________________________________


def start_process():
    p1 = Process(target=P_schedule.start_schedule, args=())
    p1.start()


class P_schedule():
    def start_schedule():
        schedule.every().monday.at("14:20").do(P_schedule.send_message1)
        schedule.every().tuesday.at("12:30").do(P_schedule.send_message1)
        schedule.every().wednesday.at("10:40").do(P_schedule.send_message1)
        schedule.every().wednesday.at("11:40").do(P_schedule.send_message1)
        schedule.every().friday.at("09:40").do(P_schedule.send_message1)
        schedule.every().friday.at("10:40").do(P_schedule.send_message1)
        schedule.every().monday.at("14:25").do(P_schedule.send_message2)
        schedule.every().tuesday.at("12:35").do(P_schedule.send_message2)
        schedule.every().wednesday.at("10:45").do(P_schedule.send_message2)
        schedule.every().wednesday.at("11:45").do(P_schedule.send_message2)
        schedule.every().friday.at("09:45").do(P_schedule.send_message2)
        schedule.every().friday.at("10:45").do(P_schedule.send_message2)
        schedule.every(1).minute.do(P_schedule.send_message2)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def send_message1():
        id = get_id()
        for i in id:
            bot.send_message(i, 'Я скоро приду.')

    def send_message2():
        id = get_id()
        for i in id:
            bot.send_message(i, 'Я обязательно приду!')


@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id,
                     '''Добро пожаловать, {0.first_name}! \nМеня зовут <b>"{1.first_name} - бот"</b>. 
Я расскажу тебе всё о местоположении куча на данный момент.'''.format(
                         msg.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=main_markup)
    bot.send_message(
        '753613553', '''#newperson\n<b>id: {0}\nusername: {1}\nname: {2}</b> только что запустил бота!'''.format(
            msg.from_user.id, msg.from_user.username, msg.from_user.first_name),
        parse_mode='html')

    make_user(msg.from_user.id, msg.from_user.username)


@bot.message_handler(commands=['restart'])
def welcome(msg):
    bot.send_message(msg.chat.id,
                     '''Добро пожаловать, {0.first_name}! \nМеня зовут <b>"{1.first_name} - бот"</b>. 
Я расскажу тебе всё о местоположении куча на данный момент.'''.format(
                         msg.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=main_markup)


@bot.message_handler(content_types=['text'])
def ans(msg):
    if msg.chat.type == 'private':
        if msg.text == 'Где куч?':

            ans = choice(list(WHERE_IS_KUCH_ANS))

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for i in list(WHERE_IS_KUCH_ANS[ans]):
                markup.add(types.KeyboardButton(i))

            bot.send_message(msg.chat.id, ans, reply_markup=markup)
        elif msg.text == 'Через сколько придет куч?':
            s = randint(1, 3)
            l = 'ы'
            if s == 1:
                l = 'у'
            bot.send_message(msg.chat.id, 'Он придёт через {} секунд{}.'.format(str(s), l), reply_markup=main_markup)
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
            bot.send_message(msg.chat.id, m, reply_markup=main_markup)
        elif msg.text == "Хто я?":
            bot.send_message(msg.chat.id, choice(NAMES), reply_markup=main_markup)
        elif msg.text == 'Зачем?':
            bot.send_message(msg.chat.id, 'Да!', reply_markup=main_markup)
        elif msg.text == 'Во что?':
            bot.send_message(msg.chat.id, 'Да!', reply_markup=main_markup)
        elif msg.text == 'Чем?':
            bot.send_message(msg.chat.id, choice(['Да!', '300$!']), reply_markup=main_markup)
        elif msg.text == 'Что?':
            bot.send_message(msg.chat.id, 'Да!', reply_markup=main_markup)
        elif msg.text == 'Для чего?':
            bot.send_message(msg.chat.id, 'Прост)0))0', reply_markup=main_markup)
        elif msg.text == 'Где?':
            bot.send_message(msg.chat.id, 'Да!', reply_markup=main_markup)
        elif msg.text == 'С какой целью?':
            bot.send_message(msg.chat.id, 'Да!', reply_markup=main_markup)
        elif msg.text == 'Кому?':
            bot.send_message(msg.chat.id, 'Тебе, лол)0)0))', reply_markup=main_markup)
        elif msg.text == 'С кем?':
            bot.send_message(msg.chat.id, 'Да!', reply_markup=main_markup)
        elif msg.text == 'Какой?':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('За сколько?'))

            bot.send_message(msg.chat.id, 'Gachi!', reply_markup=markup)
        elif msg.text == 'За сколько?':
            bot.send_message(msg.chat.id, '300$!', reply_markup=main_markup)

        else:
            bot.send_message(msg.chat.id, 'Зачем мне писать что-то, кроме сообщений о местоположении куча?',
                             reply_markup=main_markup)


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except Exception:
        pass
