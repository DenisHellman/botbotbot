# Шаг 1 / ЗАГЛАВНАЯ СТРАНИЦА
@bot.message_handler(commands=['start'])
def start(message):
    userid = message.from_user.id
    balance = 0
    bd = "../base.txt"
    bd = open(bd, mode='a', encoding='utf_8')
    bd.write(str(userid) + str(balance))
    bd.close()
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=menu_markup)
