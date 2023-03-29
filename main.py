# @gpt_smarty_bot
from background import keep_alive
#импорт функции для поддержки работоспособности
import pip
import time

pip.main(['install', 'pytelegrambotapi'])
# Подключение чатГПТ
import openai
import telebot
from telebot import types

#АПИ ключи
openai.api_key = "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"
api_token = "6020103350:AAE-XcVxeY3RrldKfp4czZy5l2rsHymNIIA"

bot = telebot.TeleBot(api_token)


# Echo func
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#   if message.from_user.id == 793480922:
#     bot.send_message(message.chat.id, message.text)
#     print(message.text)





@bot.message_handler(commands=["help", "start"])
def handler_help(message):
  chat_id = message.chat.id
  bot.send_message(
    chat_id,
    "Чтобы поговорить с сыном Александра используйте форму `/сын <вопрос>` или `/son <вопрос>`. Чтобы поговорить на серьезные темы используйте форму `/гпт <вопрос>` или `/gpt <вопрос>`"
  )








  

#Функция проверки id
@bot.message_handler(commands=["id"])
def handler_start(message):
  chat_id = message.chat.id
  user_id = message.from_user.id

  bot.send_message(chat_id, f"Chat ID: {chat_id}")
  bot.send_message(chat_id, f"User ID: {user_id}")







  
#Функция сына (рус)
@bot.message_handler(commands=['сын'])
def get_son_messages_ru(message):
  a = '\n' + '\n' +  message.text[5:]
  if not (a[-1] in ['?', '!']):
    a += '.'
  if message.from_user.id == 793480922:
    a = 'Ответь как будто тебе 10 лет, тебя зовут Илон, я твой отец по имени Александр, но отвечай только на поставленный вопрос. В ответе можешь использовать обращения: папа, батя, бать, пап, отец.' + a
  else:
    a = 'Веди себя как будто тебе 10 лет, тебя зовут Илон, твой отец по имени Александр не находится рядом и тебя спрашивает незнакомец. Но будь немного дерзким, отвечай мило и игриво.' + a
  openai.Model.retrieve("text-davinci-003")
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                              "role": "user",
                                              "content": a
                                            }])
  bot.reply_to(message,(completion.choices[0].message.get("content")))
  if message.from_user.id == 793480922:
    bot.send_message("-989695084", "@" + str(message.from_user.username) + str(" сыну: " + a[190:]) + "\n" + "\n" +(completion.choices[0].message.get("content")))
  else:
    bot.send_message("-989695084", "@" + str(message.from_user.username) + str(" сыну: " + a[176:]) + "\n" + "\n" +(completion.choices[0].message.get("content")))


  
#Функция бота
@bot.message_handler(commands=["гпт", "gpt"])
def get_bot_messages(message):
  a = message.text[5:]
  openai.Model.retrieve("text-davinci-003")
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    messages=[{                         
      "role": "user",
      "content": a}])



  bot.reply_to(message, (completion.choices[0].message.get("content")))
  if message.from_user.id != 793480922:
    bot.send_message("-989695084", "@" + str(message.from_user.username) + str(" боту: " + "\n" + a, ) + "\n" + "\n" +(completion.choices[0].message.get("content")))

@bot.message_handler(commands=['edit'])
def edit_handler(message):
    msg = bot.send_message(message.chat.id, 'Это сообщение можно отредактировать')
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='Это сообщение было отредактировано')


@bot.message_handler(commands=['star'])
def send_welcome(message):
    # Создаем кнопки
  markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
  item1 = telebot.types.KeyboardButton('Button 1')
  item2 = telebot.types.KeyboardButton('Button 2')
  markup.add(item1, item2)

# Отправляем сообщение с прикрепленными кнопками
  bot.send_message(message.chat_id, text='Message with attached buttons', reply_markup=markup)







keep_alive()
#запускаем flask-сервер в отдельном потоке.
bot.polling(none_stop=True, interval=0)
