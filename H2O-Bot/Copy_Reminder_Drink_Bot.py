import telebot
import datetime
import random
import time

# Инициализация бота
bot = telebot.TeleBot("7113367263:AAFwxj9CqxD2a-0IXGSIR3qlSztzP0r2eOE")

# Запас воды пользователя в литрах
water_supply = 3

# Установка времени напоминаний
REMINDERS = [
    "09:00",  # Первое напоминание
    "14:00",  # Второе напоминание
    "17:59"   # Третье напоминание
]

# Фразы для мотивационных сообщений
MOTIVATIONS = [
    "Поглоти пару глотков волшебного эликсира и стань супергероем своего дня!",
    "Встряхни шляпу, закуси яблочко и угостись вкусным водопадом энергии! Вода - наш веселый напиток!",
    "Не откладывайте улыбки на завтра - сегодня наполните свой день весельем, попивая воду!"
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет, я чат-бот, который напоминает тебе пить водичку")
    send_reminders(message.chat.id)

# Отправка мотивационного сообщения
def send_motivation_message(chat_id):
    bot.send_message(chat_id, random.choice(MOTIVATIONS))

# Отправка напоминания о питье воды
def send_water_reminder(chat_id):
    global water_supply
    bot.send_message(chat_id, "Не забудьте выпить 250 мл воды сейчас!")
    bot.send_message(chat_id, f"Ваш текущий запас воды: {water_supply} литров.")

# Проверка остатка воды и отправка уведомления при необходимости
def check_water_supply(chat_id):
    global water_supply
    if water_supply < 1:
        bot.send_message(chat_id, "Внимание! Ваш запас воды подходит к концу. Пора купить воды")

# Отправка напоминаний
def send_reminders(chat_id):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in REMINDERS:
            send_water_reminder(chat_id)
            send_motivation_message(chat_id)
            check_water_supply(chat_id)
        time.sleep(60)

# Обработчик команды /drink
@bot.message_handler(commands=['drink'])
def drink_water(message):
    global water_supply
    water_supply -= 0.25  # Предполагаем, что пользователь выпил 250 мл воды
    bot.reply_to(message, "Отлично! Не забывайте пить воду.")

# Запуск бота
bot.polling(none_stop=True)
