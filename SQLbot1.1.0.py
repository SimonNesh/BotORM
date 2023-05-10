import time
import telebot
from telebot import types
import sqlite3
import telegram

bot = telebot.TeleBot('6084739146:AAFdG1H7U6nRuaWVYsKAyjgIfJze8vjXm-w')

user_dict = {}

@bot.message_handler(commands=['start'])
def start(message):
    global user_dict
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Africa")
    but2 = types.KeyboardButton("Arabic")
    but3 = types.KeyboardButton("European")
    but4 = types.KeyboardButton("Latam")
    but5 = types.KeyboardButton("GEO 1")
    but6 = types.KeyboardButton("Asia")
    but7 = types.KeyboardButton("OTHER COUNTRIES")
    markup.add(but1, but2, but3, but4, but5, but6, but7)
    bot.send_message(message.from_user.id, 'Привіт! Я бот що збирає інформацію про всі репутаційні питання та проблеми. Тут Ви можете залишити своє звернення до відділу ORM.')
    bot.send_message(message.from_user.id, 'Оберіть регіон із списку', reply_markup=markup)
    user_id = message.chat.id
    print(user_id)
    if user_id not in user_dict:
        user_dict[user_id] = {}

conn = sqlite3.connect('BaseBot1.db', check_same_thread=False)
cur = conn.cursor()

# Сообщение Админу.
def send_notification(chat_id, text):
    #bot = telegram.Bot(token='6084739146:AAFdG1H7U6nRuaWVYsKAyjgIfJze8vjXm-w')
    bot.send_message(chat_id=chat_id, text=text)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Привіт! Я інструкція з користування ormhelpbot. Прочитай, будь ласка, уважно, порядок формування свого звернення до відділу ORM.\n" 
                                            "Для початку роботи з ботом введи команду /start. Після - внеси дані стосовно свого звернення у такому порядку:\n"
                                            "1. Обери регіон\n"
                                            "2. Обери країну\n"
                                            "3. Введи дату виникнення свого питання або загрозливої ситуації щодо репутації брендів клієнтів. Приклад дати - 21.12.2012\n"
                                            "4. Коротко опишіть суть свого питання або загрозливої ситуації щодо репутації брендів клієнтів\n"
                                            "5. Як би ви оцінили рівень загрози репутації брендів клієнтів? Оберіть з чотирьох варіантів нижче\n"
                                            "6. Залиште посилання на веб-ресурс або на скріншот з описом репутаційної проблеми або питання.\n"
                                            "Як зробити посилання на скріншот? Відкрий програму Lightshot на своєму ноутбуці -> Виділи область екрану, яку хочеш надіслати у вигляді скріншоту->Обери зображення хмаринки із стрілкою внизу області скріншоту “Завантажити на prntscr.com”->Дочекайся завантаження->Натисни “Копіювати”->Обери “Вставити” у рядок введення інформації боту->Відправ\n"
                                            "7. Напиши розгорнутий коментар щодо загрози або питання. Не забудь вказати всі важливі деталі.\n"
                                            "Вітаю! Твоя заявка прийнята до опрацювання!\n"
                                            "Якщо у тебе виникли технічні проблеми з ботом або ти знайшов невідповідність, то звернись до @SimonORM в Телеграм.")

print(user_dict)
def db_table_val(user_id, data):
    Name, Date, Region, date_conflict, The_essence_of_the_conflict, Level, Link, Comments = data['Name'], data['Date'], data['Region'], data['date_conflict'], data['The_essence_of_the_conflict'], data['Level'], data['Link'], data['Comments']
    cur.execute('INSERT INTO db_table (Name, Date, Region, date_conflict, The_essence_of_the_conflict, Level, Link, Comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (Name, Date, Region, date_conflict, The_essence_of_the_conflict, Level, Link, Comments))
    conn.commit()

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "/start"):
        bot.register_next_step_handler(message.chat.id, start)
    elif (message.text == "/help"):
        bot.register_next_step_handler(message.chat.id, help)
    #else:
    if(message.text == 'Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA1 = types.KeyboardButton("Angola")
        regA2 = types.KeyboardButton("Benin")
        regA3 = types.KeyboardButton("Cameroon")
        regA4 = types.KeyboardButton("Botswana")
        regA5 = types.KeyboardButton("Burkina Faso")
        regA6 = types.KeyboardButton("Burundi")
        regA7 = types.KeyboardButton("Cabo Verde")
        regA8 = types.KeyboardButton("Cape Verde")
        regA9 = types.KeyboardButton("Central African Republic")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next1 = types.KeyboardButton("➡ 2 сторінка Africa")
        markup.add(regA1, regA2, regA3, regA4, regA5, regA6, regA7, regA8, regA9, back1, next1)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '⬅ Повернутись до Регіону'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("Africa")
        but2 = types.KeyboardButton("Arabic")
        but3 = types.KeyboardButton("European")
        but4 = types.KeyboardButton("Latam")
        but5 = types.KeyboardButton("GEO 1")
        but6 = types.KeyboardButton("Asia")
        but7 = types.KeyboardButton("OTHER COUNTRIES")
        markup.add(but1, but2, but3, but4, but5, but6, but7)
        bot.send_message(message.from_user.id, 'Привіт! Я бот що збирає інформацію про всі репутаційні питання та проблеми. Тут Ви можете залишити своє звернення до відділу ORM.')
        bot.send_message(message.from_user.id, 'Оберіть регіон із списку', reply_markup=markup)

    elif (message.text == '➡ 2 сторінка Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA10 = types.KeyboardButton("Chad")
        regA11 = types.KeyboardButton("Comoros")
        regA12 = types.KeyboardButton("Côte d'Ivoire")
        regA13 = types.KeyboardButton("Democratic Republic Congo")
        regA14 = types.KeyboardButton("Equatorial Guinea")
        regA15 = types.KeyboardButton("Eritrea")
        regA16 = types.KeyboardButton("Eswatini (Swaziland)")
        regA17 = types.KeyboardButton("Ethiopia")
        regA18 = types.KeyboardButton("Gabon")
        back2 = types.KeyboardButton("⬅ 1 сторінку Africa")
        next2 = types.KeyboardButton("➡ 3 сторінка Africa")
        markup.add(regA10, regA11, regA12, regA13, regA14, regA15, regA16, regA17, regA18, back2, next2)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')


    elif (message.text == '⬅ 1 сторінку Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA1 = types.KeyboardButton("Angola")
        regA2 = types.KeyboardButton("Benin")
        regA3 = types.KeyboardButton("Cameroon")
        regA4 = types.KeyboardButton("Botswana")
        regA5 = types.KeyboardButton("Burkina Faso")
        regA6 = types.KeyboardButton("Burundi")
        regA7 = types.KeyboardButton("Cabo Verde")
        regA8 = types.KeyboardButton("Cape Verde")
        regA9 = types.KeyboardButton("Central African Republic")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next1 = types.KeyboardButton("➡ 2 сторінка Africa")
        markup.add(regA1, regA2, regA3, regA4, regA5, regA6, regA7, regA8, regA9, back1, next1)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '➡ 3 сторінка Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA19 = types.KeyboardButton("Gabon")
        regA20 = types.KeyboardButton("Gambia")
        regA21 = types.KeyboardButton("Ghana")
        regA22 = types.KeyboardButton("Guinea")
        regA23 = types.KeyboardButton("Gabon")
        regA24 = types.KeyboardButton("Gambia")
        regA25 = types.KeyboardButton("Ghana")
        regA26 = types.KeyboardButton("Guinea")
        regA27 = types.KeyboardButton("Guinea-Bissau")
        back3 = types.KeyboardButton("⬅ 2 сторінку Africa")
        next3 = types.KeyboardButton("➡ 4 сторінка Africa")
        markup.add(regA19, regA20, regA21, regA22, regA23, regA24, regA25, regA26, regA27, back3, next3)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 2 сторінку Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA10 = types.KeyboardButton("Chad")
        regA11 = types.KeyboardButton("Comoros")
        regA12 = types.KeyboardButton("Côte d'Ivoire")
        regA13 = types.KeyboardButton("Democratic Republic Congo")
        regA14 = types.KeyboardButton("Equatorial Guinea")
        regA15 = types.KeyboardButton("Eritrea")
        regA16 = types.KeyboardButton("Eswatini (Swaziland)")
        regA17 = types.KeyboardButton("Ethiopia")
        regA18 = types.KeyboardButton("Gabon")
        back2 = types.KeyboardButton("⬅ 1 сторінку Africa")
        next2 = types.KeyboardButton("➡ 3 сторінка Africa")
        markup.add(regA10, regA11, regA12, regA13, regA14, regA15, regA16, regA17, regA18, back2, next2)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 4 сторінка Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA28 = types.KeyboardButton("Kenya")
        regA29 = types.KeyboardButton("Lesotho")
        regA30 = types.KeyboardButton("Liberia")
        regA31 = types.KeyboardButton("Madagascar")
        regA32 = types.KeyboardButton("Malawi")
        regA33 = types.KeyboardButton("Mali")
        regA34 = types.KeyboardButton("Mauritius")
        regA35 = types.KeyboardButton("Mayotte")
        regA36 = types.KeyboardButton("Mozambique")
        back4 = types.KeyboardButton("⬅ 3 сторінку Africa")
        next4 = types.KeyboardButton("➡ 5 сторінка Africa")
        markup.add(regA28, regA29, regA30, regA31, regA32, regA33, regA34, regA35, regA36, back4, next4)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == "⬅ 3 сторінку Africa"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA19 = types.KeyboardButton("Gabon")
        regA20 = types.KeyboardButton("Gambia")
        regA21 = types.KeyboardButton("Ghana")
        regA22 = types.KeyboardButton("Guinea")
        regA23 = types.KeyboardButton("Gabon")
        regA24 = types.KeyboardButton("Gambia")
        regA25 = types.KeyboardButton("Ghana")
        regA26 = types.KeyboardButton("Guinea")
        regA27 = types.KeyboardButton("Guinea-Bissau")
        back3 = types.KeyboardButton("⬅ 2 сторінку Africa")
        next3 = types.KeyboardButton("➡ 4 сторінка Africa")
        markup.add(regA19, regA20, regA21, regA22, regA23, regA24, regA25, regA26, regA27, back3, next3)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == "⬅ 4 сторінку Africa"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA28 = types.KeyboardButton("Kenya")
        regA29 = types.KeyboardButton("Lesotho")
        regA30 = types.KeyboardButton("Liberia")
        regA31 = types.KeyboardButton("Madagascar")
        regA32 = types.KeyboardButton("Malawi")
        regA33 = types.KeyboardButton("Mali")
        regA34 = types.KeyboardButton("Mauritius")
        regA35 = types.KeyboardButton("Mayotte")
        regA36 = types.KeyboardButton("Mozambique")
        back4 = types.KeyboardButton("⬅ 3 сторінку Africa")
        next4 = types.KeyboardButton("➡ 5 сторінка Africa")
        markup.add(regA28, regA29, regA30, regA31, regA32, regA33, regA34, regA35, regA36, back4, next4)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 5 сторінка Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA37 = types.KeyboardButton("Namibia")
        regA38 = types.KeyboardButton("Niger")
        regA39 = types.KeyboardButton("Nigeria")
        regA40 = types.KeyboardButton("Republic Congo")
        regA41 = types.KeyboardButton("Reunion")
        regA42 = types.KeyboardButton("Rwanda")
        regA43 = types.KeyboardButton("Sao Tome and Principe")
        regA44 = types.KeyboardButton("Senegal")
        regA45 = types.KeyboardButton("Seychelles")
        back5 = types.KeyboardButton("⬅ 4 сторінку Africa")
        next5 = types.KeyboardButton("➡ 6 сторінка Africa")
        markup.add(regA37, regA38, regA39, regA40, regA41, regA42, regA43, regA44, regA45, back5, next5)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 5 сторінку Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA37 = types.KeyboardButton("Namibia")
        regA38 = types.KeyboardButton("Niger")
        regA39 = types.KeyboardButton("Nigeria")
        regA40 = types.KeyboardButton("Republic Congo")
        regA41 = types.KeyboardButton("Reunion")
        regA42 = types.KeyboardButton("Rwanda")
        regA43 = types.KeyboardButton("Sao Tome and Principe")
        regA44 = types.KeyboardButton("Senegal")
        regA45 = types.KeyboardButton("Seychelles")
        back5 = types.KeyboardButton("⬅ 4 сторінку Africa")
        next5 = types.KeyboardButton("➡ 6 сторінка Africa")
        markup.add(regA37, regA38, regA39, regA40, regA41, regA42, regA43, regA44, regA45, back5, next5)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 6 сторінка Africa'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA46 = types.KeyboardButton("Sierra Leone")
        regA47 = types.KeyboardButton("South Africa")
        regA48 = types.KeyboardButton("Tanzania")
        regA49 = types.KeyboardButton("Togo")
        regA50 = types.KeyboardButton("Uganda")
        regA51 = types.KeyboardButton("Zambia")
        regA52 = types.KeyboardButton("Zimbabwe")
        regA53 = types.KeyboardButton("West Sahara")
        back6 = types.KeyboardButton("⬅ 5 Africa")
        markup.add(regA46, regA47, regA48, regA49, regA50, regA51, regA52, regA53, back6)
        bot.send_message(message.chat.id, text='Африка', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'Arabic'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regB1 = types.KeyboardButton("Afghanistan")
        regB2 = types.KeyboardButton("Algeria")
        regB3 = types.KeyboardButton("Iran")
        regB4 = types.KeyboardButton("Bahrain")
        regB5 = types.KeyboardButton("Comoros Islands")
        regB6 = types.KeyboardButton("Djibouti")
        regB7 = types.KeyboardButton("Egypt ")
        regB8 = types.KeyboardButton("Iraq")
        regB9 = types.KeyboardButton("Jordan")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next7 = types.KeyboardButton("➡ 2 сторінка Arabic")
        markup.add(regB1, regB2, regB3, regB4, regB5, regB6, regB7, regB8, regB9, back1, next7)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '➡ 2 сторінка Arabic'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA10 = types.KeyboardButton("Kuwait")
        regA11 = types.KeyboardButton("Lebanon")
        regA12 = types.KeyboardButton("Libya")
        regA13 = types.KeyboardButton("Mauritania")
        regA14 = types.KeyboardButton("Morocco")
        regA15 = types.KeyboardButton("Oman")
        regA16 = types.KeyboardButton("Palestine")
        regA17 = types.KeyboardButton("Qatar")
        regA18 = types.KeyboardButton("Saudi Arabia")
        back7 = types.KeyboardButton("⬅ 1 сторінку Arabic")
        next8 = types.KeyboardButton("➡ 3 сторінка Arabic")
        markup.add(regA10, regA11, regA12, regA13, regA14, regA15, regA16, regA17, regA18, back7, next8)
        bot.send_message(message.chat.id, text='Arabic', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 3 сторінка Arabic'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA19 = types.KeyboardButton("Somalia")
        regA20 = types.KeyboardButton("Somaliland")
        regA21 = types.KeyboardButton("South Sudan")
        regA22 = types.KeyboardButton("Sudan")
        regA23 = types.KeyboardButton("Syria")
        regA24 = types.KeyboardButton("Tunisia")
        regA25 = types.KeyboardButton("United Arab Emirates")
        regA26 = types.KeyboardButton("Yemen")
        back8 = types.KeyboardButton("⬅ 2 сторінку Arabic")
        markup.add(regA19, regA20, regA21, regA22, regA23, regA24, regA25, regA26, back8)
        bot.send_message(message.chat.id, text='Arabic', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 2 сторінку Arabic'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regA10 = types.KeyboardButton("Kuwait")
        regA11 = types.KeyboardButton("Lebanon")
        regA12 = types.KeyboardButton("Libya")
        regA13 = types.KeyboardButton("Mauritania")
        regA14 = types.KeyboardButton("Morocco")
        regA15 = types.KeyboardButton("Oman")
        regA16 = types.KeyboardButton("Palestine")
        regA17 = types.KeyboardButton("Qatar")
        regA18 = types.KeyboardButton("Saudi Arabia")
        back7 = types.KeyboardButton("⬅ 1 сторінку Arabic")
        next8 = types.KeyboardButton("➡ 3 сторінка Arabic")
        markup.add(regA10, regA11, regA12, regA13, regA14, regA15, regA16, regA17, regA18, back7, next8)
        bot.send_message(message.chat.id, text='Arabic', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 1 сторінку Arabic'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regB1 = types.KeyboardButton("Afghanistan")
        regB2 = types.KeyboardButton("Algeria")
        regB3 = types.KeyboardButton("Iran")
        regB4 = types.KeyboardButton("Bahrain")
        regB5 = types.KeyboardButton("Comoros Islands")
        regB6 = types.KeyboardButton("Djibouti")
        regB7 = types.KeyboardButton("Egypt")
        regB8 = types.KeyboardButton("Iraq")
        regB9 = types.KeyboardButton("Jordan")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next7 = types.KeyboardButton("➡ 2 сторінка Arabic")
        markup.add(regB1, regB2, regB3, regB4, regB5, regB6, regB7, regB8, regB9, back1, next7)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == 'European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regС1 = types.KeyboardButton("Albania")
        regС2 = types.KeyboardButton("Andorra")
        regС3 = types.KeyboardButton("Croatia")
        regС4 = types.KeyboardButton("Austria")
        regС5 = types.KeyboardButton("Belgium")
        regС6 = types.KeyboardButton("Bosnia and Herzegovina")
        regС7 = types.KeyboardButton("Bulgaria")
        regС8 = types.KeyboardButton("Czech Republic")
        regС9 = types.KeyboardButton("Denmark")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next9 = types.KeyboardButton("➡ 2 сторінка European")
        markup.add(regС1, regС2, regС3, regС4, regС5, regС6, regС7, regС8, regС9, back1, next9)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '➡ 2 сторінка European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC10 = types.KeyboardButton("Estonia")
        regC11 = types.KeyboardButton("Finland")
        regC12 = types.KeyboardButton("France")
        regC13 = types.KeyboardButton("Germany")
        regC14 = types.KeyboardButton("Greece")
        regC15 = types.KeyboardButton("Hungary")
        regC16 = types.KeyboardButton("Iceland")
        regC17 = types.KeyboardButton("Ireland")
        regC18 = types.KeyboardButton("Italy")
        back9 = types.KeyboardButton("⬅ 1 сторінку European")
        next10 = types.KeyboardButton("➡ 3 сторінка European")
        markup.add(regC10, regC11, regC12, regC13, regC14, regC15, regC16, regC17, regC18, back9, next10)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 1 сторінку European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regС1 = types.KeyboardButton("Albania")
        regС2 = types.KeyboardButton("Andorra")
        regС3 = types.KeyboardButton("Croatia")
        regС4 = types.KeyboardButton("Austria")
        regС5 = types.KeyboardButton("Belgium")
        regС6 = types.KeyboardButton("Bosnia and Herzegovina")
        regС7 = types.KeyboardButton("Bulgaria")
        regС8 = types.KeyboardButton("Czech Republic")
        regС9 = types.KeyboardButton("Denmark")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next9 = types.KeyboardButton("➡ 2 сторінка European")
        markup.add(regС1, regС2, regС3, regС4, regС5, regС6, regС7, regС8, regС9, back9, next9)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '⬅ 2 сторінку European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC10 = types.KeyboardButton("Estonia")
        regC11 = types.KeyboardButton("Finland")
        regC12 = types.KeyboardButton("France")
        regC13 = types.KeyboardButton("Germany")
        regC14 = types.KeyboardButton("Greece")
        regC15 = types.KeyboardButton("Hungary")
        regC16 = types.KeyboardButton("Iceland")
        regC17 = types.KeyboardButton("Ireland")
        regC18 = types.KeyboardButton("Italy")
        back9 = types.KeyboardButton("⬅ 1 сторінку European")
        next10 = types.KeyboardButton("➡ 3 сторінка European")
        markup.add(regC10, regC11, regC12, regC13, regC14, regC15, regC16, regC17, regC18, back9, next10)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 3 сторінка European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC19 = types.KeyboardButton("Latvia")
        regC20 = types.KeyboardButton("Liechtenstein")
        regC21 = types.KeyboardButton("Lithuania")
        regC22 = types.KeyboardButton("Luxembourg")
        regC23 = types.KeyboardButton("Malta")
        regC24 = types.KeyboardButton("Monaco")
        regC25 = types.KeyboardButton("Montenegro")
        regC26 = types.KeyboardButton("Netherlands")
        regC27 = types.KeyboardButton("North Macedonia")
        back10 = types.KeyboardButton("⬅ 2 сторінку European")
        next11 = types.KeyboardButton("➡ 4 сторінка European")
        markup.add(regC19, regC20, regC21, regC22, regC23, regC24, regC25, regC26, regC27, back10, next11)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 3 сторінку European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC19 = types.KeyboardButton("Latvia")
        regC20 = types.KeyboardButton("Liechtenstein")
        regC21 = types.KeyboardButton("Lithuania")
        regC22 = types.KeyboardButton("Luxembourg")
        regC23 = types.KeyboardButton("Malta")
        regC24 = types.KeyboardButton("Monaco")
        regC25 = types.KeyboardButton("Montenegro")
        regC26 = types.KeyboardButton("Netherlands")
        regC27 = types.KeyboardButton("North Macedonia")
        back10 = types.KeyboardButton("⬅ 2 сторінку European")
        next11 = types.KeyboardButton("➡ 4 сторінка European")
        markup.add(regC19, regC20, regC21, regC22, regC23, regC24, regC25, regC26, regC27, back10, next11)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 4 сторінка European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC28 = types.KeyboardButton("Norway")
        regC29 = types.KeyboardButton("Poland")
        regC30 = types.KeyboardButton("Portugal")
        regC31 = types.KeyboardButton("Romania")
        regC32 = types.KeyboardButton("San Marino")
        regC33 = types.KeyboardButton("Serbia")
        regC34 = types.KeyboardButton("Slovakia")
        regC35 = types.KeyboardButton("Slovenia")
        regC36 = types.KeyboardButton("Spain")
        back11 = types.KeyboardButton("⬅ 3 сторінку European")
        next12 = types.KeyboardButton("➡ 5 сторінка European")
        markup.add(regC28, regC29, regC30, regC31, regC32, regC33, regC34, regC35, regC36, back11, next12)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 4 сторінку European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC28 = types.KeyboardButton("Norway")
        regC29 = types.KeyboardButton("Poland")
        regC30 = types.KeyboardButton("Portugal")
        regC31 = types.KeyboardButton("Romania")
        regC32 = types.KeyboardButton("San Marino")
        regC33 = types.KeyboardButton("Serbia")
        regC34 = types.KeyboardButton("Slovakia")
        regC35 = types.KeyboardButton("Slovenia")
        regC36 = types.KeyboardButton("Spain")
        back11 = types.KeyboardButton("⬅ 3 сторінку European")
        next12 = types.KeyboardButton("➡ 5 сторінка European")
        markup.add(regC28, regC29, regC30, regC31, regC32, regC33, regC34, regC35, regC36, back11, next12)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 5 сторінка European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regC37 = types.KeyboardButton("Sweden")
        regC38 = types.KeyboardButton("Switzerland")
        regC39 = types.KeyboardButton("United Kingdom")
        back12 = types.KeyboardButton("⬅ 4 сторінку European")
        markup.add(regC37, regC38, regC39, back12)
        bot.send_message(message.chat.id, text='European', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'Latam'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD1 = types.KeyboardButton("Argentina")
        regD2 = types.KeyboardButton("Belize")
        regD3 = types.KeyboardButton("Costa Rica")
        regD4 = types.KeyboardButton("Bolivia")
        regD5 = types.KeyboardButton("Brazil")
        regD6 = types.KeyboardButton("Chile")
        regD7 = types.KeyboardButton("Colombia")
        regD8 = types.KeyboardButton("Cuba")
        regD9 = types.KeyboardButton("Dominican Republic")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next13 = types.KeyboardButton("➡ 2 сторінка Latam")
        markup.add(regD1, regD2, regD3, regD4, regD5, regD6, regD7, regD8, regD9, back1, next13)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '➡ 2 сторінка Latam'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD10 = types.KeyboardButton("Ecuador")
        regD11 = types.KeyboardButton("El Salvador")
        regD12 = types.KeyboardButton("French Guiana")
        regD13 = types.KeyboardButton("Guadeloupe")
        regD14 = types.KeyboardButton("Guatemala")
        regD15 = types.KeyboardButton("Guyana")
        regD16 = types.KeyboardButton("Haiti")
        regD17 = types.KeyboardButton("Honduras")
        regD18 = types.KeyboardButton("Martinique")
        back13 = types.KeyboardButton("⬅ 1 сторінку Latam")
        next14 = types.KeyboardButton("➡ 3 сторінка Latam")
        markup.add(regD10, regD11, regD12, regD13, regD14, regD15, regD16, regD17, regD18, back13, next14)
        bot.send_message(message.chat.id, text='Latam', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 1 сторінку Latam'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD1 = types.KeyboardButton("Argentina")
        regD2 = types.KeyboardButton("Belize")
        regD3 = types.KeyboardButton("Costa Rica")
        regD4 = types.KeyboardButton("Bolivia")
        regD5 = types.KeyboardButton("Brazil")
        regD6 = types.KeyboardButton("Chile")
        regD7 = types.KeyboardButton("Colombia")
        regD8 = types.KeyboardButton("Cuba")
        regD9 = types.KeyboardButton("Dominican Republic")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        next13 = types.KeyboardButton("➡ 2 сторінка Latam")
        markup.add(regD1, regD2, regD3, regD4, regD5, regD6, regD7, regD8, regD9, back1, next13)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == '⬅ 2 сторінку Latam'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD10 = types.KeyboardButton("Ecuador")
        regD11 = types.KeyboardButton("El Salvador")
        regD12 = types.KeyboardButton("French Guiana")
        regD13 = types.KeyboardButton("Guadeloupe")
        regD14 = types.KeyboardButton("Guatemala")
        regD15 = types.KeyboardButton("Guyana")
        regD16 = types.KeyboardButton("Haiti")
        regD17 = types.KeyboardButton("Honduras")
        regD18 = types.KeyboardButton("Martinique")
        back13 = types.KeyboardButton("⬅ 1 сторінку Latam")
        next14 = types.KeyboardButton("➡ 3 сторінка Latam")
        markup.add(regD10, regD11, regD12, regD13, regD14, regD15, regD16, regD17, regD18, back13, next14)
        bot.send_message(message.chat.id, text='Latam', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 3 сторінка Latam'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD19 = types.KeyboardButton("Mexico")
        regD20 = types.KeyboardButton("Nicaragua")
        regD21 = types.KeyboardButton("Panama")
        regD22 = types.KeyboardButton("Paraguay")
        regD23 = types.KeyboardButton("Peru")
        regD24 = types.KeyboardButton("Puerto Rico")
        regD25 = types.KeyboardButton("Saint-Barthélemy")
        regD26 = types.KeyboardButton("Saint-Martin")
        regD27 = types.KeyboardButton("Suriname")
        back14 = types.KeyboardButton("⬅ 2 сторінку European")
        next15 = types.KeyboardButton("➡ 4 сторінка European")
        markup.add(regD19, regD20, regD21, regD22, regD23, regD24, regD25, regD26, regD27, back14, next15)
        bot.send_message(message.chat.id, text='Latam', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '⬅ 3 сторінку Latam'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD19 = types.KeyboardButton("Mexico")
        regD20 = types.KeyboardButton("Nicaragua")
        regD21 = types.KeyboardButton("Panama")
        regD22 = types.KeyboardButton("Paraguay")
        regD23 = types.KeyboardButton("Peru")
        regD24 = types.KeyboardButton("Puerto Rico")
        regD25 = types.KeyboardButton("Saint-Barthélemy")
        regD26 = types.KeyboardButton("Saint-Martin")
        regD27 = types.KeyboardButton("Suriname")
        back14 = types.KeyboardButton("⬅ 2 сторінку European")
        next15 = types.KeyboardButton("➡ 4 сторінка European")
        markup.add(regD19, regD20, regD21, regD22, regD23, regD24, regD25, regD26, regD27, back14, next15)
        bot.send_message(message.chat.id, text='Latam', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == '➡ 4 сторінка European'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regD28 = types.KeyboardButton("Uruguay")
        regD29 = types.KeyboardButton("Venezuela")
        back15 = types.KeyboardButton("⬅ 3 сторінку European")
        markup.add(regD28, regD29, back15)
        bot.send_message(message.chat.id, text='Latam', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'GEO 1'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regE1 = types.KeyboardButton("Belarus")
        regE2 = types.KeyboardButton("Georgia")
        regE3 = types.KeyboardButton("Tajikistan")
        regE4 = types.KeyboardButton("Kazakhstan")
        regE5 = types.KeyboardButton("Kyrgyzstan")
        regE6 = types.KeyboardButton("Moldova")
        regE7 = types.KeyboardButton("Russia")
        regE8 = types.KeyboardButton("Turkmenistan")
        regE9 = types.KeyboardButton("Ukraine")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        regE10 = types.KeyboardButton("Uzbekistan")
        markup.add(regE1, regE2, regE3, regE4, regE5, regE6, regE7, regE8, regE9, regE10, back1)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    elif (message.text == 'Asia'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regF1 = types.KeyboardButton("South East Asia Islands")
        regF2 = types.KeyboardButton("South East Asia Continental")
        regF3 = types.KeyboardButton("East Asia")
        regF4 = types.KeyboardButton("South Asia")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        markup.add(regF1, regF2, regF3, regF4, back1)
        bot.send_message(message.chat.id, text='Оберіть регіон Азії із списку', reply_markup=markup)

    elif (message.text == '⬅ Asia'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regF1 = types.KeyboardButton("South East Asia Islands")
        regF2 = types.KeyboardButton("South East Asia Continental")
        regF3 = types.KeyboardButton("East Asia")
        regF4 = types.KeyboardButton("South Asia")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        markup.add(regF1, regF2, regF3, regF4, back1)
        bot.send_message(message.chat.id, text='Оберіть регіон Азії із списку', reply_markup=markup)

    elif (message.text == 'South East Asia Islands'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regG1 = types.KeyboardButton("Brunei")
        regG2 = types.KeyboardButton("Indonesia")
        regG3 = types.KeyboardButton("Laos")
        regG4 = types.KeyboardButton("Malaysia")
        regG5 = types.KeyboardButton("Philipines")
        regG6 = types.KeyboardButton("Singapore")
        back16 = types.KeyboardButton("⬅ Asia")
        markup.add(regG1, regG2, regG3, regG4, regG5, regG6, back16)
        bot.send_message(message.chat.id, text='Asia', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'South East Asia Continental'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regG7 = types.KeyboardButton("Cambodia")
        regG8 = types.KeyboardButton("Myanmar")
        regG9 = types.KeyboardButton("Thailand")
        regG10 = types.KeyboardButton("Vietnam")
        back16 = types.KeyboardButton("⬅ Asia")
        markup.add(regG7, regG8, regG9, regG10, back16)
        bot.send_message(message.chat.id, text='Asia', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'East Asia'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regG11 = types.KeyboardButton("China")
        regG12 = types.KeyboardButton("Hong Kong")
        regG13 = types.KeyboardButton("Japan")
        regG14 = types.KeyboardButton("Macao")
        regG15 = types.KeyboardButton("South Korea")
        regG16 = types.KeyboardButton("Taiwan")
        back16 = types.KeyboardButton("⬅ Asia")
        markup.add(regG11, regG12, regG13, regG14, regG15, regG16, back16)
        bot.send_message(message.chat.id, text='Asia', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'South Asia'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regG17 = types.KeyboardButton("Bangladesh")
        reg18 = types.KeyboardButton("Bhutan")
        regG19 = types.KeyboardButton("Sri Lanka")
        regG20 = types.KeyboardButton("India")
        regG21 = types.KeyboardButton("Maldives")
        regG22 = types.KeyboardButton("Nepal")
        regG23 = types.KeyboardButton("Pakistan")
        back16 = types.KeyboardButton("⬅ Asia")
        markup.add(regG17, reg18, regG19, regG20, regG21, regG22, regG23, back16)
        bot.send_message(message.chat.id, text='Asia', reply_markup=markup)
        bot.send_message(message.chat.id, 'Відповідь Наступні країни')

    elif (message.text == 'OTHER COUNTRIES'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        regH1 = types.KeyboardButton("Australia")
        regH2 = types.KeyboardButton("Canada")
        regH3 = types.KeyboardButton("Mongolia")
        regH4 = types.KeyboardButton("Multi GEO 🌍")
        regH5 = types.KeyboardButton("New Zeland")
        regH6 = types.KeyboardButton("Turkey")
        regH7 = types.KeyboardButton("USA")
        back1 = types.KeyboardButton("⬅ Повернутись до Регіону")
        markup.add(regH1, regH2, regH3, regH5, regH6, regH7, regH4, back1)
        bot.send_message(message.chat.id, text='Оберіть країну із списку', reply_markup=markup)

    if (message.text == "Cameroon"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)
            #if (message.text == str):
            #    bot.register_next_step_handler(message, user_essence)
            #else:
            #    bot.send_message(message.chat.id, 'Помилка!')

    elif (message.text == "Madagascar"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Benin"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mozambique"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Guinea"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Burkina Faso"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Burundi"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Republic Congo"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Democratic Republic Congo"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Côte d'Ivoire"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Senegal"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Togo"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Central African Republic"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Ghana"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Zambia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Kenya"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Liberia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Nigeria"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Sierra Leone"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Uganda"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Ethiopia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Republic of Guinea"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Angola"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Botswana"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Cabo Verde"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Cape Verde"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Chad"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Comoros"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Eritrea"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Gabon"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Gambia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Guinea-Bissau"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Lesotho"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Malawi"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mali"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mauritius"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mayotte"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Namibia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Niger"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Reunion"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Rwanda"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Sao Tome and Principe"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Seychelles"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "South Africa"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Tanzania"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Zimbabwe"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "West Sahara"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Eswatini (Swaziland)"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Afghanistan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Algeria"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Iran"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Bahrain"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Comoros Islands"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Djibouti"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Egypt"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Iraq"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Jordan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Kuwait"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Lebanon"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Libya"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mauritania"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Morocco"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Oman"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Palestine"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Qatar"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Saudi Arabia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Somalia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Somaliland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "South Sudan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Sudan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Syria"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Tunisia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "United Arab Emirates"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Yemen"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Albania"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Andorra"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Croatia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Austria"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Belgium"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Bosnia and Herzegovina"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Bulgaria"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Czech Republic"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Denmark"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Estonia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Finland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "France"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Germany"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Greece"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Hungary"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Iceland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Ireland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Italy"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Latvia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Liechtenstein"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Lithuania"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Luxembourg"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Malta"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Monaco"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Montenegro"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Netherlands"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "North Macedonia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Norway"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Poland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Portugal"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Romania"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "San Marino"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Serbia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        elif (message.text == "/help"):
            bot.register_next_step_handler(message, help)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Slovakia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Slovenia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Spain"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Sweden"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Switzerland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "United Kingdom"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Argentina"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Belize"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Costa Rica"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Bolivia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Brazil"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Chile"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Colombia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Cuba"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Dominican Republic"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Ecuador"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "El Salvador"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "French Guiana"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Guadeloupe"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Guatemala"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Guyana"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Haiti"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Honduras"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Martinique"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mexico"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Nicaragua"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Panama"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Paraguay"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Peru"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Puerto Rico"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Saint-Barthélemy"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Saint-Martin"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Suriname"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Uruguay"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Venezuela"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Belarus"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Georgia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Tajikistan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Kazakhstan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Kyrgyzstan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Moldova"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Russia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Turkmenistan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Ukraine"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Uzbekistan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Brunei"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Indonesia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Laos"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Malaysia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Philipines"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Singapore"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Cambodia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Myanmar"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Thailand"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Vietnam"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "China"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Hong Kong"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Japan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Macao"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "South Korea"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Taiwan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Bangladesh"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Bhutan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Sri Lanka"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "India"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Maldives"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Nepal"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Pakistan"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Australia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Canada"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"')
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Mongolia"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Multi GEO 🌍"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "New Zeland"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "Turkey"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    elif (message.text == "USA"):
        bot.send_message(message.chat.id, 'Введіть дату виникнення запитання або репутаційної проблеми у форматі "ДД.ММ.РРРР"',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        if (message.text == "/start"):
            bot.register_next_step_handler(message, start)
        else:
            bot.register_next_step_handler(message, user_essence)

    tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))
    date = tconv(message.date)
    name = message.from_user.username
    reg = message.text.strip()
    user_id = message.chat.id
    print(user_id)

    if user_id not in user_dict:
        user_dict[user_id] = {}
    user_dict[user_id]['Name'] = name
    user_dict[user_id]['Date'] = date
    user_dict[user_id]['Region'] = reg
    print(user_dict)

def user_essence(message):
    d_conflict = message.text.strip()
    if (message.text == "/start"):
        bot.register_next_step_handler(message, start)
    elif (message.text == "/help"):
        bot.register_next_step_handler(message, help)
    #elif (message.text == str ):
    else:
        bot.register_next_step_handler(message, user_level)
        bot.send_message(message.chat.id, "Опишіть суть проблеми або питання")
    #else:
    #    bot.send_message(message.from_user.id, 'Помилка! не відповідає формату!')
    #    bot.register_next_step_handler(message, user_essence)


    user_id = message.chat.id
    if user_id not in user_dict:
        user_dict[user_id] = {}
    user_dict[user_id]['date_conflict'] = d_conflict
    print(user_dict)

def user_level(message):
    essence = message.text.strip()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    L1 = types.KeyboardButton("Вкрай небезпечна 🔴")
    L2 = types.KeyboardButton("Небезпечна  🟠")
    L3 = types.KeyboardButton("Потенційно небезпечна 🟡")
    L4 = types.KeyboardButton("Не несе загрози 🟢")
    markup.add(L1, L2)
    markup.add(L3, L4)
    bot.send_message(message.from_user.id, 'Оцініть рівень небезпечності ситуації', reply_markup=markup)
    if (message.text == "/start"):
        bot.register_next_step_handler(message, start)
    elif (message.text == "/help"):
        bot.register_next_step_handler(message, help)
    else:
        bot.register_next_step_handler(message, user_link)

    user_id = message.chat.id
    if user_id not in user_dict:
        user_dict[user_id] = {}
    user_dict[user_id]['The_essence_of_the_conflict'] = essence
    print("1 - ", user_dict)

def user_link (message, content_types=["text", "photo", "document"]):

    level = message.text.strip()
    bot.send_message(message.chat.id, "Залиште посилання на веб-ресурс або на скріншот з описом репутаційної проблеми або питання",
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    if (message.text == "/start"):
        bot.register_next_step_handler(message, start)
    elif (message.text == "/help"):
        bot.register_next_step_handler(message, help)
    #elif (message.text != str):
    #    bot.send_message(message, 'Помилка! не відповідає формату!')
    else:
        bot.register_next_step_handler(message, user_comments)

    user_id = message.chat.id
    if user_id not in user_dict:
        user_dict[user_id] = {}
    user_dict[user_id]['Level'] = level
    print("2 - ", user_dict)

def user_comments (message, content_types=["text", "photo", "document"]):
    link = message.strip()
    bot.send_message(message.chat.id, "Залиште коментар до звернення")
    if (message.text == "/start"):
        bot.register_next_step_handler(message, start)
    elif (message.text == "/help"):
        bot.register_next_step_handler(message, help)
    else:
        bot.register_next_step_handler(message, user_bd_locc)

    user_id = message.chat.id
    if user_id not in user_dict:
        user_dict[user_id] = {}
    user_dict[user_id]['Link'] = link
    print(user_dict)

def user_bd_locc (message):
    if (message.text == "/start"):
        bot.register_next_step_handler(message, start)
    elif (message.text == "/help"):
        bot.register_next_step_handler(message, help)
#    else:
#        bot.register_next_step_handler(message, start)
    bot.send_message(message.chat.id, 'Дякую! Ваше звернення зафіксовано. Ми повернемось до вас після його опрацювання.')
    comments = message.text.strip()



    user_id = message.chat.id
    if user_id not in user_dict:
        user_dict[user_id] = {}

    user_dict[user_id]['Comments'] = comments
    db_table_val(user_id, user_dict[user_id])
    conn.commit()
    #Сообщение Админу.
    send_notification(chat_id='6219851938', text='Данные были успешно внесены в базу данных')

    print(user_dict)


bot.polling(none_stop=True)