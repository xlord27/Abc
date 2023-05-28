from telethon import *
import datetime as DT
from telethon import *
import requests,time,os,subprocess,re,sqlite3,sys,random,base64,json,math
import logging
#usr/local/bin/ftvpn
logging.basicConfig(level=logging.INFO)
uptime = DT.datetime.now()

exec(open("ftvpn/var.txt","r").read())
bot = TelegramClient("meme","1356873527","6291068412:AAGrW9atoS0f-ySEdJ9C36gHBT_bxIloeRI").start(bot_token=BOT_TOKEN)
#bot = TelegramClient("memek1","28120399","ea57a2f73ec92724b08f52acaf1f814d").start(bot_token=BOT_TOKEN)
try:
	open("ftvpn/database.db")
except:
	x = sqlite3.connect("ftvpn/database.db")
	c = x.cursor()
	c.execute("CREATE TABLE admin (user_id)")
	c.execute("INSERT INTO admin (user_id) VALUES (?)",(ADMIN,))
	x.commit()

def get_db():
	x = sqlite3.connect("ftvpn/database.db")
	x.row_factory = sqlite3.Row
	return x

def valid(id):
	db = get_db()
	x = db.execute("SELECT user_id FROM admin").fetchall()
	a = [v[0] for v in x]
	if id in a:
		return "true"
	else:
		return "false"
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
