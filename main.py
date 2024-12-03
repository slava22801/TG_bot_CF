import telebot
from telebot import types
from bd import initDb, initUser

bot = telebot.TeleBot('7749042989:AAEsYCfXcMsuGZtV8cjIjFvu91nfE286uNc')

# Инициализация БД
initDb()

# меню
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
write = types.KeyboardButton("Записать событие")
events = types.KeyboardButton("События")
delete = types.KeyboardButton("Удалить событие")
edit = types.KeyboardButton("Редактировать событие")
menu.add(write, events, delete, edit)


# кнопка назад
back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton("Назад")
back.add(back_button)



# обработка команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    print(f"Start command received from {message.chat.id}")  # Логирование команды start

    initUser(message.chat.id)
    gif_url = 'https://media.giphy.com/media/lSVL6vdhdZVPW/giphy.gif?cid=790b761126yc80ko2dcmrks4hjxlimcfoo74ru2678kk5a7m&ep=v1_gifs_search&rid=giphy.gif&ct=g'  # Замените на URL вашего GIF
    bot.send_animation(message.chat.id, gif_url)
    bot.send_message(message.chat.id, "Привет Salam aleikum", reply_markup=menu)




# реакции на кнопки
@bot.message_handler(content_types=['text'])
def text_messages(message):
    print(f"Received message: {message.text}")  # Логирование входящих сообщений
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=menu)
    elif message.text == "События":
        bot.send_message(message.chat.id, "Записанные события", reply_markup=back)


    elif message.text == "Записать событие":


        bot.send_message(message.chat.id, "Введите дату (дд-мм-гггг, день месяц год)", reply_markup=types.ReplyKeyboardRemove())


    elif message.text == "Удалить событие":
        bot.send_message(message.chat.id, "Выберите событие которое нужно удалить", reply_markup=back)
    elif message.text == "Редактировать событие":
        bot.send_message(message.chat.id, "Выберите событие которое нужно редактировать", reply_markup=back)



bot.infinity_polling()