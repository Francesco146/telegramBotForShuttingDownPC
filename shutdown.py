
#pip install pyTelegramBotAPI

import telebot
import os

telegram_API_Key = ''
bot = telebot.TeleBot(telegram_API_Key)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, """\
        Ciao, spegni il computer con /spegni""")

@bot.message_handler(commands=['spegni'])
def send_api(message):
    chat_id = message.chat.id
    if str(message.from_user.id) == "" and str(message.from_user.first_name) == "" and str(message.from_user.last_name) == "" and str(message.from_user.username) == "":
        bot.send_message(chat_id, (f'sto spegnendo, per spegnere /spegni'))
        bot.stop_polling() 
        import subprocess
        subprocess.call(["shutdown", "/s", "/t", "00"])
    else:
        bot.send_message(chat_id, (f'non sei autorizzato a spegnermi il pc'))

def main():
    bot.polling()

if __name__ == '__main__':
    main()