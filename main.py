import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
TO_CHAT_ID = "-1001605494487"
evilListText = ['пліхан на ','плішко на ','йосип на ', 'йосипович на ', 'вахта на ']

@bot.message_handler(commands=['help'])
def helpFunc(message):
	bot.send_message(message.chat.id, "Щоб повідомити де зло, просто пишеш імя + на")

@bot.message_handler(commands=['chanel'])
def helpFunc(message):
	bot.send_message(message.chat.id, "Щоб завжди знати де зло підпишись на цей канал: https://t.me/+Hs6diV14g200ZDdi")

@bot.message_handler(content_types=['text'])
def listen(message):
	text = message.text.lower()
	for pl in evilListText:
		if pl == 'плішко на хую': 
			bot.send_message(message.chat.id, "А ти з ним?")
			return

		if text.find('пліхан на хую') >= 0: 
			bot.send_message(message.chat.id, "Шас замість нього сядеш! Тут тільки корисна інфа")
			return

		if(text.find(pl) >= 0): 
			bot.send_message(TO_CHAT_ID,"{0} ХОДИТЬ! \n{1}".format(pl.upper().split(" ")[0], message.text))


bot.infinity_polling()


