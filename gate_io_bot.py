import csv
import telebot

with open('selected_list.csv', 'r') as f:
        rows = list(csv.reader(f))

a = rows[0][0]

bot = telebot.TeleBot('6565244721:AAFFZmNxxg6yo-WeDdOZvnlhqhkkZtsIzko')

@bot.message_handler(commands=['start'])
def main(message):
    for row in rows:
        bot.send_message(message.chat.id, f'{row[0]} +{row[4]}%')



bot.polling(non_stop=True)
