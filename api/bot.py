import telebot
import requests

bot = telebot.TeleBot('876869920:AAFLGJvSEInwblEcQXIw7QfuDyHP0FFDHWo')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add('/start')  # Имена кнопок
    msg = bot.reply_to(message, 'Напишите Жалобу: \n1)Текст для жалобы', reply_markup=keyboard)


@bot.message_handler(content_types=['text', 'image'])
def send_text(message):
    #     count = 0
    #     if message.text and count == 0:
    #         count += 1
    #         bot.send_message(message.chat.id, 'Теперь отправьте фото')
    if message.text:
        requests.post('http://194.67.210.80/api/create/', data={'title': message.text, 'image': message.text})


bot.polling(none_stop=True, interval=0)
