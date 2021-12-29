import os
import telebot


bot = telebot.TeleBot("API Key Here")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! Shadow Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/General_Knowledge_Quiz_SL_Group")



bot.polling()
