import telebot
import requests
from bs4 import BeautifulSoup
import random
from telebot import types
from neiron import send_text_neiron
from neiron import send_design_neiron
from neiron import send_video_neiron
from neiron import send_content_neiron
from neiron import send_productivity_neiron
from neiron import send_business_neiron
from neiron import send_presentations_neiron
from neiron import send_research_neiron

# Установка токена бота
bot = telebot.TeleBot('6292020588:AAGmz8T0z6bL3H0idUVKQEtRSJ8hYLZ_VYo')


# Функция для парсинга новостей
def parse_news_politic():
    url = 'https://ria.ru/politics/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('div', class_="list-item__content")[:5]
    news = ''
    for item in news_list:
        title = item.find('a', class_="list-item__title color-font-hover-only").text
        link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
        news += f'<a href="{link}">{title}</a>\n\n'
    news = news.split("\n\n")
    return news[random.randint(0, 5)]


def parse_news_mir():
    url = 'https://ria.ru/world/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('div', class_="list-item__content")[:5]
    news = ''
    for item in news_list:
        title = item.find('a', class_="list-item__title color-font-hover-only").text
        link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
        news += f'<a href="{link}">{title}</a>\n\n'
    news = news.split("\n\n")
    return news[random.randint(0, 5)]


def parse_news_economy():
    url = 'https://ria.ru/economy/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('div', class_="list-item__content")[:5]
    news = ''
    for item in news_list:
        title = item.find('a', class_="list-item__title color-font-hover-only").text
        link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
        news += f'<a href="{link}">{title}</a>\n\n'
    news = news.split("\n\n")
    return news[random.randint(0, 5)]


def parse_news_society():
    url = 'https://ria.ru/society/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('div', class_="list-item__content")[:5]
    news = ''
    for item in news_list:
        title = item.find('a', class_="list-item__title color-font-hover-only").text
        link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
        news += f'<a href="{link}">{title}</a>\n\n'
    news = news.split("\n\n")
    return news[random.randint(0, 5)]


def parse_news_science():
    url = 'https://ria.ru/science/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('div', class_="list-item__content")[:5]
    news = ''
    for item in news_list:
        title = item.find('a', class_="list-item__title color-font-hover-only").text
        link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
        news += f'<a href="{link}">{title}</a>\n\n'
    news = news.split("\n\n")
    return news[random.randint(0, 5)]


def parse_news_culture():
    url = 'https://ria.ru/culture/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('div', class_="list-item__content")[:5]
    news = ''
    for item in news_list:
        title = item.find('a', class_="list-item__title color-font-hover-only").text
        link = item.find('a', class_="list-item__title color-font-hover-only").get('href')
        news += f'<a href="{link}">{title}</a>\n\n'
    news = news.split("\n\n")
    return news[random.randint(0, 5)]


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Политика")
    btn2 = types.KeyboardButton("Экономика")
    btn3 = types.KeyboardButton("Наука")
    btn5 = types.KeyboardButton("Культура")
    btn6 = types.KeyboardButton("Мировые")
    btn7 = types.KeyboardButton("Общество")
    btn8 = types.KeyboardButton("⭐Полезное")
    markup.add(btn1, btn2, btn3, btn5, btn6, btn7, btn8)
    bot.reply_to(message,
                 f'Привет, {message.from_user.first_name}!\n'
                 f'Я специализированный бот, который может отправлять новости.\n'
                 f'Также я могу скинуть ссылку на интересные нейросети.\n'
                 f'Они могут решить множество задач, такие как:\n'
                 f'1.Создать презентацию.\n'
                 f'2.Помочь тебе создать новый бизнесс и продвинуть твой стартап.\n'
                 f'3.Найти тебе нужную информацию.\n'
                 f'И другие.\n'
                 f'Пожалуйста, выберите категорию новостей, которые хотите увидеть.\n'
                 f'Или нажми на кнопку Полезное, где ты сможешь найти умные нейросети!',
                 reply_markup=markup)


# Обработчик команд
@bot.message_handler(content_types=['text'])
def send_news(message):
    if message.text == "Политика":
        news = parse_news_politic()
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    elif message.text == "Экономика":
        news = parse_news_economy()
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    elif message.text == "Наука":
        news = parse_news_science()
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    elif message.text == "Культура":
        news = parse_news_culture()
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    elif message.text == "Мировые":
        news = parse_news_mir()
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    elif message.text == "Общество":
        news = parse_news_society()
        bot.send_message(message.chat.id, news, parse_mode='HTML')
    elif message.text == "⭐Полезное":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📱Нейросети")
        btn3 = types.KeyboardButton("↩Назад")
        markup.add(btn1, btn3)
        bot.send_message(message.chat.id,
                         'Вы перешли во вкладку Полезное, выберите нужную Вам категорию.',
                         reply_markup=markup)
    elif message.text == "📱Нейросети":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Text")
        btn2 = types.KeyboardButton("Design")
        btn3 = types.KeyboardButton("Video")
        btn4 = types.KeyboardButton("Content")
        btn5 = types.KeyboardButton("Productivity")
        btn6 = types.KeyboardButton("Business")
        btn7 = types.KeyboardButton("Presentations")
        btn8 = types.KeyboardButton("Research")
        btn9 = types.KeyboardButton("↩Назад")
        image = open('image/neiron.jpg', "rb")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, "Выберите тип нейросетей, чтобы получить нужные ссылки", reply_markup=markup)
    elif message.text == "↩Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Политика")
        btn2 = types.KeyboardButton("Экономика")
        btn3 = types.KeyboardButton("Наука")
        btn5 = types.KeyboardButton("Культура")
        btn6 = types.KeyboardButton("Мировые")
        btn7 = types.KeyboardButton("Общество")
        btn8 = types.KeyboardButton("⭐Полезное")
        markup.add(btn1, btn2, btn3, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, "↩Назад", reply_markup=markup)
    elif message.text == "Text":
        text = send_text_neiron()
        bot.send_message(message.chat.id, text)
    elif message.text == "Design":
        design = send_design_neiron()
        bot.send_message(message.chat.id, design)
    elif message.text == "Video":
        video = send_video_neiron()
        bot.send_message(message.chat.id, video)
    elif message.text == "Content":
        content = send_content_neiron()
        bot.send_message(message.chat.id, content)
    elif message.text == "Productivity":
        productivity = send_productivity_neiron()
        bot.send_message(message.chat.id, productivity)
    elif message.text == "Business":
        business = send_business_neiron()
        bot.send_message(message.chat.id, business)
    elif message.text == "Presentations":
        presentations = send_presentations_neiron()
        bot.send_message(message.chat.id, presentations)
    elif message.text == "Research":
        research = send_research_neiron()
        bot.send_message(message.chat.id, research)


# Запуск бота
bot.polling(none_stop=True)
