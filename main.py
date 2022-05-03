import telebot
import requests
import os
from telebot import types
from geopy.geocoders import Nominatim

api = os.getenv('api_token')
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Assalomu alaykum <b>{message.from_user.first_name}</b>.\n——————————————————\n├➪ Geolokatsiyangizni yuboring.",parse_mode='html')
	markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
	button = types.KeyboardButton('🌐 Location',request_location=True)
	markup.add(button)
	bot.send_message(message.chat.id, "- Location:", reply_markup=markup)


@bot.message_handler(content_types=['location'])
def location(message):
	try:
		lt = message.location.latitude
		ln = message.location.longitude

		api_key = "711d46548dd90cf800df2d92430740b7"
		lat = str(lt) 
		lon = str(ln)
		r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}").json()

		name = r["name"]
		lat = r["coord"]["lat"]
		lon = r["coord"]["lon"]
		des = r["weather"][0]["description"]
		icon = r["weather"][0]["icon"]
		wm = r["weather"][0]["main"]
		temp = r["main"]["temp"]
		fl = r["main"]["feels_like"]
		t_min = r["main"]["temp_min"]
		t_max = r["main"]["temp_max"]
		ht = r["main"]["humidity"]
		ps = r["main"]["pressure"]
		sd = r["wind"]["speed"]
		t_zone = r["timezone"]
		base = r["base"]
		status = r["cod"]
		text = f"——————————————————\n<b>Name - City:</b> {name}\n<b>Coord:</b>\n├➪ Lat: {lat}\n├➪ Lon: {lon}\n<b>Weather:</b>\n├➪ Description: {des}\n├➪ icon: {icon}\n├➪ main: {wm}\n<b>Base:</b>\n├➪ base:{base}\n<b>Main:</b>\n├➪ temp: {temp}\n├➪ feels_like: {fl}\n├➪ temp_min: {t_min}\n├➪ temp_max: {t_max}\n├➪ pressure: {ps}\n├➪ humidity: {ht}\n<b>Wind:</b>\n├➪ {sd}\n├➪ timezone: {t_zone}\n<b>Status_code</b>\n├➪ code: {status}\n——————————————————\n<i>Thank you for your attention :).</i>"
		bot.send_message(message.chat.id,text,parse_mode='html')
	except:
		bot.send_message(message.chat.id,"ooops :(")
		
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
	button = types.KeyboardButton('🌐 Location',request_location=True)
	markup.add(button)
	bot.send_message(message.chat.id, "- Location tashlang:", reply_markup=markup)

bot.infinity_polling()
