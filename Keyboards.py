from telebot import types

#Main Keyboard
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('🍴Food,Drink, Club🍴')
    mk2 = types.KeyboardButton('🛴Tours🛴')
    mk3 = types.KeyboardButton('🛏Living🛏(in dev)')
    mk4 = types.KeyboardButton('🚍Transport🚍')
    mk5 = types.KeyboardButton('📞SIM-card🌐')
    mk6 = types.KeyboardButton('🛍Shopping🛍(in dev)')
    mk7 = types.KeyboardButton('❓Any Questions❓')
    mk8 = types.KeyboardButton('☑️Donate☑️')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8)

    return markup

# Inside main menu keyboards
def main_food():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('🇺🇦Ukarainian Cusine')
    mk2 = types.KeyboardButton('🥩Steak')
    mk3 = types.KeyboardButton('🍷Local Wine')
    mk4 = types.KeyboardButton('💃Night and Strip Clubs')
    mk5 = types.KeyboardButton("🍺Pub's and Brewaryes")
    mk6 = types.KeyboardButton('🍰Sweet')
    mk7 = types.KeyboardButton('🍸Bar')
    mk8 = types.KeyboardButton('☕️Coffee')
    mk9 = types.KeyboardButton('🧨Just Open')
    mk = types.KeyboardButton('👈Back to Main Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup
def main_tourse():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    mk1 = types.KeyboardButton('🏞Murals')
    mk = types.KeyboardButton('👈Back to Main Menu')
    markup.add(mk1, mk)

    return markup
def main_transport():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('🚇Metro')
    mk2 = types.KeyboardButton('🚖Taxi')
    mk3 = types.KeyboardButton('🚲Bike')
    mk = types.KeyboardButton('👈Back to Main Menu')
    markup.add(mk1, mk2, mk3, mk)

    return markup
def living():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    mk1 = types.KeyboardButton('🏠Apartment')
    mk2 = types.KeyboardButton('🏨Hostel')
    mk = types.KeyboardButton('👈Back to Main Menu')
    markup.add(mk1,mk2, mk)

    return markup



# Keyboards inside FOOD
def food_pub():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('🍻Pivna Duma')
    mk2 = types.KeyboardButton('🍖Kuznya Ribs and Beer')
    mk3 = types.KeyboardButton('😈Varvar Bar')
    mk4 = types.KeyboardButton('👟Sneakers art critic')
    mk5 = types.KeyboardButton('🐟Taranka — Dry Fish & Craft Beer')
    mk6 = types.KeyboardButton('🍺This is BeerBar')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk)

    return markup

def food_bar():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("🍸Handrick's")
    mk2 = types.KeyboardButton("🧉Barman Dictat")
    mk3 = types.KeyboardButton('🧊LoggerHead')
    mk4 = types.KeyboardButton('🍹Beatnik')
    mk5 = types.KeyboardButton('🍸Will be later')
    mk6 = types.KeyboardButton('🧉Talkies')
    mk7 = types.KeyboardButton('🧊Pink Freud')
    mk8 = types.KeyboardButton('🍹PR')
    mk9 = types.KeyboardButton('🧊Sklad')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup

def food_uc():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("✋🏾Last Barricade")
    mk2 = types.KeyboardButton("🛋Kanapa")
    mk3 = types.KeyboardButton("🔰100 years back in future")
    mk4 = types.KeyboardButton("🏰Hetman's fortress")
    mk5 = types.KeyboardButton('🏡Khutorets on the Dnieper')
    mk6 = types.KeyboardButton('🍴Shinok')
    mk7 = types.KeyboardButton('🍛SHO')
    mk8 = types.KeyboardButton('🍽Petrus-ь')
    mk9 = types.KeyboardButton('🦴Kyiv ribs')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup

def uc_sho():
    markup = types.InlineKeyboardMarkup(row_width=3)

    mk1 = types.InlineKeyboardButton('Menu', callback_data='ShoMenu')
    mk2 = types.InlineKeyboardButton('Location', callback_data='ShoLockation')
    mk3 = types.InlineKeyboardButton('FaceBook', url='facebook.com/shoislove')
    mk4 = types.InlineKeyboardButton('More About...', callback_data='ShoMore')

    markup.add(mk1, mk2, mk3, mk4)

    return markup
def uc_last_barricade():
    markup = types.InlineKeyboardMarkup(row_width=3)

    mk1 = types.InlineKeyboardButton('Menu', callback_data='LBMenu')
    mk2 = types.InlineKeyboardButton('Location', callback_data='LBLockation')
    mk3 = types.InlineKeyboardButton('FaceBook', url='facebook.com/ostannya.barykada.kyiv')
    mk4 = types.InlineKeyboardButton('More About...', callback_data='LBMore')

    markup.add(mk1, mk2, mk3, mk4)

    return markup
def uc_years_back_in():
    markup = types.InlineKeyboardMarkup(row_width=3)

    mk1 = types.InlineKeyboardButton('Menu', callback_data='100Menu')
    mk2 = types.InlineKeyboardButton('Location', callback_data='100Lockation')
    mk3 = types.InlineKeyboardButton('FaceBook', url='facebook.com/100rokivtomuvpered/')
    mk4 = types.InlineKeyboardButton('More About...', callback_data='100More')

    markup.add(mk1, mk2, mk3, mk4)

    return markup
def uc_kanapa():
    markup = types.InlineKeyboardMarkup(row_width=3)

    mk1 = types.InlineKeyboardButton('Menu', callback_data='KanapaMenu')
    mk2 = types.InlineKeyboardButton('Location', callback_data='KanapaLockation')
    mk3 = types.InlineKeyboardButton('FaceBook', url='facebook.com/restoransalonKanapa/')
    mk4 = types.InlineKeyboardButton('More About...', callback_data='KanapaMore')

    markup.add(mk1, mk2, mk3, mk4)

    return markup
def uc_hutor():
    markup = types.InlineKeyboardMarkup(row_width=3)

    mk1 = types.InlineKeyboardButton('Menu', callback_data='HutorMenu')
    mk2 = types.InlineKeyboardButton('Location', callback_data='HutorLockation')
    mk3 = types.InlineKeyboardButton('FaceBook', url='facebook.com/hutorets')
    mk4 = types.InlineKeyboardButton('More About...', callback_data='HutorMore')

    markup.add(mk1, mk2, mk3, mk4)

    return markup
def uc_fortress():
    markup = types.InlineKeyboardMarkup(row_width=3)

    mk1 = types.InlineKeyboardButton('Menu', url='fortetsya-hetman.com/eng/restoran/menu/')
    mk2 = types.InlineKeyboardButton('Location', callback_data='FortLockation')
    mk3 = types.InlineKeyboardButton('FaceBook', url='facebook.com/fhetman/')
    mk4 = types.InlineKeyboardButton('More About...', callback_data='FortMore')

    markup.add(mk1, mk2, mk3, mk4)

    return markup



def food_steak():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("🥩Beef: Meet and Wine")
    mk2 = types.KeyboardButton("🍖Argentina Grill")
    mk3 = types.KeyboardButton("🐂Sam`s Steak House")
    mk4 = types.KeyboardButton("🐄SteakHouse")
    mk5 = types.KeyboardButton('🥩Bootlegger')
    mk6 = types.KeyboardButton('🐄T-Bone Prime Beef')
    mk7 = types.KeyboardButton('🐂MeatStorie')
    mk8 = types.KeyboardButton('🍖Tolstiy & Tonkiy')
    mk9 = types.KeyboardButton('🥩Sheep Hunting')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup

def food_wine():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("🥂101 WINE BAR")
    mk2 = types.KeyboardButton("🍷INNOCENT BAR")
    mk3 = types.KeyboardButton("🍇LIKE A LOCAL’S WINE")
    mk4 = types.KeyboardButton("🍷MALEVICH")
    mk5 = types.KeyboardButton('🥂WIN BAR')
    mk6 = types.KeyboardButton('🍇VINSANTO')
    mk7 = types.KeyboardButton('🍇BOTTEGA')
    mk8 = types.KeyboardButton('🍷VINOSTUDIA')
    mk9 = types.KeyboardButton('🥂VIAN')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup

def food_club():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("🥂Queen")
    mk2 = types.KeyboardButton("🍷D.Fleur")
    mk3 = types.KeyboardButton("🍇Ego Party Place")
    mk4 = types.KeyboardButton("🍷Princess Men's Club")
    mk5 = types.KeyboardButton('🥂Caribbean Club')
    mk6 = types.KeyboardButton('🍇SkyBar')
    mk7 = types.KeyboardButton('🍇Penthouse')
    mk8 = types.KeyboardButton('🍷Burlesque')
    mk9 = types.KeyboardButton('🥂Dolls')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup

def food_Dess():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("🧁The Cake")
    mk2 = types.KeyboardButton("🍰Bo.Pastry")
    mk3 = types.KeyboardButton("🎂Kalyna")
    mk4 = types.KeyboardButton("🍮Polverol")
    mk5 = types.KeyboardButton('🍭Milk Bar')
    mk6 = types.KeyboardButton('🍯Honey')
    mk7 = types.KeyboardButton('🍬London: Coffee House')
    mk8 = types.KeyboardButton('🍫Art Eclair')
    mk9 = types.KeyboardButton('🍪Latte: coffee&desserts')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup

def food_coffee():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton("🧁Fandom Coffee Bar")
    mk2 = types.KeyboardButton("🍰Takava Coffee-Buffet")
    mk3 = types.KeyboardButton("🎂RIGHT coffee bar")
    mk4 = types.KeyboardButton("🍮Blur Coffee")
    mk5 = types.KeyboardButton('🍭Yellow Place')
    mk6 = types.KeyboardButton('🍯COFFEE and the CITY')
    mk7 = types.KeyboardButton('🍬Come and Stay')
    mk8 = types.KeyboardButton('🍫Cherry coffee roasters')
    mk9 = types.KeyboardButton('🍪Khlebnyi')
    mk = types.KeyboardButton('👈Back to Food Menu')
    markup.add(mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8, mk9, mk)

    return markup




#Keyboards_inside_TRANSPORT
def transport_metro():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk = types.KeyboardButton('👈Back to Main Menu')

    markup.add(mk)

    return markup


#Keyboards_TOURSE_MURALS
def mural_pres():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 1👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 2👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 3👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_3():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 4👉🏼')
    markup.add(mk1, mk2)

    return markup
def yaroslav_joke():
    markup = types.InlineKeyboardMarkup()

    mk1 = types.InlineKeyboardButton('Where I could see him', callback_data='Yaroslav')

    markup.add(mk1)

    return markup
def mural_4():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 5👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_5():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 6👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_6():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 7👉🏼')
    markup.add(mk1, mk2)

    return markup
def coffe_honey():
    markup = types.InlineKeyboardMarkup()

    mk1 = types.InlineKeyboardButton('More', callback_data='Honey')

    markup.add(mk1)

    return markup
def mural_7():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 8👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_8():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 9👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_9():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 10👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_10():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 11👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_11():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 12👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_12():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 13👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_13():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 14👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_14():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 15👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_15():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 16👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_16():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 17👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_17():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 18👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_18():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 19👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_19():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 20👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_20():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 21👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_21():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 22👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_22():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 23👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_23():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 24👉🏼')
    markup.add(mk1, mk2)

    return markup
def mural_24():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    mk1 = types.KeyboardButton('👈Back to tour selection')
    mk2 = types.KeyboardButton('"Murals": Step 25👉🏼')
    markup.add(mk1, mk2)

    return markup