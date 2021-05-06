import telebot
from telebot import types

import config
import text
import data


def kbd_main_language():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_language:
        keyboard.add(btn)
    return keyboard

def kbd_main_russia():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_russia:
        keyboard.add(btn)
    return keyboard

def kbd_main_english():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_english:
        keyboard.add(btn)
    return keyboard

def kbd_main_spain():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_spain:
        keyboard.add(btn)
    return keyboard

def kbd_main_dictionary_r():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_dictionary_r:
        keyboard.add(btn)
    return keyboard

def kbd_main_dictionary_e():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_dictionary_e:
        keyboard.add(btn)
    return keyboard

def kbd_main_dictionary_s():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in data.main_btns_dictionary_s:
        keyboard.add(btn)
    return keyboard





bot = telebot.TeleBot(config.TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, text.start_message, reply_markup=kbd_main_language())



@bot.message_handler(content_types=["text"])
def answer_menu_items(message):
    if message.text == data.main_btns_language[0]:
        bot.send_message(message.chat.id, text.start_message_russia, reply_markup=kbd_main_russia()) 
    
    elif message.text == data.main_btns_language[1]:
        bot.send_message(message.chat.id, text.start_message_english, reply_markup=kbd_main_english())
    
    elif message.text == data.main_btns_language[2]:
        bot.send_message(message.chat.id, text.start_message_spain, reply_markup=kbd_main_spain())  

   
   
    
    elif message.text == data.main_btns_english[0]:
        bot.send_message(message.chat.id, text.about_bot_e)

    elif message.text == data.main_btns_spain[0]:
        bot.send_message(message.chat.id, text.about_bot_s)        
    
    elif message.text == data.main_btns_russia[0]:
        bot.send_message(message.chat.id, text.about_bot_r)

   
   
    
    elif message.text == data.main_btns_russia[2]:
        bot.send_message(message.chat.id, text.start_message_russia, reply_markup=kbd_main_language())     

    elif message.text == data.main_btns_english[2]:
        bot.send_message(message.chat.id, text.start_message_english, reply_markup=kbd_main_language()) 

    elif message.text == data.main_btns_spain[2]:
        bot.send_message(message.chat.id, text.start_message_spain, reply_markup=kbd_main_language())           

   
   
   
    elif message.text == data.main_btns_russia[1]:
        bot.send_message(message.chat.id, text.dictinary_r, reply_markup=kbd_main_dictionary_r())   
    
    elif message.text == data.main_btns_dictionary_r[0]:
        bot.send_message(message.chat.id, text.word_r, reply_markup=kbd_main_russia())

    elif message.text == data.main_btns_dictionary_r[1]:
        bot.send_message(message.chat.id, text.Агриться, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[2]:
        bot.send_message(message.chat.id, text.Анбоксинг, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[3]:
        bot.send_message(message.chat.id, text.Антихайп, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[4]:
        bot.send_message(message.chat.id, text.Апать, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[5]:
        bot.send_message(message.chat.id, text.Байтить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[6]:
        bot.send_message(message.chat.id, text.Баян, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[7]:
        bot.send_message(message.chat.id, text.Бомбит, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[8]:
        bot.send_message(message.chat.id, text.Бро, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[9]:
        bot.send_message(message.chat.id, text.Вайб, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[10]:
        bot.send_message(message.chat.id, text.Гиг, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[11]:
        bot.send_message(message.chat.id, text.Годный, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[12]:
        bot.send_message(message.chat.id, text.Горит, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[13]:
        bot.send_message(message.chat.id, text.Душный, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[14]:
        bot.send_message(message.chat.id, text.Жиза, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[15]:
        bot.send_message(message.chat.id, text.Запилить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[16]:
        bot.send_message(message.chat.id, text.Зашквар, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[17]:
        bot.send_message(message.chat.id, text.Катка, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[18]:
        bot.send_message(message.chat.id, text.Кек, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[19]:
        bot.send_message(message.chat.id, text.Краш, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[20]:
        bot.send_message(message.chat.id, text.Кринж, reply_markup=kbd_main_dictionary_r())  

    elif message.text == data.main_btns_dictionary_r[21]:
        bot.send_message(message.chat.id, text.Крипово, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[22]:
        bot.send_message(message.chat.id, text.Крч, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[23]:
        bot.send_message(message.chat.id, text.Лан, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[24]:
        bot.send_message(message.chat.id, text.Ливнуть, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[25]:
        bot.send_message(message.chat.id, text.Личка, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[26]:
        bot.send_message(message.chat.id, text.Лойс, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[27]:
        bot.send_message(message.chat.id, text.Лол, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[28]:
        bot.send_message(message.chat.id, text.Мерч, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[29]:
        bot.send_message(message.chat.id, text.Мейнстрим, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[30]:
        bot.send_message(message.chat.id, text.Нуб, reply_markup=kbd_main_dictionary_r())  

    elif message.text == data.main_btns_dictionary_r[31]:
        bot.send_message(message.chat.id, text.Панч, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[32]:
        bot.send_message(message.chat.id, text.Пранк, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[33]:
        bot.send_message(message.chat.id, text.Пруф, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[34]:
        bot.send_message(message.chat.id, text.Позер, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[35]:
        bot.send_message(message.chat.id, text.Рофл, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[36]:
        bot.send_message(message.chat.id, text.Скилл, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[37]:
        bot.send_message(message.chat.id, text.Скрин, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[38]:
        bot.send_message(message.chat.id, text.Сорян, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[39]:
        bot.send_message(message.chat.id, text.Троллить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[40]:
        bot.send_message(message.chat.id, text.Топ, reply_markup=kbd_main_dictionary_r())  

    elif message.text == data.main_btns_dictionary_r[41]:
        bot.send_message(message.chat.id, text.Флейм, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[42]:
        bot.send_message(message.chat.id, text.Флексить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[43]:
        bot.send_message(message.chat.id, text.Форсить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[44]:
        bot.send_message(message.chat.id, text.Хайп, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[45]:
        bot.send_message(message.chat.id, text.Хейтить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[46]:
        bot.send_message(message.chat.id, text.Хоуми, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[47]:
        bot.send_message(message.chat.id, text.Чекать, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[48]:
        bot.send_message(message.chat.id, text.Чилить, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[49]:
        bot.send_message(message.chat.id, text.Шмот, reply_markup=kbd_main_dictionary_r())

    elif message.text == data.main_btns_dictionary_r[50]:
        bot.send_message(message.chat.id, text.Эпик, reply_markup=kbd_main_dictionary_r()) 

    elif message.text == data.main_btns_dictionary_r[51]:
        bot.send_message(message.chat.id, text.Юзать, reply_markup=kbd_main_dictionary_r())                                                          



   
   
    
    elif message.text == data.main_btns_english[1]:
        bot.send_message(message.chat.id, text.dictinary_e, reply_markup=kbd_main_dictionary_e())  

    elif message.text == data.main_btns_dictionary_e[0]:
        bot.send_message(message.chat.id, text.word_e, reply_markup=kbd_main_english())

    elif message.text == data.main_btns_dictionary_e[1]:
        bot.send_message(message.chat.id, text.Awesome, reply_markup=kbd_main_dictionary_e()) 

    elif message.text == data.main_btns_dictionary_e[2]:
        bot.send_message(message.chat.id, text.Anti_hype, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[3]:
        bot.send_message(message.chat.id, text.Blinding, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[4]:
        bot.send_message(message.chat.id, text.Bro, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[5]:
        bot.send_message(message.chat.id, text.Bait, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[6]:
        bot.send_message(message.chat.id, text.Cool, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[7]:
        bot.send_message(message.chat.id, text.Cringe, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[8]:
        bot.send_message(message.chat.id, text.Crush, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[9]:
        bot.send_message(message.chat.id, text.Drive_up_the_wall, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[10]:
        bot.send_message(message.chat.id, text.Diss, reply_markup=kbd_main_dictionary_e()) 

    elif message.text == data.main_btns_dictionary_e[11]:
        bot.send_message(message.chat.id, text.dm_s, reply_markup=kbd_main_dictionary_e()) 

    elif message.text == data.main_btns_dictionary_e[12]:
        bot.send_message(message.chat.id, text.Epic_fail, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[13]:
        bot.send_message(message.chat.id, text.Epic, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[14]:
        bot.send_message(message.chat.id, text.Flame, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[15]:
        bot.send_message(message.chat.id, text.Flex, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[16]:
        bot.send_message(message.chat.id, text.Force, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[17]:
        bot.send_message(message.chat.id, text.Gig, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[18]:
        bot.send_message(message.chat.id, text.Hang_out, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[19]:
        bot.send_message(message.chat.id, text.Hype, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[20]:
        bot.send_message(message.chat.id, text.Homie, reply_markup=kbd_main_dictionary_e())  

    elif message.text == data.main_btns_dictionary_e[21]:
        bot.send_message(message.chat.id, text.KEKW, reply_markup=kbd_main_dictionary_e()) 

    elif message.text == data.main_btns_dictionary_e[22]:
        bot.send_message(message.chat.id, text.Like, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[23]:
        bot.send_message(message.chat.id, text.Lol, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[24]:
        bot.send_message(message.chat.id, text.Merch, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[25]:
        bot.send_message(message.chat.id, text.Mate, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[26]:
        bot.send_message(message.chat.id, text.Mainstream, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[27]:
        bot.send_message(message.chat.id, text.Noob, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[28]:
        bot.send_message(message.chat.id, text.Proof, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[29]:
        bot.send_message(message.chat.id, text.Punch, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[30]:
        bot.send_message(message.chat.id, text.Prank, reply_markup=kbd_main_dictionary_e())  

    elif message.text == data.main_btns_dictionary_e[31]:
        bot.send_message(message.chat.id, text.Rofl, reply_markup=kbd_main_dictionary_e()) 

    elif message.text == data.main_btns_dictionary_e[32]:
        bot.send_message(message.chat.id, text.Shade, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[33]:
        bot.send_message(message.chat.id, text.Top, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[34]:
        bot.send_message(message.chat.id, text.Skill, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[35]:
        bot.send_message(message.chat.id, text.Screen, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[36]:
        bot.send_message(message.chat.id, text.Unboxing, reply_markup=kbd_main_dictionary_e())

    elif message.text == data.main_btns_dictionary_e[37]:
        bot.send_message(message.chat.id, text.Vibe, reply_markup=kbd_main_dictionary_e())           





   
   
    elif message.text == data.main_btns_spain[1]:
        bot.send_message(message.chat.id, text.dictinary_s, reply_markup=kbd_main_dictionary_s())    

    elif message.text == data.main_btns_dictionary_s[0]:
        bot.send_message(message.chat.id, text.word_s, reply_markup=kbd_main_spain())   

    elif message.text == data.main_btns_dictionary_s[1]:
        bot.send_message(message.chat.id, text.Tio, reply_markup=kbd_main_dictionary_s()) 

    elif message.text == data.main_btns_dictionary_s[2]:
        bot.send_message(message.chat.id, text.Mola, reply_markup=kbd_main_dictionary_s())

    elif message.text == data.main_btns_dictionary_s[3]:
        bot.send_message(message.chat.id, text.Guay, reply_markup=kbd_main_dictionary_s())

    elif message.text == data.main_btns_dictionary_s[4]:
        bot.send_message(message.chat.id, text.Sin_mas, reply_markup=kbd_main_dictionary_s())     

                











bot.polling()
