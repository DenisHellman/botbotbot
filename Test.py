import telebot
from telebot import types

# Токен бота
bot = telebot.TeleBot("534534")

keyboard1 = types.InlineKeyboardMarkup(row_width=3)
callback_zadanie1 = types.InlineKeyboardButton(text="Задание 1", callback_data='Задание 1')
callback_zadanie2 = types.InlineKeyboardButton(text="Задание 2", callback_data='Задание 2')
callback_zadanie3 = types.InlineKeyboardButton(text="Задание 3", callback_data='Задание 3')

keyboard1.add(callback_zadanie1, callback_zadanie2, callback_zadanie3)

# Шаг 1 / ЗАГЛАВНАЯ СТРАНИЦА
@bot.message_handler(commands=['start'])
def start(m):
    menu_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    menu_markup.row('/start', '/stop')
    menu_markup.row('📦 Задания', '📢 О проекте')
    menu_markup.row('🏆 Мой баланс', '❓ Помощь')
    bot.send_message(m.from_user.id, 'Добро пожаловать!', reply_markup=menu_markup)

# Шаг 2 / ВЫБОР ЗАДАНИЯ
@bot.message_handler(content_types=['text'])
def text(m):
    if m.text == "📦 Задания":
        bot.send_message(m.from_user.id, 'Пожалуйста, выберите задание.', reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Задание 1':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                              text='Описание задания.', parse_mode='Markdown',
                              reply_markup=keyboard1)
    elif c.data == 'Задание 2':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                              text='Описание задания.', parse_mode='Markdown',
                              reply_markup=keyboard1)
    elif c.data == 'Задание 3':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                              text='Описание задания.', parse_mode='Markdown',
                              reply_markup=keyboard1)

# Проверка бота на запросы
bot.polling(none_stop=True)
