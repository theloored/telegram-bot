# استيراد المكتبات
import telebot

# وضع التوكن الذي حصلت عليه من BotFather
TOKEN = "6431945146:AAEqIPeLu0YVJIxZptcjDvBlfld74-3IIYk"

# إنشاء كائن البوت
bot = telebot.TeleBot(TOKEN)

# دالة تعالج أوامر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"مرحبًا {message.from_user.first_name}! أهلاً وسهلاً بك في البوت الخاص بنا.")

# تشغيل البوت بشكل دائم
print("البوت يعمل الآن...")
bot.polling()