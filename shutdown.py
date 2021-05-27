
# pip install pyTelegramBotAPI #

import telebot
import threading
from time import sleep


telegram_API_Key = ''
bot = telebot.TeleBot(telegram_API_Key)

author_id_prev = ""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global author_id_prev
    chat_id = message.chat.id
    author_id = message.from_user.id
    if str(author_id) == "" and str(message.from_user.first_name) == "" and str(message.from_user.last_name) == "" and str(message.from_user.username) == "":
        try:
            bot.send_message(chat_id, """Ciao, spegni il computer con /spegni""")
        except Exception:
            return
    elif author_id_prev == author_id:
        return
    else:
        try:
            bot.send_message(chat_id, """non sei l'autore""")
        except Exception:
            return
    author_id_prev = author_id

@bot.message_handler(commands=['spegni'])
def send_api(message):
    global author_id_prev
    chat_id = message.chat.id
    author_id = message.from_user.id
    if str(author_id) == "" and str(message.from_user.first_name) == "" and str(message.from_user.last_name) == "" and str(message.from_user.username) == "":
        try:
            bot.send_message(chat_id, (f'sto spegnendo, per spegnere /spegni'))
            bot.stop_polling() 
        except Exception:
            return
        import subprocess
        subprocess.call(["shutdown", "/s", "/t", "00"])
    elif author_id_prev == author_id:
        return
    else:
        try:
            bot.send_message(chat_id, (f'non sei autorizzato a spegnermi il pc'))
        except Exception:
            return
    author_id_prev = author_id

def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            bot.stop_polling()
            break
        else:
            bot.stop_polling()
            break

polling_thread = threading.Thread(target=main)
polling_thread.daemon = True
polling_thread.start()

if __name__ == '__main__':
    a = 0
    while True:
        a += 1
        sleep(120)
