from telebot import types
import random

import telebot
bot = telebot.TeleBot('1088440063:AAGOhaUT8At4WBVRsgHfYRxZ-5Xll5pV1zA')

first = ["Today is the perfect day for new beginnings.",
         "The optimal day to decide on a bold act!",
         "Be careful, the stars today"
         " may affect your financial condition.",
         "The best time to start"
         " new relationships or deal with old ones.",
         "A fruitful day in order to "
         "deal with the backlog."]
second = ["But remember that even in this case, you must not forget about",
          "If you go out of town, think about",
          "Those who today aim to fulfill "
          "a lot of things to remember about",
          "If you are fatigued, pay attention to",
          "Remember that thoughts are material, which means you"
          " during the day you need to constantly think about"]
second_add = ["relationships with friends and family.",
              "work and business matters, "
              "who can so inappropriately interfere with the plans.",
              "yourself and your health, otherwise to "
              "in the evening, complete discord is possible.",
              "everyday issues - especially those,"
              " which you did not complete yesterday.",
              "rest so as not to turn yourself into"
              " a driven horse at the end of the month."]
third = ["Evil tongues may tell you otherwise"
         " but today you don't need to listen to them.",
         "Know that success favors only the persistent,"
         " therefore, devote this day to the education of the spirit.",
         "Even if you can't lessen the impact"
         " retrograde Mercury, then at least "
         "get things done.",
         "No need to be afraid of lonely meetings - today "
         "the very time when they mean a lot.",
         "If you meet a stranger on the way, be involved.,"
         " and then this meeting will promise you pleasant chores."]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Hi":

        bot.send_message(message.from_user.id,
        "Hi, now I will tell you the horoscope for today.")

        keyboard = types.InlineKeyboardMarkup()

        key_oven = types.InlineKeyboardButton(text='Aries', callback_data='zodiac')

        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Taurus', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Gemini', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Cancer', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Leo', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Virgo', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Libra', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Scorpio', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Sagittarius', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Capricorn', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Aquarius', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Pisces', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Choose your zodiac sign', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Type Hi")
    else:
        bot.send_message(message.from_user.id, "I don’t understand you. Type / help.")
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "zodiac":

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)

        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
