
import telebot
import random
from telebot import types

# بيانات البوت والمطور
TOKEN = '8272738507:AAGbAqceVMqARfiTNRqOb5Y-S-WqvoLzXGc'
DEVELOPER_USERNAME = 'Mody_ggg'
DESIGNER_NAME = 'مودي الحاڪم'

bot = telebot.TeleBot(TOKEN)

# قوائم بيانات غشوائية متطورة
BANKS = ['CIB Egypt', 'National Bank of Egypt', 'Chase Bank', 'Bank of America', 'HSBC', 'Wells Fargo', 'QNB']
COUNTRIES = [
    {'name': 'Egypt 🇪🇬', 'city': 'Cairo', 'zip': '11511', 'phone': '+20'},
    {'name': 'USA 🇺🇸', 'city': 'New York', 'zip': '10001', 'phone': '+1'},
    {'name': 'UK 🇬🇧', 'city': 'London', 'zip': 'E1 6AN', 'phone': '+44'},
    {'name': 'KSA 🇸🇦', 'city': 'Riyadh', 'zip': '11564', 'phone': '+966'},
    {'name': 'Germany 🇩🇪', 'city': 'Berlin', 'zip': '10115', 'phone': '+49'}
]
CARD_LEVELS = ['Classic', 'Gold', 'Platinum', 'Business', 'Signature']
CARD_TYPES = ['Debit', 'Credit', 'Prepaid']

def luhn_generate(bin_num):
    card_numbers = [int(d) for d in str(bin_num) if d.isdigit()]
    while len(card_numbers) < 15:
        card_numbers.append(random.randint(0, 9))
    sum_val = 0
    for i, digit in enumerate(reversed(card_numbers)):
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum_val += digit
    check_digit = (10 - (sum_val % 10)) % 10
    card_numbers.append(check_digit)
    return ''.join(map(str, card_numbers))

@bot.message_handler(commands=['start', 'gen'])
def handle_gen(message):
    text_split = message.text.split()
    bin_to_use = text_split[1] if len(text_split) > 1 else "471644"
    
    # توليد البيانات
    card = luhn_generate(bin_to_use)
    month = str(random.randint(1, 12)).zfill(2)
    year = random.randint(25, 30)
    cvv = str(random.randint(100, 999)).zfill(3)
    pin = random.randint(1000, 9999)
    balance = random.randint(10, 500)
    
    # اختيار الدولة والبيانات المرتبطة بها
    loc = random.choice(COUNTRIES)
    bank = random.choice(BANKS)
    level = random.choice(CARD_LEVELS)
    ctype = random.choice(CARD_TYPES)
    
    # توليد بيانات الاتصال
    email_user = "leon" + str(random.randint(10, 99))
    email = f"{email_user}@gmail.com"
    phone = loc['phone'] + str(random.randint(100000000, 999999999))
    
    # تنسيق الرسالة النهائي (كل الميزات مع بعض)
    caption = (
        f"✅ تم توليد بطاقة فيزا بنجاح!\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"💳 رقم البطاقة: `{card}`\n"
        f"👤 صاحب البطاقة: Leon Langworth\n"
        f"📅 التاريخ: {month}/{year} | 🔒 CVV: `{cvv}`\n"
        f"🔑 الرقم السري (PIN): `{pin}`\n"
        f"💵 الرصيد المتاح: ${balance}\n"
        f"🏦 البنك: {bank} | 🏷️ {level}\n"
        f"💳 النوع: {ctype}\n"
        f"🌍 الدولة: {loc['name']} | 📍 {loc['city']}\n"
        f"📮 الرمز البريدي: `{loc['zip']}`\n"
        f"📧 الإيميل: `{email}`\n"
        f"📞 الهاتف: `{phone}`\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"استمتع بالبطاقة يا حب! 💳\n"
        f"المصمم: {DESIGNER_NAME}"
    )
    
    markup = types.InlineKeyboardMarkup()
    dev_btn = types.InlineKeyboardButton("المطور 👨‍💻", url=f"https://t.me/{DEVELOPER_USERNAME}")
    markup.add(dev_btn)
    
    try:
        bot.reply_to(message, caption, parse_mode='Markdown', reply_markup=markup)
    except Exception as e:
        print(f"Error: {e}")

print("نسخة الـ FULLZ (v4) شغالة يا مودي...")
bot.infinity_polling()
