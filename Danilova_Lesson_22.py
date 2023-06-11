# 6031470236:AAFqUeg1_wOHmlJRER2lQv-lHXk9k1gjm24

import telebot
from telebot import types
token = '6031470236:AAFqUeg1_wOHmlJRER2lQv-lHXk9k1gjm24'
bot = telebot.TeleBot(token)
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    hello = types.InlineKeyboardButton(text='Приветствие', callback_data='1')
    drink_button = types.InlineKeyboardButton(text = 'Хoчу пить!', callback_data = '2')
    eat_btn = types.InlineKeyboardButton(text = 'Хoчу ecть!', callback_data = '3')
    i_want_a_joke = types.InlineKeyboardButton(text = 'Хoчу анекдот!', callback_data = '4')
    i_want_to_sleep = types.InlineKeyboardButton(text = 'Хoчу спать!', callback_data = '5')
    goodbye = types.InlineKeyboardButton(text = 'Прощание с ботом', callback_data = '6')
    keyboard.add(hello,drink_button,eat_btn,i_want_a_joke,i_want_to_sleep,goodbye)
    return keyboard
@bot.message_handler(commands = ['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Приветствую! Выберите, что вы хотите: ', reply_markup = create_keyboard())
@bot.callback_query_handler(func=lambda call:True if call.message else False)
def callback_inline(call):
    if call.data == '1':
        img = 'https://gas-kvas.com/uploads/posts/2023-02/1676713622_gas-kvas-com-p-detskie-risunki-solnishko-s-luchikami-12.png'
        bot.send_photo(call.message.chat.id, photo=img, caption='Доброго времени суток!', reply_markup=create_keyboard())
    if call.data == '2':
        img = 'https://pivobraga.ru/image/cache/data/samogon/zernovie-nabory/6/ge-data-samogon-zernovie-nabory-sm-0-600x600.jpg'
        bot.send_photo(call.message.chat.id, photo=img, caption= 'Картинка воды!', reply_markup=create_keyboard())
    if call.data == '3':
        img = open ('food.png', 'rb')
        bot.send_photo(call.message.chat.id, photo=img, caption='Приятного аппетита!', reply_markup=create_keyboard())
        img.close()
    if call.data == '4':
        img = 'https://webmg.ru/wp-content/uploads/2022/11/i-18-120.jpeg'
        bot.send_photo(call.message.chat.id, photo=img, caption='Желаю повеселиться!', reply_markup=create_keyboard())
    if call.data == '5':
        img = 'https://e7.pngegg.com/pngimages/506/914/png-clipart-sleep-dream-drawing-dream-child-hand.png'
        bot.send_photo(call.message.chat.id, photo=img, caption='Приятных сновидений!', reply_markup=create_keyboard())
    if call.data == '6':
        img = 'https://kartinkived.ru/wp-content/uploads/2021/05/61-7.jpg'
        bot.send_photo(call.message.chat.id, photo=img, caption='До скорой встречи!', reply_markup=create_keyboard())

bot.polling(non_stop=True)





