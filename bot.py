import telebot
import Keyboards
import datetime
import AI
import DATA_BASE
from Weather import weather
from random import choice
from Jokes import jokes

bot = telebot.TeleBot('1108154557:AAGUcU7i3ttX60zprFpsMXN_KuNRkxfmkEo')


# ------Хендлер Стартовой кнопки с Главным Меню-------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message('@kyivstat','''Name - {} {}
Username - @{}
Chat ID - {}
Last use - {}'''.format(message.chat.first_name,
                        message.chat.last_name,
                        message.chat.username,
                        str(message.chat.id),
                        datetime.date.today().strftime("%A %d")))
    bot.send_message(message.chat.id,
                     'Hello, {}.\nYou can use menu from below👇\n\nOr ask me what you want, for example:\n-Want to drink wine\n-Where can i eat steak\n-What is Borsch?\n-What s the weather like today\n-Tell me Joke'.format(message.chat.first_name),
                     reply_markup=Keyboards.main_menu())

    #USERS
    DATA_BASE.new_user(message)





# ------Хендлеры Бэковых Кнопок------
@bot.message_handler(regexp='👈Back to Main Menu', content_types=['text'])
def main_menu(message):
    start(message)

@bot.message_handler(regexp='👈Back to Food Menu', content_types=['text'])
def food_menu(message):
    food(message)

@bot.message_handler(regexp='👈Back to tour selection', content_types=['text'])
def tour_menu(message):
    tours(message)



# ---------ХЕНДЛЕРЫ ИНЛАЙНОВЫХ КНОПОК --------
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        #В Туре "Муралы"
        if call.data == "Yaroslav":
            bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIeS179mRm2iKwjz1XFu-XKZPWOWZLpAAL7rTEbrDLoS5ltWRGSQLMMVTiglS4AAwEAAwIAA20AAycLAQABGgQ')
        if call.data == "Honey":
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='''The main advantage of Butney are various author's desserts. For example, After eight, consisting of white chocolate mousse, three types of mint with chocolate ganache and honey, menthol capsules, lemon confit, walnut praline and biscuit, cooked without adding flour. The menu offers many desserts, cakes, sweets, marmalade, more than 15 types of pasta and eclairs with various fillings.
There is also a full menu, which includes first courses, salads, snacks, sandwiches and pies. Marking Vegan will help simplify your choices.
 The desire for originality and exclusivity is read in the choice of tea (cornel, quince, sea-buckthorn with orange fresh) and a coffee card. In addition to traditional options, you will be offered red slightly bitter cocoa, which is added with home-made marshmallows and a unique author's cherry raff.''')


        #SHO
        if call.data == 'ShoMenu':
            bot.send_document(call.message.chat.id,
                              'BQACAgIAAxkBAAIcBF75xbzEBP3qDWWVjQ9Gh-9fn0hxAAKIBwAC0sPRS59Ype-JBuprGgQ')
        if call.data == 'ShoLockation':
            bot.send_location(call.message.chat.id, 50.43748295408461, 30.53481459617615)
            bot.send_message(call.message.chat.id, 'Mechnikova, 18a')
        if call.data == 'ShoMore':
            bot.send_message(call.message.chat.id, '''A two-story restaurant with a giant glass facade and an area of ​​700 square meters. SHO interior can surely be called one of the most instagram in the city. Tables and chairs made of natural wood, tall columns, rough clay walls and ceilings, massive braids of cotton wool and lush bouquets of wildflowers create the atmosphere of a traditional Ukrainian hut-house. Chef Maxim Korzun-Zaretsky (Mercato Italiano in the shopping center) manages the kitchen at SHO Gulliver). He traveled extensively in Ukraine, studying recipes for traditional dishes, and then embodied his knowledge and experience in the menu of the new SHO. It turned out simple, satisfying and tasty.
All products are ordered from farmers. Bake the bread yourself. And not just bread, but according to a recipe 200 years ago. It consists of only water, flour and salt.''')

        #Last Baricade
        if call.data == 'LBMenu':
            bot.send_document(call.message.chat.id,
                            'BQACAgIAAxkBAAIsU18NqE1CdDEAAQaOmu7GaNAr7k4PnwAC3QsAAsaycUj4G3sAATFU6_saBA')
        if call.data == 'LBLockation':
            bot.send_location(call.message.chat.id, 50.4509496850468, 30.522658824920658)
            bot.send_message(call.message.chat.id, 'Maidan Nezalezhnosti, 1')
        if call.data == 'LBMore':
            bot.send_message(call.message.chat.id,
                             '''The Last Barricade is a museum of three modern Ukrainian revolutions.The last Barricade is 100% Ukrainian gastronomy and the first 100% Ukrainian bar. 
Entrance is in the underpass behind a gray door with big white letters. Ask about tour''')

        #100years back in future
        if call.data == '100Menu':
                bot.send_document(call.message.chat.id,
                                  'BQACAgIAAxkBAAIvl18USLN2M0vbE1p9m-FoYPnApX24AAJZBwACY32hSMzmddqcOrS4GgQ')
        if call.data == '100Lockation':
                bot.send_location(call.message.chat.id, 50.457111264046006, 30.51758944988251)
                bot.send_message(call.message.chat.id, 'Desyatinnyi lane, 4')
        if call.data == '100More':
                bot.send_message(call.message.chat.id,
                                 '''This is a kind of Ukrainian gastronomy you’ve never vitnesed before. At least, because it has never been presented from this angle. Could you belive if someone told you Ukrainian food is fresh and healthy? That most dishes fit perfectly with a glass of wine or a fancy cocktail? 100 YEARS BACK IN FUTURE – is not a rebranding of borsch, but a fundamentally new form of Ukrainian cuisine with it’s own superfoods, exotic recipes and newborn traditions with long roots.''')

        #Kanapa
        if call.data == 'KanapaMenu':
                    bot.send_document(call.message.chat.id,
                                      'BQACAgIAAxkBAAIxhl8-MeCGQx-r9Ga9peeI-fiywliuAAIICAACcUP5SfBZbWZlxrxFGwQ')
        if call.data == 'KanapaLockation':
                    bot.send_location(call.message.chat.id, 50.45985024491944, 30.516698956489567)
                    bot.send_message(call.message.chat.id, 'Andriivskyi Uzviz, 19a')
        if call.data == 'KanapaMore':
            bot.send_message(call.message.chat.id,
                                     '''How are we working on the development of new Ukrainian cuisine? We research authentic recipes, apply modern technologies (including techniques inherent in molecular cuisine), choose the best local products and create dishes that give a new gastronomic experience.
Every season we create tasting networks that represent our vision of modern Ukrainian gastronomy.
We dream that as many people in Ukraine and in the world as possible admire Ukrainian culture through amazement and sensual pleasure. We have chosen an extraordinary place for meetings with you: "Kanapa" is located in the legendary part of the city, in a preserved wooden building of the XIX century with a fireplace hall.''')

        #Hutorets
        if call.data == 'HutorMenu':
            bot.send_document(call.message.chat.id,
                              'BQACAgIAAxkBAAIxjl8-NPCYqH33RMTKn6xnEKDc5xg0AAIOCAACcUP5SfqE7mQrz6G1GwQ')
        if call.data == 'HutorLockation':
            bot.send_location(call.message.chat.id, 50.469841740524295, 30.525019168853763)
            bot.send_message(call.message.chat.id, 'Naberezhno-Khreshatytska, 10a')
        if call.data == 'HutorMore':
            bot.send_message(call.message.chat.id,
                             '''This restaurant first appeared on the side of the Dnieper in 1998. Today Khutorok has become more modern and more refined, but has remained sincere and welcoming - truly Ukrainian.
We collected the most delicious dishes from all regions of Ukraine: there was a place for fish of the Dnieper and Black Sea, for the Transcarpathian banosh and Hutsul dishes, as well as for the famous Kiev cake.
Is it possible to imagine Ukrainian cuisine without lard? Here you will find seven types of fat and three types of lard. Do you want a rich Ukrainian borsch? We have five types of it, seven types of dumplings, as well as dishes on the grill and our own smokehouse!
Where is the Ukrainian feast - there can not do without ice vodka. We approached this issue very seriously - created a unique vodka room with more than 80 types of vodka from all over Ukraine! The restaurant also has a wine list, for which we received a glass from Wine Spectator.''')

        #Fortress
        if call.data == 'FortLockation':
                bot.send_location(call.message.chat.id, 50.35570878770902, 30.43443560600281)
                bot.send_message(call.message.chat.id, 'Institutskaya, 103')
        if call.data == 'FortMore':
            bot.send_message(call.message.chat.id,
                            '''"Getman's Fortress" is a historic restaurant and hotel complex located near Kiev on the Kiev-Odessa highway, in the village of Hatnoe.The luxurious interior is made in a castle style - arched vaults and columns, stone and brickwork, massive carved furniture from natural wood, a real fireplace.''')

# ------Хендлеры основного меню------
@bot.message_handler(regexp='🍴Food,Drink, Club🍴', content_types=['text'])
def food(message):
    bot.send_message(message.chat.id,
                     '🍴All restaurant tips are based on the personal experience of the author🍴\n👇Сhoose a category from below👇',
                     reply_markup=Keyboards.main_food())

@bot.message_handler(regexp='🛏Living🛏', content_types=['text'])
def hostels(message):
    bot.send_message(message.chat.id,
                     'For me, when traveling, it is better to live in apartments than in hotels and hostels.\n\nFirst, you can drink at night without disturbing anyone.\n\nSecondly, all the charms of hotels are in apartments, but cheaper',
                     reply_markup=Keyboards.living())

@bot.message_handler(regexp='🛴Tours🛴', content_types=['text'])
def tours(message):
    bot.send_message(message.chat.id, '👇Choose the category below👇', reply_markup=Keyboards.main_tourse())

@bot.message_handler(regexp='🚍Transport🚍', content_types=['text'])
def transport(message):
    bot.send_message(message.chat.id, 'All tips about transport in Kyiv', reply_markup=Keyboards.main_transport())

@bot.message_handler(regexp='❓Any Questions❓', content_types=['text'])
def questions(message):
    bot.send_message(message.chat.id, 'If you have any questions, wishes or suggestions - text me anytime (@SerebrichDima)')

@bot.message_handler(regexp='📞SIM-card🌐', content_types=['text'])
def sim_card(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIwxl89H3wBm5-9B8TAhqaygFukLy4ZAAIirjEbcUPpSXYAAaPgWqv4IE9NEpUuAAMBAAMCAANtAAMkHAMAARsE',
                   '''I think that the best and cheapest package for staying in Ukraine for several days is:
https://shop.lifecell.ua/en/product/lifecell-starter-package-4-unlims/93/169

Price - 60 UAH (2 $)
Internet - 100MB/day
Social networks - Unlim
Video services - Unlim


You can buy at LifeCellShop or in small newspaper shops''')
    bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAIw0F89Ijpf4El1mDwNvTZvIRLEL-MIAAKLBwACcUPpSeNRfytdFyGpGwQ')



#--------Хендлеры FOOD------------
@bot.message_handler(regexp="🍺Pub's and Brewaryes")
def pub(message):
    bot.send_message(message.chat.id,
                     'Pubs and Brewayes👇',
                     reply_markup=Keyboards.food_pub())

@bot.message_handler(regexp='🍸Bar')
def bar(message):
    bot.send_message(message.chat.id,
                     "🍸Bar's👇",
                     reply_markup=Keyboards.food_bar())

@bot.message_handler(regexp='🇺🇦Ukarainian Cusine')
def ukr_cus(message):
    bot.send_message(message.chat.id,
                     "🇺🇦Ukrainian Cusine👇",
                     reply_markup=Keyboards.food_uc())

@bot.message_handler(regexp='🥩Steak')
def steak(message):
    bot.send_message(message.chat.id,
                     "🥩Steak's👇",
                     reply_markup=Keyboards.food_steak())

@bot.message_handler(regexp='🍷Local Wine')
def local_wine(message):
    bot.send_message(message.chat.id,
                     """🍷"from the throat" on a bench in the park is, of course, good. Cheap, cheerful and romantic. But what to do with the onset of cold weather? Correctly! Walk the bars!
Where to look for spiritual places in Kiev with delicious wine and good snacks for it?
All the secrets of Kiev wine from below👇""",
                     reply_markup=Keyboards.food_wine())

@bot.message_handler(regexp='💃Night and Strip Clubs')
def night_club(message):
    bot.send_message(message.chat.id,
                     "💃Night Club's👇",
                     reply_markup=Keyboards.food_club())

@bot.message_handler(regexp='🍰Sweet')
def sweet(message):
    bot.send_message(message.chat.id,
                     "🍰Sweets👇",
                     reply_markup=Keyboards.food_Dess())

@bot.message_handler(regexp='☕️Coffee')
def coffee(message):
    bot.send_message(message.chat.id,
                     "☕️Over the past few years, we have become so spoiled for quality drink that the lack of such in institutions is considered bad manners. The number of coffee houses is growing exponentially, but I will talk about the best of them.👇",
                     reply_markup=Keyboards.food_coffee())

@bot.message_handler(regexp='🧨Just Open')
def justopen(message):
    bot.send_message(message.chat.id,
                     "I add interesting places to this section upon my visit")


#----------Хендлеры FOOD_PUBS-----------
@bot.message_handler(regexp='🍻Pivna Duma', content_types=['text'])
def pivnaduma(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAICmF66Ywh3WorJkBNKUBHUXCimOyR4AAJurTEbthfZSe788N7M-8h4TVLFki4AAwEAAwIAA20AA4nmAQABGQQ',
                   '''The largest craft brewery in Ukraine. Always fresh, light, wheat or dark beer brewed for you.
They brew classic beers according to the author’s recipe under the guidance of respected, and most importantly, 
knowledgeable brewer Sergei Goiko. For special holidays and every 3 months they brew seasonal exclusive beers, 
such as: Amber, Munich, Irish stout, October, Christmas, Amber ale, Golden Belgian ale!
In just 5 years since the opening of the first Beer Duma it was brewed 47 types of beers.

Personal recomendations: IPA beer, Borshch, Khrenovuha shot, Chicken wings

Addresses:
st. Khreshatic 10 (Centr) 098-979-78-78

st. Spasskaya 5 (10 minutes from Centr by walking) 098-002-52-25

st. Dmitriivskaya 2 (10 minutes from centr by taxi) 044 486 17 70

st. Dragomanova 31G (Recomend, first one with brewery inside, 30 minutes from centr by taxi) 063-37-646-73''')

@bot.message_handler(regexp='🍖Kuznya Ribs and Beer', content_types=['text'])
def ribs(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAICll66YwJcOOUZEcSNu7ATJUSSGpgVAAJtrTEbthfZSX4wPBCOG2Id4XvjkS4AAwEAAwIAA20AAzXVAQABGQQ',
                   '''The main dish on the menu is ribs.
Cold-smoked quail, soups and eclairs are also prepared.
The restaurant presents 4 varieties of "Mykulynets barrel beer".

Site: https://www.facebook.com/KuznyaRB/

Address: bul. Tarasa Shevchenka 2

Booking: 067-550-7722''')

@bot.message_handler(regexp='😈Varvar Bar', content_types=['text'])
def varvar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAICkl66Yu8lQGGGW_ccEbxF0kchkUa5AAJqrTEbthfZSbfqCWaYaRi01qaAki4AAwEAAwIAA20AAyZOAQABGQQ',
                   '''One of the best pubs in Ukraine with its own brewery.
Lots of great beers. My personal recommendations:
1. Milk Stout
2. IPA NEMA
3. Pampking Ale

Booking: 067-621-5511

Adress: Saksaganskogo 108/16''')

@bot.message_handler(regexp='👟Sneakers art critic', content_types=['text'])
def sneakers(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIClF66YvpVCg93GMzqA9_pr6iom3-FAAJsrTEbthfZSdDUGRJViPW08jjxkS4AAwEAAwIAA20AA2XNAQABGQQ',
                   '''Here guests can taste various sorts of craft beer from Ukrainian breweries, 
as well as a foamy drink from Belgium, England, the USA, Germany, Italy, Holland, Sweden, and the Baltic countries.
In total, the bar card contains more than one hundred and fifty sorts of beer.
As well as a large selection of whiskey, strong alcohol, wine.
The menu is dominated by popular and original dishes of European and Pan-Asian cooking.
Guests can enjoy snacks, salads, soups, main dishes and desserts.

Personal recomendation:
1. Barbecue pork ribs with kimchi cabbage
2. Calf tongue with Adyghe cheese cream and eggplant tartar
3. "Ban mi" sandwich in a Bao bun with french fries

Addres: st. Basseynaia 2

Booking: 066-277-3288''')

@bot.message_handler(regexp='🐟Taranka — Dry Fish & Craft Beer', content_types=['text'])
def taranka(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAICml66Yw4hUcNYJsNPYQpNoFxHMjJAAAJvrTEbthfZSYGXdpMKII14B7C9ki4AAwEAAwIAA20AA17kAQABGQQ',
                   '''Craft Pub Taranka - a small cozy place with a proposal of domestic craft beer and stockfish.
Available beer varieties and fish species are written out on separate boards.
The menu also includes interesting hutsul snacks, burgers with hot dogs, crayfish and mussels.
Great place for honest beer lovers!

Booking: 050-337-77-80

Address: ul. Balshaya Vasilkovskaya 63''')

@bot.message_handler(regexp='🍺This is BeerBar', content_types=['text'])
def thisisbeerbar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAICkF66Yt-D7OptBU26T9EmAVxPbykDAAJprTEbthfZSQR3EBuHAVRnWRPeky4AAwEAAwIAA20AA7NCAAIZBA',
                   '''It is 4 restaurants in Kiev with more than 100 beers from around the world.
Delicious and nutritious food menu.
Performances of musical groups almost every day.
The most wonderful guests who believed in the dream of beer rock and roll artists and joined the riot.

Addresses:

Centr:
st. Basseynaya 15

Out of centr:
st. Timoshenko 18 (recomendation of author)
st. Trostyianecka 4/2
st. Liskivska 9a/22

Site: https://thisispivbar.ua/

Booking: (044)334-33-33


''')



#--------Хендлеры FOOD_BAR----------
@bot.message_handler(regexp="🍸Handrick's", content_types=['text'])
def handricks(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID7l6-iepeBHICgnsZ-jTJUq0NecpZAAIwrjEbo5f4Sc5b2ax6hCi_MbDvkS4AAwEAAwIAA20AA976AQABGQQ',
                   '''Hendricks bar is also hidden from prying eyes and the bustle of the city, but at the same time it is located 
in the historical center of the city. The "star" team of bartenders, a large selection of cocktails, 
a pleasant interior and a wide variety of spirits are all about Hendricks.
In addition to 40 cocktails, the list of which is constantly updated with new products, you can find “travelers cocktails” from the best bars around the world, 
as well as hearty dishes like tacos, beef tartare, sea bass fillet with cauliflower and much more.

Instagram: @hendricks.bar

Where to find: Bogdan Khmelnitsky, 42''')

@bot.message_handler(regexp='🧉Barman Dictat', content_types=['text'])
def dictat(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID6l6-idvGiruNvTiPdQ5uWs1yVGPpAAIurjEbo5f4SdTDYDAqkoI9nza_ki4AAwEAAwIAA20AA48IAgABGQQ',
                   '''The advantage of BarmenDictat is complete autonomy. It does not depend on the monopoly of alcohol suppliers, the range is striking in variety. Here you can find alcohol unique to our country: the collection has more than 400 items.The history of the institution began with a 13-meter bar counter. There are still no more in Kiev. The five-row alcohol stand is made of metal. Its weight is 4 tons. In the top three rows, not a single bottle is repeated. It is made at an angle. It imitates the tilt of the hand of a man raising a glass. It is convenient for the guest to consider the bottles, this encourages him to try something new.

Instagram: @barmandictat
                   
Where to find: Khreschatyk 44''')

@bot.message_handler(regexp='🧊LoggerHead', content_types=['text'])
def loggerhead(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID4F6-iVsRwZ3-_cR_DVI6pU9Y_ncYAAIprjEbo5f4SV3pam7HXfrWDWBJkS4AAwEAAwIAA20AA0-PAwABGQQ',
                   '''a mysterious institution without a sign in the very center of Kiev. A dark courtyard and an unpretentious iron door, near the door there is a factory switch that serves as a bell. And behind the door - the entrance to the looking glass, into the mysterious basement with brick arched vaults, into the LoggerHead bar. The building where the bar is located previously belonged to Jacob Berner, a well-known Kiev merchant and philanthropist. The creators of the institution have relied on the authenticity of the structure, bar art mixologists and jazz music.

Instagram: @loggerhead.bar

Where to find: blvd. Taras Shevchenko 1''')

@bot.message_handler(regexp='🍹Beatnik', content_types=['text'])
def beatnik(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID3l6-iU1VDukrl4wiYh1hVYRxcvAjAAIorjEbo5f4SavO7fEBx4IU2mbLDgAEAQADAgADbQADDakFAAEZBA',
                   '''The Beatnik concept bar, after closing in Kharkov, moved to the capital, along with the whole team and the idea, to one of the main streets of the city.
The name was chosen for a reason, beatniks are one of the first youth subcultures that arose in the 50-60s in America.
People from the world of literature were bored with the everyday life and the idea of ​​the American dream, but the fun, alcohol and jazz turned out to be much more attractive. 
The creators of the Beatnik bar took this very philosophy.
It will not work to find the bar the first time and it is always under lock and key,
but each guest is met there personally, talking about hipsters and the rules of the establishment.
The room is designed for 40 guests and a comfortable pastime.

Address:   Bolshaya Vasilkovskaya, 23a
Instagram: Instagram: @bar.beatnik
Facebook:  facebook.com/barbeatnik''')

@bot.message_handler(regexp='🍸Will be later', content_types=['text'])
def willbelater(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID7F6-iePrTTb7GO5kTsQ9AZ6EMkOxAAIvrjEbo5f4STJI8frUAYtZQx0Iki4AAwEAAwIAA20AA5FwAQABGQQ',
                   '''The creators of the bar "I'll be later" call it a place where there is something to drink.
The cocktail card of the institution combines both classics, twists and copyrighted works of bartenders.
In addition to drinks, you can find light snacks and coffee.
Since the bar is located in an old building in 1939 near the Bessarabian market, the repairs are made concise, 
with white walls and a minimum of furniture.

Address: Krutoy Spusk, 6/2

Instagram: @budupozhe''')

@bot.message_handler(regexp='🧉Talkies', content_types=['text'])
def talkies(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIELF6-m2Ngz6TXBxKGu7CB4mD1Y2pcAAItrjEbo5f4SZZr83Ym6BAmmPThkS4AAwEAAwIAA20AA1b4AQABGQQ',
                   '''The appearance and internal content of the bar, as the name implies, stand firmly on the stories that Talkies bartenders tell glass by glass. There are no waiters, cooks, administrators and managers in the establishment, and their functions are performed by bartenders, who have recently become partners of the establishment.

Each cocktail tells the story of one of the famous films of the “roaring twenties” period, and the menu is designed as a script with a detailed description of drinks.

Instagram: @ talkies.bar

Where to find: Mezhigorsk, 3/7''')

@bot.message_handler(regexp='🧊Pink Freud', content_types=['text'])
def pinkfreud(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID4l6-iWVzcXHKiJgBFbnTmnpybiVDAAIqrjEbo5f4SXSil-0WPedu4jiFki4AAwEAAwIAA20AA3RuAQABGQQ',
                   '''Freud’s pink graffiti greets visitors at the entrance bar, on Tuesdays in the therapeutic space (as PinkFreud calls the social media bar), a saxophonist will play, Wednesday will receive piano therapy, and a Spanish guitar on Thursday.

Instagram: @pink_freud_kyiv

Where to find: Nizhny Val, 19''')

@bot.message_handler(regexp='🍹PR', content_types=['text'])
def prbar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID5F6-iW6NDt5WEHD9lhg1HubToSvsAAIrrjEbo5f4SZiSNpO45p2vBf_ADgAEAQADAgADbQADxxQGAAEZBA',
                   '''The founder of the bar, Nadia Pereviznyk, worked in the field of PR for many years, but the choice of name was determined not only by this fact. The institution regularly hosts networking meetings and parties where you can find both friends and colleagues in the field. Promoted in the bar Ukrainian producers of alcohol and food.

Instagram: @pr_bar_kyiv

Where to find: Petra Sagaidachnogo, 6a''')

@bot.message_handler(regexp='🧊Sklad', content_types=['text'])
def sklad(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAID_F6-jZhfrwloemBIApMi7Zyr4j7HAAK6rDEbVTn4SURdbWKQHkGZi0LCki4AAwEAAwIAA20AA2UKAgABGQQ',
                   '''They planned to make a full-fledged bar with two floors a warehouse for alcohol, but found a more successful use of such an area. The institution works around the clock, but with a slight amendment: one floor - from 6:00 to 18, and the other - vice versa.

But the features of the institution do not end there. Cocktails on the menu can not be found, only pure alcohol. If you are not strong in various drinks, bartenders will be happy to tell you what to choose depending on taste preferences.

Instagram: @ sklad.bar

Where to find: pl. Bessarabskaya, 2''')


#------------Хендлеры FOOD_UkrCus------------
@bot.message_handler(regexp="✋🏾Last Barricade", content_types=['text'])
def LB(message):
    bot.send_video(message.chat.id,
                   'BAACAgIAAxkBAAIsYl8NycPfrrAC24gDgMez255gwC2HAAIZDAACxrJxSIGtFtMg_mvAGgQ',
                   reply_markup=Keyboards.uc_last_barricade())


@bot.message_handler(regexp="🛋Kanapa", content_types=['text'])
def kanapa(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIEqF6_09W73JnhuYs1PB23VFeQkabbAAJbrjEbVTkAAUpkDFDfOy9eg5ateJEuAAMBAAMCAANtAAOLUwMAARkE',
                   reply_markup=Keyboards.uc_kanapa())


@bot.message_handler(regexp="🔰100 years back in future", content_types=['text'])
def backinfuture(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIEyl6_2d4b1NPV-bFY9tDGxPUJ_MqFAAJnrjEbVTkAAUqwK9skjWFpRFBcyw4ABAEAAwIAA20AA1u0BQABGQQ',
                   reply_markup=Keyboards.uc_years_back_in())


@bot.message_handler(regexp="🏰Hetman's fortress", content_types=['text'])
def hetman(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIy8l9E_XXjsP8xxCRm5Hu2MwABl4u4TQACh64xG78kKUp8O14sO7ZI_P4OBZIuAAMBAAMCAANtAAOWmwUAARsE',
                   reply_markup=Keyboards.uc_fortress())


@bot.message_handler(regexp='🏡Khutorets on the Dnieper', content_types=['text'])
def khutorets(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIErF6_0-OE4jV_vD-hsdge9vSPnk1hAAJdrjEbVTkAAUrBCKSfR7SQJ2hRyw4ABAEAAwIAA20AA521BQABGQQ',
                   reply_markup=Keyboards.uc_hutor())


@bot.message_handler(regexp='🍴Shinok', content_types=['text'])
def shinok(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIErl6_0-ncJXy5uy5PpDaUrJBdBFbTAAJerjEbVTkAAUoaQqc-S1bfXRoAAVGRLgADAQADAgADbQADZ5QDAAEZBA',
                   '''On the Lesya Ukrainka Boulevard there is the Shinok Restaurant and Museum. The interior of the restaurant is decorated in the style of an old Ukrainian village - the whitewashed walls are decorated with kitchen utensils, the hall has massive furniture, and the ceilings are supported by wooden beams. Spinning wheels, pots, rushnyks are placed around the hall as a decor. The menu consists of popular Ukrainian dishes prepared according to home recipes. The bar has a rich selection of homemade tinctures prepared by shinkar.

Where to find - Blvd. Lesia Ukrainka, 28c

Reserve - 067 327 7915''')


@bot.message_handler(regexp='🍛SHO', content_types=['text'])
def sho(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIEsF6_0_B3BN2hrwL4qkUR4-RwbiyxAAJfrjEbVTkAAUrlUsvXcZiQZFT515MuAAMBAAMCAANtAAPnbQACGQQ',
                   reply_markup=Keyboards.uc_sho())


@bot.message_handler(regexp="🍽Petrus-ь", content_types=['text'])
def petrus(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIEol6_08G65MFIcSGJ6x19gsuwS76CAAJYrjEbVTkAAUraINJH7AONRHQe65EuAAMBAAMCAANtAAO_AgIAARkE',
                   '''Fans of Ukrainian cuisine come to us to enjoy the wonderful dishes and the incredible atmosphere, to feel what real hospitality is! We are warm and emotional - like at home! Our guests know that Petrus is one of the best restaurants in Kyiv where you can invite foreign guests to introduce them to the national cuisine. Homemade lard, pickles, 13 types of dumplings made from especially thin dough, potato pancakes, dumplings, dumplings, cabbage rolls, borsch with donuts - having tried all these culinary masterpieces at least once, foreign guests fall in love with Ukraine forever! But for fans of the European menu, we have a huge choice: pork knuckle in Czech; American steaks Ribeye and New York; salads with arugula and veal or tiger prawns; BBQ veal medallions; dorado fillet with vegetables.


Where to find - Esplanade, 28

Reserve - 067 232 69 79''')


@bot.message_handler(regexp='🦴Kyiv ribs', content_types=['text'])
def kyivribs(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIEoF6_07hSuVTr9XWNwOO7AVNjqgn5AAJWrjEbVTkAAUoqR-jmNdborGkIwQ4ABAEAAwIAA20AA9IvBgABGQQ',
                   '''Kyiv Ribs is a restaurant for real gourmets!
Juicy grilled ribs in honey-mustard or honey-ginger sauce - Ukrainian classics!
Traditional dishes in the author's interpretation of the brand chef of the institution conquer and give unforgettable pleasure.
Beer and alcohol cards are famous for their variety and high quality.
The cozy and joyful atmosphere of the restaurant will add a special charm to a friendly meal or a romantic date.

Where to find - Svitla, 3D

Reserve - (066) 113 11 21''')



#------------Хендлеры FOOD_STEAKS------------
@bot.message_handler(regexp="🥩Beef: Meet and Wine", content_types=['text'])
def beef_meat_wine(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFA17ES9DLu8PSSGXj67cav5QIwsg9AAJ_rjEbjGYhSuSW4M2b5wABIff515MuAAMBAAMCAANtAAPejQACGQQ',
                   '''Separately, on our list, I would like to mention one of the best meat restaurants in the capital, whose steaks have long won fans, and the level of service and skill of the chefs are invariably high. In 2010, BEEF: meat & wine was twice awarded the Best Meat Restaurant of Ukraine Award.

The meat is cooked on a Parrilla four-meter open grill and in a wood-fired oven. For steaks, BEEF uses marble meat from the Creekstone Farms organic farm (Kansas, USA).

Where to find - Shota Rustaveli, 11

Reservation - 044 384 2804''')


@bot.message_handler(regexp="🍖Argentina Grill", content_types=['text'])
def argentina_grill(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFAV7ES7PzXtj7OufyplRS3HkDEKF9AAJ-rjEbjGYhSqvG0YYedz8ziQHlkS4AAwEAAwIAA20AA5gdAgABGQQ',
                   '''The meat for Argentinean asadors is not just food, it is a culture that Argentina Grill develops in Ukraine. The kitchens use a josper grill (which serves Spanish cuisine here) and a special parilla grill. Due to the design features of this grill, fat does not drain onto burning coals.

Each of Argentina Grill steaks has special qualities inherent only to it, structure and taste. Bife Angosto - taste-rich meat of wet or dry aging, its uniqueness in a combination of tender and coarser structures. Ojo de Bife is the juiciest marbled beef steak. It is presented on the menu both of Ukrainian origin and from the USA. Entrana is an American meat with a unique incomparable taste, which is difficult to find on the Ukrainian market, but everyone should try it. Complete your dinner with a glass of tart Malbec and you will never forget this taste.

Where to find - Marshal Tymoshenko Street, 18

Reservation - 067 374 2627''')


@bot.message_handler(regexp="🐂Sam`s Steak House", content_types=['text'])
def sam_steak(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFC17ETDY-vsPQi70xNs-Ph_oxxF7vAAKFrjEbjGYhSh8kqOdlqK53RlTLDgAEAQADAgADbQADZNQFAAEZBA',
                   '''In search of steaks, of course, you need to look at the very first steakhouse in Ukraine - Sam`s Steak House. Back in 1996, here the first advanced technology for wet ripening of steaks, bringing it closer to Ukrainian realities. At Sam`s you can also taste world-famous steaks from the American Creekstone Farms.

And you can start exploring American beef steaks from the classic New York, enjoy the famous Porterhouse and Thibone from the meat of an American producer, or evaluate the same positions, but from the meat of a Ukrainian producer.

For each steak, guests can choose a separate sauce, as well as try branded Sam`s drinks (fit for Steaks)! Non-alcoholic Smoky Virgin Mary and Cilanto Virgin Mary cost 140 UAH here, and for those who like a bit stronger, Sam`s offers Smoky Bloody Mary and Cilanto Bloody Mary for 165 UAH.

Sam`s Steak House is a legend among metropolitan steakhouses you should definitely visit!

Where to find - Zhilyanskaya street, 37

Reservation - 044 287 2000''')


@bot.message_handler(regexp="🐄SteakHouse", content_types=['text'])
def steakhouse(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFDV7ETE4RZBYE9hSwmwXLYvKUnI6AAAKGrjEbjGYhSsXdcAAB35l0LRhSxZIuAAMBAAMCAANtAAMOLwIAARkE',
                   '''The Steakhouse restaurant contains all kinds of meat dishes - steaks and loins, kebabs, steaks, grilled chicken and other specialties. Steaks, of course, are central here. There is an open kitchen right in the hall, and different types of farm meat are presented to the guests on the showcase. If desired, the waiter will bring a cart with raw meat to your table, and you can choose your favorite piece.

After this, the cooks cook the selected meat in a josper in the open kitchen. The menu shows the cost per 100 grams. As a result, the price for the weight of the piece chosen by the guest is added to the bill. The meat is served on a wooden board with barbecue sauce and a side dish of vegetables. Local Ukrainian meat is used here, there is a chamber for dry aging and a coal stove. Chefs prepare with a minimum of spices - only salt and black pepper, for complete immersion in all shades of taste of each steak.

Where to find - Vladimirskaya 49A

Reservation - 067 230 6444''')


@bot.message_handler(regexp='🥩Bootlegger', content_types=['text'])
def bootlegger(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFBV7ES-cI61N_nNZgLJ_grNuO3CuBAAKArjEbjGYhSjdOKOHBE-au6Yllky4AAwEAAwIAA20AA3o0AAIZBA',
                   '''Regardless of the time of day or occasion, your mood and style, Bootlegger will always be cordially welcomed and deliciously fed in an atmosphere of coziness and hospitality on the Left Bank of Kiev.

The restaurant presents steaks of American and Ukrainian producers with grilled vegetables, french fries and sauces: pesto, pepper, truffle aioli, Heinz ketchup, cheese, Dutch.

Where to find - Sobornosti Avenue, 5

Reservation - 067 987 5455''')


@bot.message_handler(regexp='🐄T-Bone Prime Beef', content_types=['text'])
def t_bone_prime(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFD17ETGMoXoHyNdGxKTDDAs-NrWOCAAKHrjEbjGYhStomQG6XFFLmbqO6ki4AAwEAAwIAA20AA8M2AgABGQQ',
                   '''Here, in the interior of a real American steakhouse, juicy and tender steaks are prepared for every taste.

For example, a filet mignon steak is prepared from the most valuable and expensive part of the carcass - tenderloin, which is also called tenderloin. Delicacy is the main flavor value of filet mignon. It is taken by those who prefer fatty and rich dishes to a mild flavor and exquisite serving. The meat extract here has the characteristic of Top Choice (21+ days). The meat is cooked in a josper oven, emphasizing the delicate taste of filet mignon with Himalayan salt, pepper, butter and a sprig of rosemary.

T-Bone Prime Beef operates on the principle of a meat-shop-steakhouse. Having tasted the steak ready-made, you can buy chilled meat of any degree of aging and cook a restaurant-level dish at home!
 
Where to find - Knyazhyi Zaton 2/30

Reservation - 044 499 0977''')


@bot.message_handler(regexp='🐂MeatStorie', content_types=['text'])
def meatstorie(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFB17ETAWEvh1W2VaoGWUUbFwVEJrIAAKCrjEbjGYhSk01_uWpOGI-HwPlkS4AAwEAAwIAA20AA7keAgABGQQ',
                   '''Shop-restaurant on Obolon. This place is the crown of the store-restaurant concept. On the ground floor there is a barista shop and counter, on the second floor there is a restaurant where you can enjoy dishes from the chef in a relaxed atmosphere. In addition, the interior design of the institution includes crafting details of masters from all over Ukraine.

The entire meat assortment of meat is of Ukrainian origin. And not the giants of the market, but small farms from different parts of Ukraine. They do not use any additives that improve the appearance, increase weight or extend the shelf life. All meat is chilled and fully complies with current sanitary standards.

Where to find - Heroiv Stalingrada, 8

Reservation - 097 730 7007''')


@bot.message_handler(regexp="🍖Tolstiy & Tonkiy", content_types=['text'])
def tolstiy_tonkiy(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFEV7ETH2B6wXPP7XAODYpQazEFOVIAAKIrjEbjGYhSiCsPGJdHqmJksV-kS4AAwEAAwIAA20AAxp0AwABGQQ',
                   '''Australian beef steaks on a traditional Asian robat grill acquire the same Asian flavor at Tolstiy & Tonkiy!

The menu presents the classic of meat gastronomy - filet mignon and ribeye steaks (120 days of grain fattening). Local food followers can also order steaks from Ukrainian dairy veal and filet mignon from Ukrainian beef.

One has only to choose the desired roast and enjoy rich and juicy meat!

Where to find - Proreznaya, 15a

Reservation - 073 222 3345''')


@bot.message_handler(regexp='🥩Sheep Hunting', content_types=['text'])
def sheep_hunting(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFCV7ETCBn_1Y4dg_YGiL9Lpyq321HAAKErjEbjGYhSuy0D5ukmOn9bJnfky4AAwEAAwIAA20AAzqOAAIZBA',
                   '''Undoubtedly, one of the top Kyiv restaurants. Try to book a table for the evening in a few hours - and you will see
Open kitchen with wooden robata grill, which fry excellent steaks of marble beef and fresh fish
Oxota Na Ovets is an authentic Asian cuisine, legendary recipes from the still mysterious part of the continent: Indonesian soup Tom Yam
and variations of spicy curry, Korean Kim Chi, Chinese Harumaki, smoky cocktails ..
There is also an aquarium with live lobsters and crabs, oyster and caviar bars, a well-thought-out wine list
Unusual breakfasts, large Asian lunches, creative serving and loft-antique interior

Where to find - Vozdvyzhenska 10 B

Booking - 067 406 41 56''')



#------------Хендлеры FOOD_WINE------------
@bot.message_handler(regexp="🥂101 WINE BAR", content_types=['text'])
def winebar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFml7FDnuZ6a0rxIwhS0Y4KwF_mE1VAAIVrjEb6AkoSm8P9BU2IaQ0oaPskS4AAwEAAwIAA20AA-orAgABGQQ',
                   '''Wine bar at Good Wine store. Wine prices here come with a margin of only 10% per bottle from the shelf of Good Wine store. And the number 101 in the name is the number of positions of wine that is poured here in blocks: 101 types of white, red, pink, sparkling, dry, semi-sweet and fortified. All wines are the visiting cards of the world's major wine regions. The kitchen menu is small. Chefs prepare food that goes well with different sorts of wine.

Where to find - Mechnikov, 9

Reservation - 050 400 2257''')


@bot.message_handler(regexp="🍷INNOCENT BAR", content_types=['text'])
def nevinnyi_bar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFol7FD1PJ1HAPxbDyhj6xlG5aueuMAAIZrjEb6AkoSrc5bFi9IAby1APlkS4AAwEAAwIAA20AA5wlAgABGQQ',
                   '''This wine bar operates in the same room as the Chashka coffee shop near the Kinopanorama cinema. In the morning they offer breakfast and a cup of coffee, but from six in the evening a red glass lights up in the window. This means that the bar has started its work and you are ready to pour a vinyl. Although, if you really want to, here you can drink a glass of red dry right in the morning. A variety of snacks are offered here for wine: meat and cheese dishes, brie with dates, figs, cranberries and nuts, ricotta mousse with grissini bread sticks, and hummus with challa.

Where to find - Shota Rustaveli, 15

Reservation - 093 184 8101''')


@bot.message_handler(regexp="🍇LIKE A LOCAL’S WINE", content_types=['text'])
def like_a_local(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFnl7FDv3TBi4M_FHnVimzUweOBNsBAAIXrjEb6AkoSnWCCZg4NpjQMB25ki4AAwEAAwIAA20AAxM6AgABGQQ',
                   '''This wine bar serves only wines from Ukrainian winemakers: Guliyev Wines, Prince Trubetskoy Winery, Kolonist, Grande Vallee, Shabo, Inkerman, Cotnar, Chizay, Bolgrad, Koblevo, French Boulevard, Artemovsk Winery and Swans Land. To blame, the guys offer snacks also only from Ukrainian producers. Here you can try cheese, meat and sausages from small local farms, mincemeat and other spreads, various pies, bruschettas selected for a particular type of wine, as well as grissini and other bread pastries that are made right in the bar.

Where to find - Sichovy Streltsov, 26

Reservation - 063 658 8048''')


@bot.message_handler(regexp="🍷MALEVICH", content_types=['text'])
def malevich(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFoF7FDy0BAkFF5VdX633951rraTvWAAIYrjEb6AkoSs6_f_U7003-EiyCki4AAwEAAwIAA20AA2yeAQABGQQ',
                   '''Another place with local wines. A large selection of Ukrainian wines, which can be ordered as a bottle, or by glass. They offer simple snacks for wine: cheese from small Ukrainian cheese makers, honey, grissini, olives, sun-dried tomatoes.

Where to find - Reytarska, 17

Reservation - 063 699 3056''')


@bot.message_handler(regexp='🥂WIN BAR', content_types=['text'])
def win_bar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFql7FD9tIEpsTryw8bH5e_bLcJBnsAAIfrjEb6AkoStsg_6BmtKVooFDLDgAEAQADAgADbQAD-dQFAAEZBA',
                   '''The menu has a large selection of wines from different regions. The wine list for the establishment, by the way, was compiled by Oleg Kravchenko - the best sommelier of Ukraine in 2011. Wine is served with appetizers - cheese and meat plates, olives, baked artichokes, riyett duck with prunes, baba ganush (mashed baked eggplant). If you want a snack more densely, there are salads, soup of the day and several main dishes.

Where to find - Khoriva, 16/7

Reservation - 050 424 7167''')


@bot.message_handler(regexp='🍇VINSANTO', content_types=['text'])
def vinsanto(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFqF7FD7vqlkZzQVTz0h_8jB3IR7NpAAIerjEb6AkoSrkXv3RQ_R3e-591kS4AAwEAAwIAA20AA2h1AwABGQQ',
                   '''The wine list of this establishment has more than 100 positions. The main emphasis is on Italian wines. However, at the same time here you can find wine and other regions of the world. To the “drink of the gods” here they offer both appetizers and salads, soups, main dishes and desserts - the restaurant has a full menu. Chef sommelier can help here with a choice of wine and the perfect dish.

Where to find - Pushkinskaya, 20

Reservation - 067 977 9776''')


@bot.message_handler(regexp='🍇BOTTEGA', content_types=['text'])
def bottega(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFnF7FDtSxvTMpmvavARhsRGNPaLiSAAIWrjEb6AkoStluw_rObiB88qB1kS4AAwEAAwIAA20AA2N3AwABGQQ',
                   '''And these guys are betting on wines from various regions of Spain. However, in addition to Spanish, you can also find Argentine, Italian, Portuguese, New Zealand and German wine here. The kitchen menu is small. Tapas are offered here - traditional Spanish snacks. In Bottega, tapas are cooked for more than 20 types - on various bases (from bread to artichokes and potatoes) and with various fillings (fish, meat, vegetarian). You can also try several types of paella, salads, fish, seafood and meat here for wine.

Where to find - 13 Tereschenkovskaya

Reservation - 094 823 8574''')


@bot.message_handler(regexp="🍷VINOSTUDIA", content_types=['text'])
def vinostudia(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFpl7FD46F0XVl7bLJyRFByfWLI9ORAAIcrjEb6AkoSm7dTVt-eBk1xa_CDwAEAQADAgADbQADGDUHAAEZBA',
                   '''Australian beef steaks on a traditional Asian robat grill acquire the same Asian flavor at Tolstiy & Tonkiy!

The menu presents the classic of meat gastronomy - filet mignon and ribeye steaks (120 days of grain fattening). Local food followers can also order steaks from Ukrainian dairy veal and filet mignon from Ukrainian beef.

One has only to choose the desired roast and enjoy rich and juicy meat!

Where to find - Proreznaya, 15a

Reservation - 073 222 3345''')


@bot.message_handler(regexp='🥂VIAN', content_types=['text'])
def vian(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIFpF7FD3MQcfiBclEfun4B36XTGC1AAAIbrjEb6AkoSuvC6t4cDZ9pqRp0kS4AAwEAAwIAA20AA7N4AwABGQQ',
                   '''But in this wine bar there is no fixed wine list. Owners are experimenting with assortment, suppliers, manufacturers and countries. Therefore, the availability of wine is constantly changing. However, there are always both classic wines of the New and Old Worlds, as well as unusual little-known wines. There are also many cocktails based on wine, sparkling and port. From food there are only appetizers for wine: olives, meat, cheese, snails, spreads of hummus, paste, cream cheese. There are also sweets and ... herring under a fur coat with olivier.

Where to find - Mikhailovskaya, 21B

Reservation - 050 420 4442''')



#------------Хендлеры FOOD_CLUB------------
@bot.message_handler(regexp="🥂Queen", content_types=['text'])
def queen(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHj17JgzffNPUVW0LWazpgMH-28aqgAAIQrTEbrRJRSi-t6GkkFSjVtWjoki4AAwEAAwIAA20AA0DBAQABGQQ',
                   '''Unique complex with an area of more than 4200 sq.m with
panoramic view of the Dnieper. Includes rooftop (open view terrace), ballroom, spacious restaurant, lounge bar and equipped stage for concert performances and shows.

Where to find - 25 Naberezhnoye Shosse

Reservation - (067) 011-11-15''')


@bot.message_handler(regexp="🍷D.Fleur", content_types=['text'])
def d_fleur(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHhV7JgrsIzZz81KcsnEF6SuKPtp0MAAIKrTEbrRJRSg3ObLFiZZTXaTjxkS4AAwEAAwIAA20AA7NGAgABGQQ',
                   '''This is a unique place in Kiev, confidently combining the light of the neon rays of a modern night club with the stunning comfort of a cozy restaurant. Here everyone will find a place for themselves. On a noisy dance floor under a quality sound of the best DJs, behind a bar with a delicious cocktail in hand. Or sitting on soft sofas in karaoke or relaxing in the lounge area.

Where to find - 3, Grushevskogo

Reservation - (073) 200-90-09''')


@bot.message_handler(regexp="🍇Ego Party Place", content_types=['text'])
def ego_party_place(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHiV7Jgu1wG7xwmZHMWkz102SH__F3AAINrTEbrRJRSl8OxoJ9chISmuZKkS4AAwEAAwIAA20AAxPfAwABGQQ',
                   '''a place of bright parties, pleasant acquaintances and exquisite dishes in the heart of Kiev.

Where to find - Fyodorogo, 4

Reservation - 094 667 7070''')


@bot.message_handler(regexp="🍷Princess Men's Club", content_types=['text'])
def princess(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHjV7Jgx9TCfPeAUzzVMIBMjoydzgNAAIPrTEbrRJRSm78cx5g3Vsjf6K6ki4AAwEAAwIAA20AA7ZeAgABGQQ',
                   '''Princess Men’s Club is the epitome of erotic theater in a new, more modern format, where girls for every taste perform before sophisticated guests. To escape from hard working days, enjoy the beauty of female silhouettes, relax and satisfy your desires - all this is possible in the strip club Princess Men’s Club, because the atmosphere of the holiday reigns here

Where to find - st. Khreshchatyk 14

Reservation - 066 525 6004''')


@bot.message_handler(regexp='🥂Caribbean Club', content_types=['text'])
def caribbean(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHgV7JgoW0xfXZEskYUeGZVEYKq0FjAAIIrTEbrRJRSjPIUQABDgyfxHbh5pIuAAMBAAMCAANtAAMnvwEAARkE',
                   '''This is a cult place in Kiev, where the chic of the West and the fiery Latin rhythms are merged. The most amazing shows, exciting energy and the best musical performances in Kiev. For almost 20 years, the club remains one of the most popular places in the capital. Working seven days a week, the Caribbean Club gives a feeling of celebration and good mood to its many guests!

Where to find - Simon Petlyury, 4

Reservation - (067) 224-41-11''')


@bot.message_handler(regexp='🍇SkyBar', content_types=['text'])
def skybar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHkV7Jg1EcZtt7rM3j97YwtEFtRP4pAAIRrTEbrRJRSmozcc5vMEwICQLlkS4AAwEAAwIAA20AA0RIAgABGQQ',
                   '''SKYBAR is a dance nightclub. The visual concept is associated with the birth of the planet after the explosion of a volcano.

Where to find - Bolshaya Vasilkovskaya 5

Reservation - (097) 223-88-88''')


@bot.message_handler(regexp='🍇Penthouse', content_types=['text'])
def penthouse(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHi17JgwW6GanTFuztwEMGhHnfysiMAAIOrTEbrRJRSmfMHQJPO8lFVi-Cki4AAwEAAwIAA20AA2W-AQABGQQ',
                   '''Every man needs a place where he can relax and forget about the problems. Penthouse Arena is exactly what you need. This is the fulfillment of all your wildest fantasies. In this place, even the most piquant dream can come true. Incredible girls will amaze you with their beauty and fulfill all sophisticated fantasies, and you just have to have fun.

Where to find - Basseinaya, 2

Reservation - (098) 232-0-232''')


@bot.message_handler(regexp="🍷Burlesque", content_types=['text'])
def burlesque(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHf17Jgl1oYspD5zIAAXRaRpPdwlIIjwACB60xG60SUUqQOUZKO_cG1-mJZZMuAAMBAAMCAANtAANVXQACGQQ',
                   '''In 2019, Burlesque opened in Kiev and announced a program with 100 dancers every day. Burlesque (Burlesque) is not just a strip club, it is a world-class erotic theater, where every girl’s dance is a bewitching show.

Where to find - Bolshaya Vasilkovskaya 5 (Arena shopping center)

Reservation - (063) 689-50-35
''')


@bot.message_handler(regexp='🥂Dolls', content_types=['text'])
def dolls(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIHh17JgtZqPSG3f8PY84Jt_sAscfaTAAILrTEbrRJRShrsW6N9U2lqhR7rkS4AAwEAAwIAA20AA0pGAgABGQQ',
                   '''Dolls Men’s Club invites you to spend an unforgettable evening surrounded by beautiful dancers. To appreciate the combination of amazing beauty and plasticity of the participants of our strip show program. The interior, creating an atmosphere of mystery and celebration, is conducive to enjoying the show program and the strip club cuisine.

Where to find - 57/3 Bolshaya Vasilkovskaya

Reservation - (099) 380-77-44''')



#------------Хендлеры FOOD_SWEET------------
@bot.message_handler(regexp="🧁The Cake", content_types=['text'])
def thecake(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIIs17jYyE-oawqKrHQcNEBjzKiblDYAAIarjEbzVsYS3yNfeTiwx1tXP9QkS4AAwEAAwIAA20AAyOsBAABGgQ',
                   '''The Cake is a cafe and pastry shop located in the Arena City shopping and entertainment center. The interior has a pronounced Scandinavian design: rather cold colors of the room, but the brightness here is given by comfortable green armchairs and woody textures of tables. The main emphasis in the menu is on sweets and pastries of our own production. Various types of cakes, eclairs, tarts, pasta, marshmallows, marmalade are presented here. There is a separate breakfast menu, which is served from 8 in the morning until late at night.

Where to find - Bolshaya Vasilkovskaya 5

Reservation - 097 384 5707''')


@bot.message_handler(regexp="🍰Bo.Pastry", content_types=['text'])
def bo_pastry(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIIml7jYlhgVpCV2klJSzgH4s5ntB3pAAITrjEbzVsYS6nsVUSrm8OQM9MTlS4AAwEAAwIAA20AA2pNAAIaBA',
                   '''In the center of Kiev, in a small two-story building, there is a cafe-confectionery "Bo.Pastry" of the chef and TV presenter Hector Jimenez-Bravo.

The original interior of the room is made in a modern minimalist style and is designed in white, black and turquoise shades.

In the center of the hall is a tree of planks. In a large showcase, guests are presented with a wide range of desserts and pastries - gluten-free desserts, croissants, cakes, homemade pies, eclairs, pastries, pasta, marshmallows, marmalade, cookies, sweets, bread.

For a more satisfying snack, guests can order soups and sandwiches.

Where to find - Khreschatyk 19a (near the entrance to Khreshchatyk metro)

Reservation - 096 208 0088''')


@bot.message_handler(regexp="🎂Kalyna", content_types=['text'])
def kalyna(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIInl7jYqFSizIFAZC1ejPKPt5QscnSAAIVrjEbzVsYS4RJ_SWS2HRb84rmkS4AAwEAAwIAA20AA9IMAwABGgQ',
                   '''In the center of Pechersk there is a confectionery "Kalina". The interior of the establishment is made in a modern style and resembles an Italian coffee house - elegant sofas in burgundy shades, cozy tables for two, classic chandeliers and a lot of wood in decoration. Here visitors can order Italian cuisine. The main emphasis in the institution is on desserts. Guests are offered a wide range of their own pastries - cakes, strudel, macaroons, eclairs, pastries, ice cream, pastries and handmade sweets.

Where to find - Moskovskaya 29a

Reservation - 050 913 8513''')


@bot.message_handler(regexp="🍮Polverol", content_types=['text'])
def polverol(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIIpl7jYwUZI3vpqIRxDhGXsHxmA8x9AAIZrjEbzVsYS-Ag_6zr56V0wYEelS4AAwEAAwIAA20AAx5PAAIaBA',
                   '''On Podol in Kiev, along Vozdvizhenskaya street, not far from the Kontraktovaya Ploshchad metro station, there is an author's cafe and confectionery Polverol
The institution specializes in the preparation of confectionery products according to original recipes based on natural fresh products and ingredients.
In the menu, guests can find cakes, pastries, cupcakes, keypops, eclairs, chocolates, shu cakes, pasta, marshmallows, marshmallows, marmalade, cookies. In addition, the restaurant has a restaurant serving European cuisine.

Where to find - Vozdvizhenskaya 44

Reservation - 050 378 8998''')


@bot.message_handler(regexp='🍭Milk Bar', content_types=['text'])
def milkbar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIIpF7jYu2_29FnudPMMnVpGzbtYMf-AAIYrjEbzVsYS0cPAW14cIJN98h-kS4AAwEAAwIAA20AA8JpBAABGgQ',
                   '''“When I first arrived in Kiev, I realized that there wasn’t any confectionery here. Cheesecake, tiramisu, panna cotta, profiteroles, perhaps. We wanted to offer something new, but understandable. When I understand - I want to immediately. So the first two weeks I met the guests myself, told them.
In Florida, there is Key West, the southernmost point, and so in any place there is the same dessert - “Key Lime Pie”. There are no others; they do not need. I wanted to bring him here. I had to adapt a little, though. The Americans in the original super sugar, everything is super-dense - with us people don’t understand such desserts.

ALEXANDER KATAEV
pastry chef

Where to find - Verkhnyi Val, 18

Reservation - (068) 773-73-15''')


@bot.message_handler(regexp='🍯Honey', content_types=['text'])
def honey(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIInF7jYnClQA6BSSTgZLGrWqB1ZOV5AAIUrjEbzVsYSymn98GbY4ljVdQTlS4AAwEAAwIAA20AA7lMAAIaBA',
                   '''The main advantage of Butney are various author's desserts. For example, After eight, consisting of white chocolate mousse, three types of mint with chocolate ganache and honey, menthol capsules, lemon confit, walnut praline and biscuit, cooked without adding flour. The menu offers many desserts, cakes, sweets, marmalade, more than 15 types of pasta and eclairs with various fillings.
There is also a full menu, which includes first courses, salads, snacks, sandwiches and pies. Marking Vegan will help simplify your choices.
 The desire for originality and exclusivity is read in the choice of tea (cornel, quince, sea-buckthorn with orange fresh) and a coffee card. In addition to traditional options, you will be offered red slightly bitter cocoa, which is added with home-made marshmallows and a unique author's cherry raff.

Where to find:
Yaroslaviv Val, 20
Nyzhnyi Val 19-21
Khreschatyk 38 TSUM Kiev, food hall, 6th on top

Reservation - 067 127 1921''')


@bot.message_handler(regexp='🍬London: Coffee House', content_types=['text'])
def london(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIIol7jYtfYdp1B1hHguS8UQbs38noiAAIXrjEbzVsYS-VU5ocWouC9zYQelS4AAwEAAwIAA20AA4tNAAIaBA',
                   '''The coffee house immediately immerses its guests in the English atmosphere - you can get into the cafe through a real red telephone box! The coffee house is divided into three conventional zones - classic, bar and underground zone. The visitor can take any place convenient for himself and look at the original interior of the cafe. There are reproductions of paintings by the famous elusive artist Banksy. The largest of them - the British queen with David Bowie makeup - flaunts on the central wall. You can also see a map of the London Underground. Inside the coffee house is really cozy, but at the same time, it is a very stylish and modern place.

Where to find - Verkhnyi Val, 18

Reservation - (068) 773-73-15''')


@bot.message_handler(regexp="🍫Art Eclair", content_types=['text'])
def art_eclair(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIImF7jYj0pnGxkhqX-r86A5hPG3iJ5AAISrjEbzVsYS7RoxId25wG1aXXrki4AAwEAAwIAA20AA5OIAgABGgQ',
                   '''ÉCLAIR LITTLE ARTWORK - THE FIRST UKRAINIAN KINGDOM OF ECLERS
We left in the past the everyday view of everyone's favorite eclair cake. In our performance, every cake is a small work of art. This is already something fashionable, vibrant and must-eat. Now each of you can please yourself and your loved ones with this exquisite delicacy, the taste of which will remain with you forever!

Where to find - Kostelnaya, 6

Reservation - 067 903 33 77''')


@bot.message_handler(regexp='🍪Latte: coffee&desserts', content_types=['text'])
def latte_coffee(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIIoF7jYrwyqrOyVjMF2lOGKKaMoRQVAAIWrjEbzVsYS6oZsj1C31uPu9X2lC4AAwEAAwIAA20AA6W0AAIaBA',
                   '''The Latte coffee shop was founded by a professional pastry chef, Irina, who was trained by many famous chefs Hans Owando, Frank Hasnut, Guillaume Mabie, Jordi Bordas, Andrei Kanakin and Pascal Brunstein. Under the direction of Irina, cakes, pastries, pasta, truffles are prepared in the coffee shop.
All desserts served to guests in the coffee shop can be ordered at the event. Any festive cakes, candy bars, corporate orders are prepared here. Dessert delivery works.
Here you can also order a light breakfast - almond croissant, sandwich with salmon, jamon or avocado. The coffee card contains classic coffee drinks - espresso, cappuccino, aeropress, latte. We recommend trying the signature pink raff, which was invented by chance: the confectioners made syrup from a tea rose, and the barista added it to the raff. In the warmer months, it is worth trying lemonade and smoothies.

Where to find - Verhniy Val, 54

Reservation - 099 328 4963''')



#------------Хендлеры FOOD_COFFEE------------
@bot.message_handler(regexp="🧁Fandom Coffee Bar", content_types=['text'])
def thecake(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJs17mPelSQyHatmHhNUeVkBt0QzUqAAJirjEbsGs5S4jw867wpBOVIpnfky4AAwEAAwIAA20AA1qRAQABGgQ',
                   '''Fandom Coffee Bar is not just a coffee shop. This is a place where unique design, European cuisine in the author's interpretation, a variety of cocktails and great specialty coffee are harmoniously combined. The facility is located in the very center of Kiev, near the National Opera. The interior is decorated with works by Kiev artists, the mood is created by the work of metropolitan sculptors, sofas and armchairs are made in compliance with all ergonomic requirements, and soft and directional lighting does not tire your eyesight at any time of the day or evening.

Where to find - Vladimirskaya 49a

Phone - 063 380 2722''')


@bot.message_handler(regexp="🍰Takava Coffee-Buffet", content_types=['text'])
def bo_pastry(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJuV7mPkFLTjObHw9OZAgO09HQhE-tAAJlrjEbsGs5S6gcjhME7JRvn591kS4AAwEAAwIAA20AAyx5BAABGgQ',
                   '''The second coffee shop opened recently. The main concept has remained unchanged - it’s the same favorite specialty coffee on its own roasting grain and signature cocktails. The difference is the availability of a full breakfast menu, served throughout the day.

Where to find - Bolshaya Vasilkovskaya, 1-3

Phone - 063 138 2597''')


@bot.message_handler(regexp="🎂RIGHT coffee bar", content_types=['text'])
def kalyna(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJt17mPiPyPYJKxSgSM7P1qJYzoFmyAAJkrjEbsGs5S_cGv1MpoM9P0qC6ki4AAwEAAwIAA20AA6c4AwABGgQ',
                   '''The coffee house is located deep in the courtyard, which makes it very cozy. There are various zones inside the room, so for whatever purpose you are here, you will surely find yourself a nook. Drinks can be tasted from local as well as foreign roasters. In addition, a small menu and a series of desserts are presented.

Where to find - Sichovy Striltsov, 9v

Phone - 067 507 7163''')


@bot.message_handler(regexp="🍮Blur Coffee", content_types=['text'])
def polverol(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJq17mPQmDjxLVxfB770TH7OMc9vGaAAJYrjEbsGs5SyqHsJZILdYaa551kS4AAwEAAwIAA20AA7Z4BAABGgQ',
                   '''One of the biggest advantages of Blur Coffee is its spacious summer terrace, where you want to spend as much time as possible in the shade of the trees. But inside the coffee house is not inferior to anything, because the photos in this interior are practical in every Instagram of the city.
Coffee is prepared by classical and alternative methods, they offer a healthy menu.

Where to find - 5 Mechnikova

Phone - 068 270 7575''')


@bot.message_handler(regexp='🍭Yellow Place', content_types=['text'])
def milkbar(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJu17mPnDGh8-Lqlc93nm7PArgFH9RAAJmrjEbsGs5S0IiWlGbnZog3GcYlS4AAwEAAwIAA20AA4VgAAIaBA',
                   '''Coffee legend. Be sure to look at a cup of aromatic drink from the virtuosos of their craft. You can drink coffee on the spot, accompanied by a dessert, or take with you. A huge variety of varieties of fresh roasting will not leave indifferent even the most skeptical connoisseur.

Where to find - 9 Mechnikova

Phone - 044 390 7962''')


@bot.message_handler(regexp='🍯COFFEE and the CITY', content_types=['text'])
def honey(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJr17mParNbMlmOc-b_nCh1lxBj81qAAJgrjEbsGs5S-fDrlEsZp16NQABbpEuAAMBAAMCAANtAAOdcwQAARoE',
                   '''A cozy cafe where you can drink a cup of premium coffee and specialty freshly roasted grains, but the real hit here is the author's Insta-latte: Blue and Pink based on syrups made from natural ingredients. In addition to drinks, breakfast is offered throughout the day, light salads, croissants with savory and sweet fillings, soups, home-made desserts.

Where to find - Saksaganskogo, 118

Phone - 067 364 0980''')


@bot.message_handler(regexp='🍬Come and Stay', content_types=['text'])
def london(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJsV7mPdGiNrfbgQRom21vbRelybjmAAJhrjEbsGs5S7upVXYrF6kiGSd3kS4AAwEAAwIAA20AAz9qBAABGgQ',
                   '''A small Come & Stay coffee shop is located in a secluded courtyard near the Leo Tolstoy Square metro station. Recently, the guys celebrated 4 years of their work. It offers coffee classics and alternatives, fruit teas and ice cream. Go for granola or porridge for breakfast, and grab a dessert with you.

Where to find - Bolshaya Vasilkovskaya, 23v

Phone - 063 683 3241''')


@bot.message_handler(regexp="🍫Cherry coffee roasters", content_types=['text'])
def art_eclair(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJrV7mPTIP1eMSfU6b15ONHKr1LYGcAAJerjEbsGs5S9TOV-6a6P4f1pl9ki4AAwEAAwIAA20AA6GbAgABGgQ',
                   '''It is worth going for a portion of vivid impressions. Any visitor can watch how the coffee is roasted in a roaster. The cafe is quite spacious, so you can practically admire this process endlessly.

Where to find - 57 Bolshaya Vasilkovskaya

Phone - 095 238 0082''')


@bot.message_handler(regexp='🍪Khlebnyi', content_types=['text'])
def latte_coffee(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIJtV7mPgGFDaU8zO3h0rOr8mv0UXDvAAJjrjEbsGs5S1cNkijF3CysnP7ski4AAwEAAwIAA20AA3ecAgABGgQ',
                   '''Khlebnyi is a cafe-shop with fresh pastries and aromatic coffee. On the counter of the store fresh buns are sold: croissants, pies, cheesecakes, donuts and all kinds of bread. We paid great attention to coffee and attracted Slavik Babich (the main barista of Kiev) for this.

Where to find - Bolshaya Vasilkovskaya 67/7

Phone - 067 466 0696''')



#-------------Хендлеры_TRANSPORT---------
@bot.message_handler(regexp='☑️Donate☑️', content_types=['text'])
def donate(message):
    bot.send_message(message.chat.id, '''I am working on the same bots for other European cities

Donations are still in development, but you can leave a donation at the Last Barricade restaurant or transfer to a card:

UA Number: 4441 1144 4445 2757(monobank)
or
IBAN: UA983220010000026203300262395''')



#-------------Хендлеры_TRANSPORT---------
@bot.message_handler(regexp='🚇Metro', content_types=['text'])
def transport_metro(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIMYV7pLYX5yGK1-XhjZ4iKAoOr8HbpAALPsDEb-2pJS8j5CCbOK-l5gCm8ki4AAwEAAwIAA20AA_pFAwABGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIMXV7pLXjur0xTaJNOW8yj-77wAjDjAALKsDEb-2pJS36w09YEDUBo_mfoki4AAwEAAwIAA20AAzu1AgABGgQ')
    bot.send_message(message.chat.id, '''Choose the metro scheme that you like and save to your phone. Because there will be no Internet in the subway
First one is official scheme😎''',
                     reply_markup=Keyboards.transport_metro())

@bot.message_handler(regexp='🚖Taxi', content_types=['text'])
def transport_taxi(message):
    bot.send_message(message.chat.id, '''❌Never take a taxi from the street❌

The best way is to use the app

Prices on average - 50-70 UAH (2-3 $) in the center, 100-120 UAH (4-5 $) from the Left Side of Kiev to the center


There are 3 main taxi call services in Kiev:

1) Uber
2) Uklon
3) Bolt

Check prices in all three apps during peak hours, because prices can vary 2-3 times

Everything can be found in Apple Store and Google Play''')

@bot.message_handler(regexp='🚲Bike', content_types=['text'])
def transport_bike(message):
    bot.send_message(message.chat.id, '''🚲In Kiev, you can ride a bicycle and an electric scooter quite cheaply.The first application is BikeNow(you can download it in PlayMarket and AppStore) in it you can look at which station there are bicycles, pay by card, the price is 20 UAH - 30 minutes. Do not forget to test your bike for proper functioning.

🛴Through the Bolt application (taxi) you can take electric scooters''')




#------------Хендлеры_TOURSE_MURALS---------------
@bot.message_handler(regexp='🏞Murals', content_types=['text'])
def murals_pres(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAINnl7tw3jZTiu-pEDkknoxgntUSLkNAALhrTEbqSloS0f2CKxBaQy5wQtxkS4AAwEAAwIAA20AA-GsBAABGgQ',
                   '''Tour Time - 2.5 hours
Distance -    5 km
Start End -   Ⓜ️Zoloti Vorota 🔜 Ⓜ️Kontraktova Ploscha
Quantity - Mural:   21
                    Art-Obj: 7
                    Beauty: ♾
Voice acting - @p_babin
Photographer - @zoia_didok''',
                   )
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIPJl7vW1dxaWs4kA5rVP-rQVTIjSBHAALNBgAC57iAS2I6si3nAr4yGgQ',
                   reply_markup=Keyboards.mural_pres()
                   )

@bot.message_handler(regexp='"Murals": Step 1👉🏼', content_types=['text'])
def murals_1(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIOOl7vDhZEd__DrWAXzDaE-w8tSlnzAAJorTEb57h4S39GrCU2W_lFVRCXlS4AAwEAAwIAA20AA8WfAAIaBA',
                   reply_markup=Keyboards.mural_1())
    bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAIO_V7vWJQrLRxj1CpITO3m4d0ypV7cAALHBgAC57iAS4oG76snne6PGgQ')
    bot.send_message(message.chat.id, '👇🏼When you will be there, click on the next step👇🏼')

@bot.message_handler(regexp='"Murals": Step 2👉🏼', content_types=['text'])
def murals_2(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIOq17vPAQ8idJ97HgVM55XMnhmV8bmAAL_rzEb57iAS5L9eOhNZNCgj_jXky4AAwEAAwIAA20AA7POAQABGgQ',
                   reply_markup=Keyboards.mural_2())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIPDF7vWROLcvviL3e-8DFHQjAO4YJDAALJBgAC57iAS2Lsywkz2uR7GgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIQ1F7wMOedu1ilmzrr3LH-h3sWa2OXAAKZrzEb57iIS-lLgWdZ_OxUujSglS4AAwEAAwIAA20AAyumAAIaBA')

@bot.message_handler(regexp='"Murals": Step 3👉🏼', content_types=['text'])
def murals_3(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIPrl7vapMSnjhOlae_BS_LS4FfaiF9AAIosDEb57iASwPkdtXGtrKe7_WQlS4AAwEAAwIAA20AA9elAAIaBA',
                   reply_markup=Keyboards.mural_3())
    bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAISBF7xqJ867rWMXVAF-SNKuXGAZLadAALUBgACcieQS4EWYWrvI7zfGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIQFl7viFtYX30lJ1NLq4jMS2mAFiKtAAI8sDEb57iASx1u1qeu_y0wQV34lC4AAwEAAwIAA20AAxIQAQABGgQ',
                   reply_markup=Keyboards.yaroslav_joke())

@bot.message_handler(regexp='"Murals": Step 4👉🏼', content_types=['text'])
def murals_4(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIQWF7vmwQCXIAB8UMvVBiXqPUpR7WtAAJSsDEb57iASycPtBJ_nBNf1gtxkS4AAwEAAwIAA20AA7W-BAABGgQ',
                   reply_markup=Keyboards.mural_4())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAISBl7xqKn4bXa3eZ5rZqK4pvJMaJ0fAALVBgACcieQS5VPC1CWJyk1GgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIQWl7vmyLEnunqOTH8z6l3O-yo0LdwAAJTsDEb57iAS4_9OvZs5vOJBqKblS4AAwEAAwIAA20AA7imAAIaBA')

@bot.message_handler(regexp='"Murals": Step 5👉🏼', content_types=['text'])
def murals_5(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIRBl7wN-pmXmYEOTCKebDU6a20Kg0zAAKbrzEb57iISwzisWrgM5BpDrWDki4AAwEAAwIAA20AA9rjAgABGgQ',
                   reply_markup=Keyboards.mural_5())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAITl17yKon7x_uGdVZWqDtGkc1bdmjOAAJKBwACcieYSz2d_02yt5LdGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAISIl7xscpCnpPeBt3N16n3jj2eJSHsAAIlrzEbcieQSyQkAAEBqrUi7gN7kpUuAAMBAAMCAANtAANstAACGgQ',
                   reply_markup=Keyboards.coffe_honey())
            
@bot.message_handler(regexp='"Murals": Step 6👉🏼', content_types=['text'])
def murals_6(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAISR17xuVVdIsx9Z1Y7RPT164HXRDg1AAIvrzEbcieQSwh99e-B_joCEPSQlS4AAwEAAwIAA20AA160AAIaBA',
                   reply_markup=Keyboards.mural_6())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIVgl71gWtIzH8NlZPI_ktlaHegY_3RAAI1CQACiqexS1qiwqUaQl1MGgQ')

@bot.message_handler(regexp='"Murals": Step 7👉🏼', content_types=['text'])
def murals_7(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIUNV7y3trbUGTyc5RmQbs4DM07bzrlAAJArTEb9M6YS4tuPReiIcyeHAtxkS4AAwEAAwIAA20AA2zYBAABGgQ',
                   reply_markup=Keyboards.mural_7())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIVhF71gXZ6YnNmsXuj_UxlLSc9earvAAI2CQACiqexS2671Vk3aThyGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIUNl7y3t2gKzyGUG_dxz42PDXB-LlVAAJBrTEb9M6YS9L9of2C2RlWI_NNkS4AAwEAAwIAA20AA8UVBQABGgQ')

@bot.message_handler(regexp='"Murals": Step 8👉🏼', content_types=['text'])
def murals_8(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIV0l71h2HeEokUazeqKTfnslWfdiW2AAJ8rTEbiqexS0eJZFqz70baKPAZlS4AAwEAAwIAA20AAx_RAAIaBA',
                   reply_markup=Keyboards.mural_8())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIbw175wfX_b4a5UHCDLhUJ1j6q1cjvAAKDBwAC0sPRSyHHRaIRqTdSGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIWbV71i97SOCV0z6mqJCglQwrm96RaAAKErTEbiqexSy-YsPXad6jsdLG9ki4AAwEAAwIAA20AA6ikAwABGgQ')

@bot.message_handler(regexp='"Murals": Step 9👉🏼', content_types=['text'])
def murals_9(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIWQ171ibeKJQbTjKky5w9sLgbQebrIAAJ-rTEbiqexS80xhSCkPo-qFWroki4AAwEAAwIAA20AA_ENAwABGgQ',
                   reply_markup=Keyboards.mural_9())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIbxV75wiSFu-QiXc7snBf_ArxWVcfvAAKEBwAC0sPRS5ccSagef4HmGgQ')

@bot.message_handler(regexp='"Murals": Step 10👉🏼', content_types=['text'])
def murals_10(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIWzl71kMi8WheRcXJAX_5vTddVCFR9AAKrrTEbiqexS5QJTJLCG6wgdqTskS4AAwEAAwIAA20AAyqXAwABGgQ',
                   reply_markup=Keyboards.mural_10())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAImql8FmqqzatJxwDYS4us0N_M0GIEhAAJcBwACOkQwSCmJATvtR7IYGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIW0l71kOzlftPua1RkGwABkuDcRwTAmQACra0xG4qnsUuRpgTwB0tJ3nUc65EuAAMBAAMCAANtAAPklQMAARoE')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIW0F71kON7MjxskjDC2uBQ1cx8bnRgAAKsrTEbiqexS-oL6tv59d2NnX3jkS4AAwEAAwIAA20AA5uRAwABGgQ')

@bot.message_handler(regexp='"Murals": Step 11👉🏼', content_types=['text'])
def murals_11(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIcoF7514My9FhnpCY1RSLfwD7jxjlEAALgsDEb0sPRS0yT3EE1MeX2Py-Cki4AAwEAAwIAA20AA6YuAwABGgQ',
                   reply_markup=Keyboards.mural_11())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAImrF8Fms_su-vRwPn1f-M0VonHdEkwAAJdBwACOkQwSFonRdnwBpc_GgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIdzV79lf9ezQZffTt49kOZlNubVc8GAAL5rTEbrDLoS-VgiF_O6Xr7UPfhkS4AAwEAAwIAA20AAzfEAwABGgQ')

@bot.message_handler(regexp='"Murals": Step 12👉🏼', content_types=['text'])
def murals_12(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIep179oKx8vlpjxuYIpidop434CexqAAOuMRusMuhLZrMW4u9w7-hODpeVLgADAQADAgADbQADWwsBAAEaBA',
                   reply_markup=Keyboards.mural_12())

@bot.message_handler(regexp='"Murals": Step 13👉🏼', content_types=['text'])
def murals_13(message):
    bot.send_message(message.chat.id,
                     '🇺🇦Ukrainian Soviet writer, publicist and public figure🖋')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIfE179p94-9i9_Ph9Sjv1fR9YTfRoLAAIOrjEbrDLoS5wbtHZ54qaRunlPkS4AAwEAAwIAA20AA-xmBQABGgQ',
                   reply_markup=Keyboards.mural_13())
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIf0179rV9d2rx_WTvX8lA1bfZUqTPcAAIRrjEbrDLoS7D7jwrVL66umGfoki4AAwEAAwIAA20AAwdLAwABGgQ')

@bot.message_handler(regexp='"Murals": Step 14👉🏼', content_types=['text'])
def murals_14(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIf1V79ren4PznskGFbEu9AQIWsliOpAAISrjEbrDLoS--e_I8neZMnQSR3kS4AAwEAAwIAA20AA7UlBQABGgQ',
                   reply_markup=Keyboards.mural_14())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAImrl8FmxdetTNyJagLEKeA6BWkfvptAAJfBwACOkQwSOZk2uDkzt8PGgQ')

@bot.message_handler(regexp='"Murals": Step 15👉🏼', content_types=['text'])
def murals_15(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAInHV8FqJf6mLbgqqLC6LUksB0E-IUhAAI-rjEbOkQwSCXKrI7L-DTJ1fXhkS4AAwEAAwIAA20AAzcJBAABGgQ',
                   reply_markup=Keyboards.mural_15())
    bot.send_message(message.chat.id, '👈So, let"s go on')
    bot.send_sticker(message.chat.id,
                   'CAACAgIAAxkBAAIhI179umdDis9GUh5pWqniUngL3H_8AAKCCAACeVziCd1eGH84UPxHGgQ')

@bot.message_handler(regexp='"Murals": Step 16👉🏼', content_types=['text'])
def murals_16(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIhol79yInUHk8H22CDe-9ZSRF6TuERAAKvrjEbrDLwS8IyXTr-Aved6QxxkS4AAwEAAwIAA20AA_ouBQABGgQ',
                   reply_markup=Keyboards.mural_16())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAImsF8Fm0j3LeQ2WvydJU-7vStSg9U3AAJgBwACOkQwSBWHAbewsm_XGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIhpF79yJEdssJgQmKes9VnNoKVmR5KAAKwrjEbrDLwSxmLeZ4pGcI78q2elS4AAwEAAwIAA20AA3QOAQABGgQ')
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAImsl8Fm2xqsPhVN-0fSSnb2dnO6H9yAAJhBwACOkQwSKk08yLKVeusGgQ')

@bot.message_handler(regexp='"Murals": Step 17👉🏼', content_types=['text'])
def murals_17(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIh6F79zDsYho6N95idBlQJAAG6rPi87gACua4xG6wy8EsqGjS1vv-uLPVNEpUuAAMBAAMCAANtAAMwDQEAARoE',
                   reply_markup=Keyboards.mural_17())
    bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAItsl8UK0u2tlHH17PJg-YLVnFqdbPeAAIzBwACY32hSAABtUAClbhZKBoE')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAInZ18FrAuC4ykNRsaWi8q8hU9SsgqCAAJFrjEbOkQwSEmTLNjfj2Bn-bSDki4AAwEAAwIAA20AA-eCAwABGgQ')
    bot.send_message(message.chat.id,
                     'Go, Morty')
    bot.send_sticker(message.chat.id,
                     'CAACAgIAAxkBAAIh7V79zQlIDw-WGrfmFR-_2XEZPAjwAAI8AwACtXHaBiUqGutotFmMGgQ')

@bot.message_handler(regexp='"Murals": Step 18👉🏼', content_types=['text'])
def murals_18(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAInsl8FrzjpjI-AxzmR72qC5xIItksFAAIbrzEbkw8xSNJ53OnWq8EaLsd-kS4AAwEAAwIAA20AA4lZBQABGgQ',
                   reply_markup=Keyboards.mural_18())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIttF8UK1iixjXRjSEB2BxVfui37apdAAI0BwACY32hSGEd1najtAnaGgQ')

@bot.message_handler(regexp='"Murals": Step 19👉🏼', content_types=['text'])
def murals_19(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIoS18GBKHysVUe_TfzwXn2h8LHTC8mAAKbrjEbOkQwSJeutaEAAecw6HuC7pIuAAMBAAMCAANtAAMXfQMAARoE',
                   reply_markup=Keyboards.mural_19())
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIoU18GBnmTpXZsfJTQPUil9LZ7jtJRAAKfrjEbOkQwSJnZYKg31-FT-oEelS4AAwEAAwIAA20AA0pMAQABGgQ')
    bot.send_message(message.chat.id, "🏃‍♀️Let's go on🏃‍♂️")

@bot.message_handler(regexp='"Murals": Step 20👉🏼', content_types=['text'])
def murals_20(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuC18UMrEZJsBV4oPD0KAhQxFXPdbdAAKnrjEbY32hSJ59Ck9drhh1zv0clS4AAwEAAwIAA20AA3i3AQABGgQ',
                   reply_markup=Keyboards.mural_20())

@bot.message_handler(regexp='"Murals": Step 21👉🏼', content_types=['text'])
def murals_21(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuXl8UNCcN1plyCPaJs8v0d48s9FLZAAKorjEbY32hSATW_Ypfa065gA6XlS4AAwEAAwIAA20AA5-4AQABGgQ',
                   reply_markup=Keyboards.mural_21())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIttF8UK1iixjXRjSEB2BxVfui37apdAAI0BwACY32hSGEd1najtAnaGgQ')

@bot.message_handler(regexp='"Murals": Step 22👉🏼', content_types=['text'])
def murals_22(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuuF8UOHc78ZYOJtHwmA5hjVcKAjxeAAKqrjEbY32hSBC71zQoMZ7KkWcYlS4AAwEAAwIAA20AA261AQABGgQ',
                   reply_markup=Keyboards.mural_22())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIttF8UK1iixjXRjSEB2BxVfui37apdAAI0BwACY32hSGEd1najtAnaGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuul8UOaaZlxb570uUxwUP8qYD-TTdAAKsrjEbY32hSDzDgg2z24W5HyZ3kS4AAwEAAwIAA20AA27OBQABGgQ')

@bot.message_handler(regexp='"Murals": Step 23👉🏼', content_types=['text'])
def murals_23(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuvF8UPNpviTiRcGLPQFbrcbHEHXa_AAKwrjEbY32hSD14rvGBd0CvEPrXky4AAwEAAwIAA20AA73kAgABGgQ',
                   reply_markup=Keyboards.mural_23())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIttF8UK1iixjXRjSEB2BxVfui37apdAAI0BwACY32hSGEd1najtAnaGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuvV8UPOnPmtEIEvtuDfTH2WUGGYzYAAKxrjEbY32hSFwbBAKOlM4g3Rp0kS4AAwEAAwIAA20AA3_KBQABGgQ')

@bot.message_handler(regexp='"Murals": Step 24👉🏼', content_types=['text'])
def murals_24(message):
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuvF8UPNpviTiRcGLPQFbrcbHEHXa_AAKwrjEbY32hSD14rvGBd0CvEPrXky4AAwEAAwIAA20AA73kAgABGgQ',
                   reply_markup=Keyboards.mural_24())
    bot.send_audio(message.chat.id,
                   'CQACAgIAAxkBAAIttF8UK1iixjXRjSEB2BxVfui37apdAAI0BwACY32hSGEd1najtAnaGgQ')
    bot.send_photo(message.chat.id,
                   'AgACAgIAAxkBAAIuvV8UPOnPmtEIEvtuDfTH2WUGGYzYAAKxrjEbY32hSFwbBAKOlM4g3Rp0kS4AAwEAAwIAA20AA3_KBQABGgQ')



#ARTAFICIAL INTELEGENT
@bot.message_handler(content_types=['text'])
def ArtaficialIntelegent(message):
    try:
        ans = AI.question(message.text)
        if ans == 'greeting':
            return bot.send_message(message.chat.id,
                             'Hey, {}'.format(message.chat.first_name))
        elif ans == 'wether':
            return bot.send_message(message.chat.id,
                             weather())
        elif ans == 'coffee':
            return coffee(message)
        elif ans == 'wine':
            return local_wine(message)
        elif ans == 'food':
            return food(message)
        elif ans == 'HowAreYou':
            return bot.send_message(message.chat.id, "Well, I'm a robot. I can set any mood for myself.\nAnd you,Leather Bag ? ")
        elif ans == 'thanks':
            return bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIlfl8C9C-ysj7LpddaICQ-EVQ1UTd5AAImAwACtXHaBj4ZC4vnHBlAGgQ")
        elif ans == 'steak':
            return steak(message)
        elif ans == 'joke':
            return bot.send_message(message.chat.id, choice(jokes))
    except KeyError:
        return bot.send_message(message.chat.id,
                         'I dont know answer for this question. But I"m learning...\nYou can ask my Dad @serebrichdima')



# Получить ИД фоток и АУДИО дорожек ОГГ
@bot.message_handler(content_types=['photo'])
def ID(message):
    bot.send_message(message.chat.id, '{}'.format(message.photo[0].file_id))

@bot.message_handler(content_types=['audio'])
def audioID(message):
    bot.send_message(message.chat.id, '{}'.format(message.audio.file_id))

@bot.message_handler(content_types=['document'])
def docID(message):
    bot.send_message(message.chat.id, '{}'.format(message.document.file_id))

@bot.message_handler(content_types=['sticker'])
def stickerID(message):
    bot.send_message(message.chat.id, '{}'.format(message.sticker.file_id))

@bot.message_handler(content_types=['video'])
def videoID(message):
    bot.send_message(message.chat.id, '{}'.format(message.video.file_id))


#-----Polling----
bot.infinity_polling(True)