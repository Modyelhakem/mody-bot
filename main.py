import telebot
from telebot import types

# --- إعدادات مووودي الحااااڪم ---
API_TOKEN = '8670105321:AAHxD1-RJdhKR4-GXLgzA4S0V69xyMddYcQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_msg = (
        f"⚡️ **أهلاً بيك يا {user_name} في بوت مووودي الحااااڪم** ⚡️\n\n"
        "👑 **أقوى بوت لخدمات الرشق وشحن الألعاب**\n"
        "----------------------------------\n"
        "📱 متاح حالياً رشق (إنستا - تيك توك)\n"
        "🎮 متاح شحن شدات ببجي وجواهر فري فاير\n\n"
        "🚀 اختر ما تحتاجه من الأزرار بالأسفل:"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("🔥 خدمات الرشق", callback_data='boost_list')
    item2 = types.InlineKeyboardButton("🎮 شحن الألعاب", callback_data='games_list')
    item3 = types.InlineKeyboardButton("👤 حسابي", callback_data='my_info')
    item4 = types.InlineKeyboardButton("📞 الدعم الفني", callback_data='support')
    
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'boost_list':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📸 رشق إنستجرام", callback_data='order_inst'))
        markup.add(types.InlineKeyboardButton("🎵 رشق تيك توك", callback_data='order_tiktok'))
        markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data='back_to_main'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="✨ **قسم الرشق العالمي** \nاختار المنصة اللي عايز ترشقها:", reply_markup=markup, parse_mode="Markdown")
    elif call.data == 'back_to_main':
        send_welcome(call.message)

print("--- البوت شغال باسم مووودي الحااااڪم ---")
bot.infinity_polling()
