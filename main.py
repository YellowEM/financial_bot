#телерам бот, считывающий расходы с анализом
import telebot

bot = telebot.TeleBot("5598305102:AAF68rW_fWOKLIPnrJhyQEzg8Zxokdmri4k")

@bot.message_handler(commands= ['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, путник, в обработке твоих зелёных деньжат. Будь добр, следи инструкциям:'
                    'Пример добавления расхода: 100 магазин'
                     "Траты сегодня: ")

@bot.message_handler()
def user_text(message):
    bot.send_message(message.chat.id)
