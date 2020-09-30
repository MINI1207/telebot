'''
import telebot

#Mini_first_bot
my_bot = telebot.TeleBot("1259052437:AAGNMhKvsnvIn_KRiBUmKmlgwUb0PAnI17E")

@my_bot.message_handler(commands=['start'])
def send_welcome(message):
        my_bot.reply_to(message, "This is mine first bot, you are welcome!!!")
        print(dir(message))

my_bot.polling()
'''

import telebot

#Mini_first_bot
my_bot = telebot.TeleBot("1259052437:AAGNMhKvsnvIn_KRiBUmKmlgwUb0PAnI17E")

@my_bot.message_handler(commands=['start', "say_again"])
def send_welcome(message):
        my_bot.reply_to(message, "This is mine first bot. " + str(message.from_user.first_name) + "is welcome...")
        print("Message from : " + message.from_user.first_name)

@my_bot.message_handler(func=lambda m:True)
def send_echo_as_reply(msg):

        print(msg.from_user.first_name + "said : " + msg.text)
        my_bot.reply_to(msg, msg.text)

my_bot.polling()
