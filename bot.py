import telebot
from googletrans import Translator
bot = telebot.TeleBot("6939522169:AAHeF0yiGODaLIwZ3E2ff2XQ3Z49HB-840E")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Salom Lazizbek Mirzayevdan yana bir bot English-Uzbek translate botga xush kelibsiz matn kititing faqat uzbekcha yoki englizcha bo'lishi kerak")
@bot.message_handler(func=lambda message: True)
def translate_text(message):
    tarjimon = Translator()
    matn = message.text
    tarjima = Translator().detect(matn)
    nima = tarjima.lang
    if nima == 'en':
        tarjima_en = tarjimon.translate(matn,src='en',dest='uz')
        bot.send_message(message.chat.id,f'Tarjima : {tarjima_en.text}')
    elif nima == 'uz':
        tarjima_uz = tarjimon.translate(matn,src='uz',dest='en')
        bot.send_message(message.chat.id,f" Tarjima : {tarjima_uz.text}")
    else:
        bot.send_message(message.chat.id,"Nimadir xato ketdi Bilib qo'ying bu English-Uzbek bot")
bot.polling()