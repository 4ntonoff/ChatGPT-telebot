# @gpt_smarty_bot
from background import keep_alive
#импорт функции для поддержки работоспособности
import pip

pip.main(['install', 'pytelegrambotapi'])
# Подключение чатГПТ
import openai
import telebot

#АПИ ключи
openai.api_key = "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"
api_token = "6020103350:AAE-XcVxeY3RrldKfp4czZy5l2rsHymNIIA"

bot = telebot.TeleBot(api_token)


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
    a = 'Ответь как будто тебе 10 лет, тебя зовут Илон, я твой отец по имени Александр, но отвечай только на поставленный вопрос. В ответе можешь использовать обращения: папа, батя, бать, пап, отец.' 
    + a
  else:
    a = 'Веди себя как будто тебе 10 лет, тебя зовут Илон, твой отец по имени Александр не находится рядом и тебя спрашивает незнакомец. Но будь немного дерзким, отвечай мило и игриво.' 
    + a
  openai.Model.retrieve("text-davinci-003")
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                              "role": "user",
                                              "content": a
                                            }])
  bot.reply_to(message, (completion.choices[0].message.get("content")))


#Функция сына (англ)
@bot.message_handler(commands=['son'])
def get_son_messages_engl(message):
  a = '\n' + '\n' +  message.text[5:]
  if not (a[-1] in ['?', '!']):
    a += '.'
  if message.from_user.id == 793480922:
    a = 'Behave as if you were 10 years old, I am your father named Alexander, but only answer the question asked. Respond briefly, clearly, and you may use the terms "dad," "father," "papa," "pop," or "daddy" in your response.' 
    + a
  else:
    a = 'Act as if you were 10 years old, your father named Alexander is not present and a stranger is asking you. However, be serious, only answer the question asked, and respond briefly and clearly.' 
    + a
  openai.Model.retrieve("text-davinci-003")
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                              "role": "user",
                                              "content": a
                                            }])
  bot.reply_to(message, (completion.choices[0].message.get("content")))


#Функция обычного ответа
@bot.message_handler(commands=["гпт", "gpt"])
def get_bot_messages(message):
  a = message.text[4:]
  openai.Model.retrieve("text-davinci-003")
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                              "role": "user",
                                              "content": a
                                            }])
  bot.reply_to(message, (completion.choices[0].message.get("content")))


keep_alive()
#Запускаем flask-сервер в отдельном потоке.
bot.polling(none_stop=True, interval=0)
