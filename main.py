import telebot

snoser_bot = "8393047647:AAE9iN6lBsbO5gcaTQ2fX7xQNvrpa4nF1AA"
admin_id = 87560475
bot = telebot.TeleBot(snoser_bot)

ascii_art = """
⣴⡿⠶⠀⠀⠀⣦⣀⣴⠀⠀⠀⠀ ⣴⡿⠶⠀⠀⠀⣦⣀⣴⠀⠀⠀⠀  
⣿⡄⠀⠀⣠⣾⠛⣿⠛⣷⠀⠿⣦ ⣿⡄⠀⠀⣠⣾⠛⣿⠛⣷⠀⠿⣦
⠙⣷⣦⣾⣿⣿⣿⣿⣿⠟⠀⣴⣿ ⠙⣷⣦⣾⣿⣿⣿⣿⣿⠟⠀⣴⣿
⠀⣸⣿⣿⣿⣿⣿⣿⣿⣾⠿⠋⠁  ⣸⣿⣿⣿⣿⣿⣿⣿⣾⠿⠋⠁
⠀⣿⣿⣿⠿⡿⣿⣿⡿⠀⠀⠀⠀ ⠀⣿⣿⣿⠿⡿⣿⣿⡿⠀⠀⠀⠀
⢸⣿⡋⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀ ⢸⣿⡋⠀⠀⠀⢹⣿⡇⠀⠀⠀
⣿⡟⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀ ⣿⡟⠀⠀⠀⠀⠀⢿⡇⠀⠀
"""

@bot.message_handler(commands=['start'])
def start_command(message):
    video = open('onion.mp4', 'rb')
    
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    btn1 = telebot.types.InlineKeyboardButton(text="Ботнет", callback_data='botnet')
    btn2 = telebot.types.InlineKeyboardButton(text="Профиль", callback_data='profile')
    btn3 = telebot.types.InlineKeyboardButton(text="Подписка", callback_data='subscription')
    
    markup.add(btn1, btn2, btn3)
    
    if message.from_user.id == admin_id:
        btn4 = telebot.types.InlineKeyboardButton(text="Админ - панель", callback_data='admin_panel')
        markup.add(btn4)
    
    bot.send_video(message.chat.id, video, caption=f'```{ascii_art}```', parse_mode='Markdown', reply_markup=markup)
    video.close()

import html

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'botnet':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text="Аккаунт", callback_data='no_sub_account')
        btn2 = telebot.types.InlineKeyboardButton(text="Канал", callback_data='no_sub_channel')
        btn3 = telebot.types.InlineKeyboardButton(text="Группа", callback_data='no_sub_group')
        btn4 = telebot.types.InlineKeyboardButton(text="Форум", callback_data='no_sub_forum')
        btn5 = telebot.types.InlineKeyboardButton(text="Сессия", callback_data='no_sub_session')
        btn6 = telebot.types.InlineKeyboardButton(text="Бот", callback_data='no_sub_bot')
        btn7 = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
        
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5, btn6)
        markup.row(btn7)
        
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f'```{ascii_art}```',
            reply_markup=markup,
            parse_mode='Markdown'
        )
    
    elif call.data == 'profile':
        user = call.from_user
        first_name = user.first_name if user.first_name else "Не указан"
        last_name = user.last_name if user.last_name else ""
        full_name = f"{first_name} {last_name}".strip()
        username = f"@{user.username}" if user.username else "Не указан"
        
        full_name_escaped = html.escape(full_name)
        username_escaped = html.escape(username)
        
        profile_text = f"""<b>В вашем профиле собрана вся необходимая информация.</b>

<b>Ник - нейм</b>: <code>{full_name_escaped}</code>
<b>ID</b>: <code>{user.id}</code>
<b>Юзер - нейм</b>: <code>{username_escaped}</code>

<b>Подписка</b>: <code>Не активна</code>
<b>Кол - во дней подписки</b>: <code>0</code>

<b>Успешных</b>: <code>0</code>
<b>Не удачных</b>: <code>0</code>
<b>Всего попыток</b>: <code>0</code>"""
        
        markup = telebot.types.InlineKeyboardMarkup()
        btn_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
        markup.add(btn_back)
        
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=profile_text,
            parse_mode='HTML',
            reply_markup=markup
        )
    
    elif call.data == 'subscription':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text="7 дней", url="https://t.me/send?start=IVuF0HpIaXXu")
        btn2 = telebot.types.InlineKeyboardButton(text="30 дней", url="https://t.me/send?start=IVI53FmncjJz")
        btn3 = telebot.types.InlineKeyboardButton(text="60 дней", url="https://t.me/send?start=IVoeSkLDfpBh")
        btn4 = telebot.types.InlineKeyboardButton(text="120 дней", url="https://t.me/send?start=IVvDkRjHVyTc")
        btn5 = telebot.types.InlineKeyboardButton(text="1 год", url="https://t.me/send?start=IVI53FmncjJz")
        btn6 = telebot.types.InlineKeyboardButton(text="На всегда", url="https://t.me/send?start=IVntCWhUqzm1")
        btn7 = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
        
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5, btn6)
        markup.row(btn7)
        
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f'```{ascii_art}```',
            parse_mode='Markdown',
            reply_markup=markup
        )
        
    elif call.data == 'admin_panel' and call.from_user.id == admin_id:
        pass
    
    elif call.data.startswith('no_sub_'):
        bot.answer_callback_query(call.id, "У вас отсутствует подписка", show_alert=True)
    
    elif call.data == 'back':
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        btn1 = telebot.types.InlineKeyboardButton(text="Ботнет", callback_data='botnet')
        btn2 = telebot.types.InlineKeyboardButton(text="Профиль", callback_data='profile')
        btn3 = telebot.types.InlineKeyboardButton(text="Подписка", callback_data='subscription')
        
        markup.add(btn1, btn2, btn3)
        
        if call.from_user.id == admin_id:
            btn4 = telebot.types.InlineKeyboardButton(text="Админ - панель", callback_data='admin_panel')
            markup.add(btn4)
        
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f'```{ascii_art}```',
            parse_mode='Markdown',
            reply_markup=markup
        )
bot.polling(none_stop=True)
