import telebot
from telebot import types

bot = telebot.TeleBot('7165536243:AAE7lW5MPMqRqKStWgl-_i9Q_IzMgqvluYQ')


@bot.message_handler(commands=['start'])
def start(message):
    # приветствуем нового пользователя, исполшьзуя его ник
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# отслеживаем соманду website
@bot.message_handler(commands=['website'])
def website(message):
    # создаем кнопку, встроенную в сообщение
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://shorthaired-beautiful-play.glitch.me/'))
    # прикрепляем кнопку к сообщению
    bot.send_message(message.chat.id, 'Сайт', reply_markup=markup)


@bot.message_handler(commands=['car'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://auto.ru/'))
    bot.send_message(message.chat.id, 'Сайт', reply_markup=markup)


@bot.message_handler(commands=['house'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.avito.ru/orenburg/nedvizhimost'))
    bot.send_message(message.chat.id, 'Сайт', reply_markup=markup)


@bot.message_handler(commands=['yandex_lms'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://lms.yandex.ru/'))
    bot.send_message(message.chat.id, 'Сайт', reply_markup=markup)


# отслеживаем команду help
@bot.message_handler(commands=['help'])
def website(message):
    # создаем кнопки(шаблоны сообщений)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # создаем сами кнопки
    website = types.KeyboardButton('/website')
    car = types.KeyboardButton('/car')
    house = types.KeyboardButton('/house')
    yandex_lms = types.KeyboardButton('/yandex_lms')
    # компонуем
    markup.add(website, house, yandex_lms, car)
    bot.send_message(message.chat.id, 'Выбери сайт', reply_markup=markup)


# отслеживаем некоторые текстовые надписи
@bot.message_handler()
def user_text(message):
    # если пользователь написал "привет", то бот с ним в ответ тоже здоровается
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    # если пользователь запрашивает свой id, то бот ему его выводит
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    # а если пользователь вводит что-то другое, то бот выводит что он не понимает пользователя
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


# отслеживаем не отправил ли пользователь фото
@bot.message_handler(content_types=['photo'])
def user_photo(message):
    # реакция от бота на фото
    bot.send_message(message.chat.id, 'Вау, крутое фото!', parse_mode='html')


bot.polling(none_stop=True)
