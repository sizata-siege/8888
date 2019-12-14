#IN THE NAME OF GOD

import os
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters 
from time import sleep

updater = Updater("919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM")

#def func (message , func):
#	updater.dispatcher.add_handler(CommandHandler('message' , func))
chat_id_var = ""
logger = "-1001309221311"
#logger = "753039129"
bot_progress_v = "وضعیت پیشرفت ربات"

def start_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "Hi {} {} 😐. WTF R U going to do ?\n/help".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.chat_id , update.message.from_user.first_name , update.message.from_user.last_name , update.message.from_user.username)#add name later
	#chat_id_var = "User "+update.message.chat_id+"started the bot"#add name in the future
	#bot.send_message(chat_id = "119940830" , text = "{} {} >>> start\n{}\n{}\n{}".format(update.message.from_user.first_name , update.message.from_user.last_name , update.message.chat_id , update.message.from_user.username))
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
	bot.send_message(chat_id = "119940830" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
	#send to channel

def chat_id_method(bot , update):
	bot.send_message(chat_id = update.send_message.chat_id , text = update.send_message.chat_id)
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ chat_id".format(update.message.from_user.first_name , update.message.from_user.last_name))

def help_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "/bot_progress ➡️ "+bot_progress_v+"\n")
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ help".format(update.message.from_user.first_name , update.message.from_user.last_name))

def bot_progress_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "Bot situation : 3%")
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ bot_progress".format(update.message.from_user.first_name , update.message.from_user.last_name))

def admin_method(bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️❓admin❓".format(update.message.from_user.first_name , update.message.from_user.last_name))
	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Prepairing ⌛️")
	sleep(2)
	bot.send_message(chat_id = update.message.chat_id , text = "🆔 Checking ID 🆔")
	sleep(3)
	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Checking Username ⌛️")
	sleep(2)
	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Checking Info ⌛️")
	sleep(3)
	bot.send_message(chat_id = update.message.chat_id , text = "🌐 Connecting to server 🌐")
	sleep(4)
	bot.send_message(chat_id = update.message.chat_id , text = "🌐 Connecting to database 🌐")
	sleep(5)
	if update.message.chat_id == 119940830: #(or update.message.from_user.username == "@SIZATA_SIEGE")
		bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ✅ Admin detected ✅".format(update.message.from_user.first_name , update.message.from_user.last_name))
		bot.send_message(chat_id = update.message.chat_id , text = "✅ Admin detected ✅")
		sleep(2)
		bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Prepairing your panel ⌛️")
		sleep(2)
		bot.send_message(chat_id = update.message.chat_id , text = "❌ ERROR ❌")
	else:
		bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ❌ Not admin ❌".format(update.message.from_user.first_name , update.message.from_user.last_name))
		bot.send_message(chat_id = update.message.chat_id , text = "❌ U R Not admin ! 😐 ❌")

#def my_job_method

def photo_detecter_test (bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "U have sent me a photo")

def text_AI (bot , update):
	#bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
	text = update.message.text
	print(text)
	if "hi" in update.message.text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
	elif "Hi" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
	elif "hello" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hello 👋")
	elif "Hello" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hello 👋")
	elif "slm" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "slm 👋")
	elif "salam" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "salam 👋")
	elif "سلام" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "سلام 👋")
	elif "sghl" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "سلام")

	if "الو" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "جانم ؟")

	if "خوبی" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "سپاسگزارم. شما چطور هستید ؟")
	elif "چطوری" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "عالی. سپاسگزارم. شما چطور هستید ؟")

	if "عالی" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	elif "عالیم" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	elif "خوب" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	elif "خوبم" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	#elif "" in text:
	#	bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")




updater.dispatcher.add_handler(CommandHandler('start' , start_method))
updater.dispatcher.add_handler(CommandHandler('help' , help_method))
updater.dispatcher.add_handler(CommandHandler('bot_progress' , bot_progress_method))
updater.dispatcher.add_handler(CommandHandler('admin' , admin_method))
updater.dispatcher.add_handler(CommandHandler('chat_id' , chat_id_method))
#updater.dispatcher.add_handler(CommandHandler('my_job' , my_job_method))
#updater.dispatcher.add_handler(CommandHandler('send_activity' , send_activity_method))
#updater.dispatcher.add_handler(CommandHandler('send_project' , send_project_method))
updater.dispatcher.add_handler(MessageHandler(Filters.photo , photo_detecter_test))
updater.dispatcher.add_handler(MessageHandler(Filters.text , text_AI))


#func (start , start)
updater.start_polling()

updater.idle()