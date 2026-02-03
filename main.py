import telebot

snoser_bot = "8393047647:AAE9iN6lBsbO5gcaTQ2fX7xQNvrpa4nF1AA"
admin_id = 87560475
bot = telebot.TeleBot(snoser_bot)

ascii_art = """                                                                    ..                          ..                                                                    
                                                                   .:.                          .:.                                                                   
                                                                  .:.                 .-...      .:.                                                                  
                                                                 .::               ..=:--.    .  .:.                                                                  
                                                               ...-. .:.           +*--.      .:  ::...                                                               
                                                              .:..-..::.          =*::.       .-. .-..:                                                               
                                                              .:.:-..-.         .:+-.          ::..-: :.                                                              
                                                              .-.:-..-.          +%*.          :-..-:.-.                                                              
                                                              .::.-::-:         .*#+-.         :-.:-.::.                                                              
                                                             ..:-.:-:--..     .=@@*#=*:.    ...--:-::-::.                                                             
                                                             .-.--.-:-:-:   -@@@%*#*@=+++.   :-:--:.-:.-.                                                             
                                                             .::.:-:::---::@@@+@@@*%*#++++=.:-:-:::-:.-:.                                                             
                                                             ..:-:::-----.@@*@@@@*#*%+-++++-.-----:.:-:..                                                             
                                                              .:.:-:-:---=@+@@##@@*%#*:=====.---:---:.:.                                                              
                                                               .:-:::::--=@+@*%@@#**+*.=====.--:::::-:.                                                               
                                                               ....:--:--.#%#+@@#@#++=:====::-::-::...                                                                
                                                                 ..:::-:::.*##+@#%#+=-----::::--:::..                                                                 
                                                                      ..-:::.++-%*+-.:-:..::::.                                                                       
                                                                       .. ...::::....::::.:. .                                                                        
                                                                             ."""

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
    
    bot.send_video(message.chat.id, video, caption=f'`{ascii_art}`', parse_mode='Markdown', reply_markup=markup)
    video.close()

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'botnet':
        pass
    elif call.data == 'profile':
        pass
    elif call.data == 'subscription':
        pass
    elif call.data == 'admin_panel' and call.from_user.id == admin_id:
        pass

bot.polling(none_stop=True)
