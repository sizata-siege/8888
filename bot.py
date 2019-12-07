#IN THE NAME OF GOD

import os
from telegram.ext import Updater , CommandHandler

updater = Updater("919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM")

#def func (message , func):
#	updater.dispatcher.add_handler(CommandHandler('message' , func))
chat_id_var = ""
bot_progress_v = "وضعیت پیشرفت ربات"

def start_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "Hi {} {} 😐. U can use /help to see bot options.".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message)
	print (update.message.chat_id)#add name later
	#chat_id_var = "User "+update.message.chat_id+"started the bot"#add name in the future
	bot.send_message(chat_id = "753039129" , text = "{} {} >>> start\n{}\n{}\n".format(update.message.from_user.first_name , update.message.from_user.last_name , update.message.chat_id , update.message.from_user.username))

def help_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "/bot_progress >>> "+bot_progress_v+"\n")
	bot.send_message(chat_id = "753039129" , text = "{} {} >>> help".format(update.message.from_user.first_name , update.message.from_user.last_name))

def bot_progress_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "Bot situation : 1%")
	bot.send_message(chat_id = "753039129" , text = "{} {} >>> bot_progress".format(update.message.from_user.first_name , update.message.from_user.last_name))



updater.dispatcher.add_handler(CommandHandler('start' , start_method))

updater.dispatcher.add_handler(CommandHandler('help' , help_method))

updater.dispatcher.add_handler(CommandHandler('bot_progress' , bot_progress_method))

updater.dispatcher.add_handler(CommandHandler('bot_progress' , bot_progress_method))

updater.dispatcher.add_handler(CommandHandler('bot_progress' , bot_progress_method))

updater.dispatcher.add_handler(CommandHandler('bot_progress' , bot_progress_method))


#func (start , start)
updater.start_polling()

updater.idle()







print ("Hello, World !")
input ("press any key ...")