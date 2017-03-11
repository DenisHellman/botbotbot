# Шаг 2 / ВЫБОР ЗАДАНИЯ
@bot.message_handler(content_types=['text'])
def text(m):
    if m.text == "📦 Задания":
        bot.send_message(m.from_user.id, 'Пожалуйста, выберите задание:')
        directory = 'C:/Photo'
        all_files_in_directory = os.listdir(directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(m.from_user.id, 'upload_photo')
            bot.send_photo(m.from_user.id, img, caption='Здесь скоро будет описание задания №1.',
                           reply_markup=keyboard2)
            img.close()
