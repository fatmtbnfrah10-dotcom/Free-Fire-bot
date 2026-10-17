import os, requests, telebot
TOKEN = os.getenv("8810621896:AAEog0ILkHP53zCSL8xv4hc0MS4uBSIceV4")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "مرحبا! صيفط UID ديال فري فاير ❤️")

@bot.message_handler(func=lambda m: True)
def send(m):
    uid = m.text.strip()
    if not uid.isdigit():
        return
    bot.reply_to(m, f"⏳ كنصيفط لايكات لـ {uid}...")
    try:
        s = requests.Session()
        s.post("http://38.45.71.17:3001/login", data={"username":"user928501","password":"Lvm910bQbdU"}, timeout=15)
        r = s.post("http://38.45.71.17:3001/api/send_like", json={"uid": uid, "region": "ME"}, timeout=15).json()
        bot.reply_to(m, f"✅ تم بنجاح!\n👤 الاسم: {r.get('nickname')}\n👍 قبل: {r.get('before')}\n🔥 دابا: {r.get('after')}")
    except Exception as e:
        bot.reply_to(m, f"❌ السيرفر طافي دابا: {e}")

bot.infinity_polling()
