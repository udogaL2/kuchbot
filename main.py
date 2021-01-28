import telebot
from telebot import types
from random import randint, choice
from create_user import make_user
import time
import datetime
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
item5 = types.KeyboardButton("Что поставите?")

main_markup.add(item1, item2, item3, item4, item5)

# ________________________________


# ________________________________
# Ответы

WHERE_IS_KUCH_ANS = {'У завуча.': ['Зачем?'], 'Играет в телефон.': ['Во что?'], 'Занимается с Ксюшей.': ['Чем?'],
                     'Курит.': ['Что?'], 'Отчитывает {} класс.': ['Зачем?'],
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
        print('Start')
        # -2 часа для heroku
        schedule.every().monday.at("14:15").do(P_schedule.send_message1)
        schedule.every().tuesday.at("11:30").do(P_schedule.send_message1)
        schedule.every().wednesday.at("09:40").do(P_schedule.send_message1)
        schedule.every().wednesday.at("10:40").do(P_schedule.send_message1)
        schedule.every().friday.at("08:40").do(P_schedule.send_message1)
        schedule.every().friday.at("09:40").do(P_schedule.send_message1)
        schedule.every().monday.at("14:10").do(P_schedule.send_message2)
        schedule.every().tuesday.at("11:25").do(P_schedule.send_message2)
        schedule.every().wednesday.at("09:35").do(P_schedule.send_message2)
        schedule.every().wednesday.at("10:35").do(P_schedule.send_message2)
        schedule.every().friday.at("08:35").do(P_schedule.send_message2)
        schedule.every().friday.at("09:35").do(P_schedule.send_message2)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def send_message1():
        id = [i[0] for i in get_id()]
        for i in id:
            bot.send_message(int(i), 'Я скоро приду.')
        print('Я приду')

    def send_message2():
        id = [i[0] for i in get_id()]
        for i in id:
            bot.send_message(int(i), 'Я обязательно приду!')
        print('Я обязательно приду')


@bot.message_handler(commands=['start', 'restart'])
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
    print('new user')


@bot.message_handler(commands=['getusers'])
def give_id(msg):
    if msg.chat.id == 753613553:
        s = [i[0] + ' - ' + i[1] for i in get_id()]
        bot.send_message(msg.chat.id, '\n'.join(s))


@bot.message_handler(commands=['help'])
def give_help(msg):
    bot.send_message(msg.chat.id,
                     '''<b>Помощь</b>\nУправлять этим ботом проще всего при помощи специальной клавиатуры с кнопками, \
соответствующими доступным вариантам действий. Если клавиатура с кнопками пропала, нажмите на иконку в правой части \
поля ввода, и она появится.\n Доступные команды:\n<em>• "Где куч?"</em> - бот расскажет о местоположении куча;\n<em>• \
"Через сколько придет куч?"</em> - бот расскажет о времени прибытия куча;\n<em>• "Сколько времени куч будет в классе?"\
</em> - бот спрогнозирует время нахождения куча в классе;\n<em>• "Хто я?"</em> - бот даст вам имя по-кучуевски;\n<em>• \
"Что поставите?"</em> - бот поставит вам оценку, основываясь только на одном факте (по-моему он так и ставит оценки, \
лол)''', reply_markup=main_markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def ans(msg):
    if msg.chat.type == 'private':
        if msg.text == 'Где куч?':

            ans = choice(list(WHERE_IS_KUCH_ANS))

            if 'Отчитывает' in ans and 'класс.' in ans:
                ans = ans.format(str(randint(5, 11)))

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
        elif msg.text == 'Что поставите?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            it1 = types.InlineKeyboardButton("Да✔", callback_data='yes')
            it2 = types.InlineKeyboardButton("Нет❌", callback_data='no')

            markup.add(it1, it2)
            bot.send_message(msg.chat.id, 'Ты хорошая девочка?', reply_markup=markup)
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


@bot.message_handler(content_types=['sticker'])
def sticker(msg):
    sti = open('img/sticker.webp', 'rb')
    bot.send_sticker(msg.chat.id, sti)
    sti.close()


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                mark = choice([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 6, 6, 3, 3, 3, 3, 3])
                if mark == 6:
                    text = 'Я поставлю тебе ' + str(mark) + '. Да, именно 6, ты ведь хорошая девочка)00))0).'
                elif mark == 3:
                    text = 'Я поставлю тебе ' + str(mark) + '. У меня хорошие девочки тоже получают тройки.'
                else:
                    text = 'Я поставлю тебе ' + str(mark)
            elif call.data == 'no':
                mas = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
                text = 'Я поставлю тебе ' + str(choice(mas))

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=text, reply_markup=None)
            if mark == 6:
                sti = open('img/kappa.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                sti.close()
            elif call.data == 'yes' and mark == 3:
                sti = open('img/sticker.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                sti.close()

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except Exception:
        pass
