# --------------------------------------- global resources -----------------------------------------------
from random import randint
from dataclasses import dataclass
from datetime import datetime



# --------- item stuff ----------------

#  remove initialize_all_items (resources already globalized)  Done
#  and make the program not shit itself due to its removal


@dataclass
class Item:
    name: str
    top_level_category: str
    category: str
    description: str
    price: float
    req_skill_lv: int
    infl_mass: int
    infl_health: int
    infl_mood: int
    infl_anger: int
    infl_boredom: int
    infl_confusion: int

    def __str__(self):
        return (f'Name: {self.name} \nKategorie: {self.category_ch} \nBeschribig: {self.description} \n'
                f'Pris: {str(self.price)} \nBenötigts Skill-Level: {str(self.req_skill_lv)} \nEffekt Masse: '
                f'{str(self.infl_mass)}'
                f'\nEffekt Gsundheit: {str(self.infl_health)} \nEffekt Stimmig: {str(self.infl_mood)} '
                f'\nEffekt Hässigkeit: {str(self.infl_anger)} \nEffekt Langwiili: {str(self.infl_boredom)}'
                f'\nEffekt Verwirrtheit: {str(self.infl_confusion)}')

    @property
    def category_ch(self):
        translations = {  # firearm
            'handgun': 'Pistole',
            'assault rifle': 'Sturmgwehr',
            'rifle': 'Gwehr',

            # explosive
            'anti tank': 'Panzerabwehr',
            'anti personnel': 'Anti-Persone',

            # consumable
            'medical': 'Medizin',

            # videogame
            'minecraft': 'Minecraft',

            # meme
            'insider': 'Insider',
            'classic': 'Klassiker'

        }

        try:
            translation = translations[self.category]
        except KeyError:
            input('ERROR: Item category translation not registered in category_ch()')
            translation = 'TRANSLATION ERROR'

        return translation

    @property
    def top_level_category_ch(self):
        translations = {'firearm': 'Schusswaffe',
                        'explosive': 'Schprängstoff',
                        'consumable': 'Konsummittel',
                        'videogame': 'Videospiel',
                        'meme': 'Meme',
                        }

        try:
            translation = translations[self.top_level_category]
        except KeyError:
            input('ERROR: Item top_level_category translation not registered in category_ch()')
            translation = 'TRANSLATION ERROR'

        return translation


item_colt_m1911 = Item('Colt M1911', 'firearm', 'handgun', 'E pistole halt', 20.0, 1, 0, -25, -25, 30, -40, 0)

item_mk_1_handgrenade = Item('Mk.1 Splittergranate', 'explosive', 'anti personnel',
                             'Tätscht und verteilt Metall-Konfetti', 30.0, 1, 0, -50, -40, 40, -50, 0)

item_rpg_7 = Item('RPG-7', 'explosive', 'anti tank', 'Nöd hine ineluege', 100.0, 3, -100, -50, -75, 50, -50, 0)

item_m16a1 = Item('M16A1', 'firearm', 'assault rifle', 'Wahre Klassiker', price=45.0, req_skill_lv=2, infl_mass=0,
                  infl_health=-15, infl_mood=-10, infl_anger=20, infl_boredom=-15, infl_confusion=0)

item_m1_garand = Item('M1 Garand', 'firearm', 'rifle', 'Tönt kuul bim Nahlade', price=20.0, req_skill_lv=2,
                      infl_mass=0, infl_health=-10, infl_mood=-10, infl_anger=15, infl_boredom=-15, infl_confusion=0)

item_m24 = Item('M24', 'firearm', 'rifle', 'De Siech isch scheisse lut aber fäggt', price=50.0, req_skill_lv=3,
                infl_mass=0, infl_health=-35, infl_mood=-15, infl_anger=20, infl_boredom=-15, infl_confusion=0)

item_kar98k = Item('Kar98k', 'firearm', 'rifle', 'Gar nöd eso churz', price=75.0, req_skill_lv=4,
                   infl_mass=0, infl_health=-25, infl_mood=-15, infl_anger=20, infl_boredom=-15, infl_confusion=0)

item_stg_44 = Item('StG 44', 'firearm', 'assault rifle', 'Ich han die imfall vergoldet in Battlefield V', price=80.0,
                   req_skill_lv=4, infl_mass=0, infl_health=-20, infl_mood=-15, infl_anger=15, infl_boredom=-15, infl_confusion=0)

item_glock_17 = Item('Glock 17', 'firearm', 'handgun', "D'Öschis wüssed wies gaht", price=40.0, req_skill_lv=5,
                     infl_mass=0, infl_health=-10, infl_mood=-10, infl_anger=15, infl_boredom=-15, infl_confusion=0)

item_medkit = Item('Medikit', 'consumable', 'medical', 'Universale Hälfer', price=10.0, req_skill_lv=1, infl_mass=0,
                   infl_health=30, infl_mood=20, infl_anger=-20, infl_boredom=0, infl_confusion=0)

item_diamond_pickaxe = Item('Diamante Pickaxe', 'videogame', 'minecraft',
                            'Alte, mit dem chasch fucking Obsidian abbaue', price=100.0, req_skill_lv=10, infl_mass=-50,
                            infl_health=-50, infl_mood=-20, infl_anger=30, infl_boredom=0, infl_confusion=15)
item_secret_firedragon = Item('De geheimi Fürdrache', 'meme', 'insider', 'Alte, er hätt de geheimi Fürdrache!',
                              price=10000.0, req_skill_lv=100, infl_mass=0, infl_health=-200, infl_mood=-150, infl_anger=100,
                              infl_boredom=-100, infl_confusion=100)
item_horny_bat = Item('Anti-Hornig-Schleger', 'meme', 'classic', 'Gang is hornig-Gfängniss', price=20.0,
                      req_skill_lv=4, infl_mass=0, infl_health=-5, infl_mood=-20, infl_anger=30,
                      infl_boredom=0, infl_confusion=5)


all_items = [item_colt_m1911, item_mk_1_handgrenade, item_rpg_7, item_m16a1, item_m1_garand,
             item_m24, item_kar98k, item_stg_44, item_glock_17, item_medkit, item_diamond_pickaxe,
             item_secret_firedragon, item_horny_bat]

# --------- item stuff ----------------

# --------- player stuff --------

@dataclass
class Player:
    skill_lv: int
    xp: int
    balance: float


player = Player(skill_lv=1, xp=90, balance=500.0)
player_inventory = [item_colt_m1911, item_m16a1, item_rpg_7, item_medkit]
player_stocks = ['Microsoft', 'Microsoft', 'Tesla', 'Bitcoin']


# --------- player stuff ------

# --------- achievement stuff ---------
@dataclass
class Achievement:
    name: str
    description: str
    reward: float
    time_earned: datetime = datetime(1970, 1, 1, 12, 00)

    def __str__(self):
        pass
        # TODO: create __str__ method for achievement

    @property
    def time_earned_formatted(self):
        time_earned_formatted = datetime.strftime(self.time_earned, '%H:%M:%S')
        return time_earned_formatted


test_achievement = Achievement('Test Achievement', 'En test du Dubbel', 1000000.0)
test_achievement_2 = Achievement('Test Achievement 2', 'De zweiti Test du Dubbel', 500000.0, )
achievement_1 = Achievement('Mueter-Killer', 'Leg dini erschti Mueter um', 100.0)
achievement_2 = Achievement('Arschloch', 'Duen erfolgrich en Cheat code ihlöse', -50.0)
achievement_3 = Achievement('r/WallStreetBets Immigrant', 'Chauf en Aktie', 75.0)
achievement_4 = Achievement('Kulturkänner', 'Chauf es Meme Item im Shop', 120.0)
achievement_5 = Achievement('Dully', 'Wähl e inexistänti Option us', -20)
all_achievements = [achievement_1, achievement_2, achievement_3, achievement_4,
                    achievement_5]

player_achievements = [test_achievement, test_achievement_2]

# --------- achievement stuff ---------


# --------------------------------------- global resources -----------------------------------------------
# --------------------------------------------- inputs -------------------------------------------

def input_selection(valid_selections, selection_names, prompt):
    """
    asks the user for yes or no with a given prompt as question.
    :param selection_names:
    :param valid_selections:
    :param prompt:
    :return user_input:
    """
    while True:
        print(f'{prompt}')
        for selection_name, selection_letter in zip(selection_names, valid_selections):
            print(f'{selection_letter.upper()}) {selection_name}')
        user_input = input('> ').lower()
        if user_input in valid_selections:
            break
        else:
            print(f'Alte, das sind dini Optione: ')

    return user_input


def input_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print('Du musch e natürlichi Zahl igeh du Depp (weisch 1, 2, 3 etc. kännsch?). ')
        else:
            break

    return user_input


def input_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
        except ValueError:
            print('Du musch e Rationali Zahl igeh du Depp (11.38, 42, 3.124 etc.). ')
        else:
            break

    return user_input


# ----------------------------------------------- inputs ------------------------------------------------
# --------------------------------------------- items ------------------------------------------

def show_items(item_list, printed_properties):
    """
    prints all items
    :param printed_properties:
    :param item_list:
    should be printed
    :return: none
    """
    print('show_items() is being executed')
    if printed_properties == 'show all properties':
        for item in item_list:
            print('--------------------------')
            print(str(item))
            print('--------------------------')
            input()
    elif printed_properties == 'show only names':
        for item in item_list:
            print(f'Nr. {str(item_list.index(item))}: {str(item.name)}')
        input()
    elif printed_properties == 'show only names and price':
        for item in item_list:
            print(f'Nr. {str(item_list.index(item))}: {str(item.name)}  CHF {str(item.price)}')
        input()
    else:
        print('ERROR: printed_properties parameter not correctly defined (show_items())')


def select_item(item_list):
    item_top_level_categories = []
    for category in item_list:
        if category.top_level_category_ch not in item_top_level_categories:
            item_top_level_categories.append(category.top_level_category_ch)

    for top_level_category in item_top_level_categories:
        print(f'Nr.{item_top_level_categories.index(top_level_category)}: {top_level_category}')

    while True:
        user_category_number = input_int("Gib d'Nummere vo de Überkategorie ih > ")
        try:
            chosen_top_level_category = item_top_level_categories[user_category_number]
        except IndexError:
            print('Die Kategorie existiert nöd, du Dubbel. ')
        else:
            break

    categories = []
    for item in item_list:
        if item.top_level_category_ch == chosen_top_level_category and item.category_ch not in categories:
            categories.append(item.category_ch)

    print(f'\n--- {chosen_top_level_category} ---')
    for category in categories:
        print(f'Nr.{categories.index(category)}: {category}')

    while True:
        user_category_number = input_int("Gib d'Nummere vo de Kategorie ih > ")
        try:
            selected_category = categories[user_category_number]
        except IndexError:
            print('Die Kategorie existiert nöd du schlaue. ')
        else:
            break

    items_of_chosen_category = []
    for item in item_list:
        if item.category_ch == selected_category:
            items_of_chosen_category.append(item)

    print(f'\n--- {selected_category} ---')
    for item in items_of_chosen_category:
        print(f'Nr.{items_of_chosen_category.index(item)}: {item.name}')

    while True:
        user_item_number = input_int("Gib d'Nummere vom Item ih > ")
        try:
            selected_item = items_of_chosen_category[user_item_number]
        except IndexError:
            print('Das Item existiert nöd du schlaue. ')
        else:
            break

    return selected_item


# --------------------------------------------- items ------------------------------------------
# -------------------------------------------- player ------------------------------------------


def show_player_inventory():
    print('show_player_inventory() is being executed')
    compactness = ''
    while compactness != 'x':
        compactness = input_selection(['a', 'k', 'x'], ['Alli Eigeschafte', 'Kompakt', 'zrugg zum Hauptmenü'],
                                      'Was sött alles ahzeigt werde?')
        if compactness == 'a':
            show_items(player_inventory, 'show all properties')
        if compactness == 'k':
            show_items(player_inventory, 'show only names')
    main_menu()


def check_player_xp():
    if player.xp >= 100:
        gained_levels = player.xp / 100
        gained_levels = int(gained_levels)
        player.xp -= gained_levels * 100
        player.skill_lv += gained_levels

        unlocked_items = []
        for item in all_items:
            if item.req_skill_lv <= player.skill_lv:
                unlocked_items.append(item)

        print('\n-------------------- LEVEL UP --------------------')
        print_skill_lv_bar()
        print(f'\n            Du bisch jetzt uf Level {player.skill_lv}            ')
        print('\n       Folgendi Items häsch du freigschalte: ')
        for item in unlocked_items:
            print(item.name, end=", ")
        print('\n-------------------- LEVEL UP --------------------')
        input()


def print_skill_lv_bar():
    while player.xp >= 100:
        if player.xp >= 100:
            player.xp -= 100
            player.skill_lv += 1

    total_bar_chars = 50
    xp_percentage = player.xp * 100 / total_bar_chars
    xp_chars = total_bar_chars * (xp_percentage / 200)
    printed_xp_chars = 0
    print(player.skill_lv, end="")
    print(f'{player.skill_lv + 1:49d}')
    for i in range(int(xp_chars)):
        print('=', end="")
        printed_xp_chars += 1

    rest_of_bar_chars = 50 - printed_xp_chars

    for i in range(rest_of_bar_chars):
        print('o', end="")

    xp_untill_level_up = 100 - player.xp
    print(f'\n           XP bis zu Skill-Level {player.skill_lv + 1}:  {xp_untill_level_up}           ')


# -------------------------------------------- player ------------------------------------------
# -------------------------------------------- achievements ------------------------------------------
def show_player_achievements():
    for achievement in player_achievements:
        print()
        print(f'-- {achievement.name} -- ')
        print(f'{achievement.description}')
        print(f'Verdient: {achievement.time_earned_formatted}')
        print(f'CHF {achievement.reward}')
        input()


def add_achievement(achievement):
    achievement.time_earned = datetime.now()
    player_achievements.append(achievement)


# -------------------------------------------- achievements ------------------------------------------

# --------------------------------------------- shop --------------------------------------------


def buy_items():
    print('buy_items() is being executed')
    items_shop = all_items
    selected_item = select_item(items_shop)
    if selected_item.req_skill_lv > player.skill_lv:
        print(f'{selected_item.name} verlangt Skill-Level {selected_item.req_skill_lv}')
        input(f'Du bisch uf Level {player.skill_lv}, du Opfer. ')
        shop()

    if selected_item.price > player.balance:
        input(f'{selected_item.name} chostet {selected_item.price}, du häsch {player.balance}')
        input("Das heisst du bisch z'broke zum das chaufe, hau ab! ")
        shop()

    if selected_item.price <= player.balance:
        player_inventory.append(selected_item)
        input(f'{selected_item.name} isch dim Inventar hinzuegfüegt worde. ')
        player.balance -= selected_item.price
        input(f'{selected_item.price} Stutz sind dim Konto abzoge worde. ')


# --------------------------------------------- shop --------------------------------------------

# --------------------------------------------- bank ---------------------------------------------

# -------------- investing ------------------

def invest():
    user_selection = input_selection(['c', 'v'], ['Chaufe', 'Verchaufe'], 'Was wetsch du mache? ')
    if user_selection == 'c':

        stocks, krypto, other = randomize_stock_values()
        all_stocks = {}
        all_stocks.update(stocks)
        all_stocks.update(krypto)
        all_stocks.update(other)

        investment_selection = input_selection(['a', 'k', 's'], ['Aktie', 'Krypto', 'andere Scheiss'],
                                               'I was wetsch du investiere? ')
        if investment_selection == 'a':
            buy_stock(stock_list=stocks)
        if investment_selection == 'k':
            buy_stock(stock_list=krypto)
        if investment_selection == 's':
            buy_stock(stock_list=other)

    if user_selection == 'v':
        sell_stock()


def buy_stock(stock_list):
    selected_stock_key = select_stock(stock_list)
    selected_stock_price = stock_list[selected_stock_key]

    while True:
        stock_quantity = input_int('Wieviel ' + selected_stock_key + ' wetsch du chaufe > ')
        total_stock_price = stock_quantity * selected_stock_price
        if total_stock_price > player.balance:
            print(f'{stock_quantity} {selected_stock_key} chosted {total_stock_price},')
            input(f"du häsch CHF {player.balance} uf dim Konto, das heisst du bisch z'broke. ")
        else:
            buy_confirmation = input_selection(['y', 'n'], ['Ja', 'Nei'],
                                               'Bisch du dir sicher, dass du ' + str(stock_quantity) +
                                               ' ' + selected_stock_key + ' für ' + str(
                                                   total_stock_price) + ' chaufe wetsch? ')
            if buy_confirmation == 'y':
                break
            if buy_confirmation == 'n':
                invest()  # go back to invest terminal

    for i in range(stock_quantity):
        player_stocks.append(selected_stock_key)

    player.balance -= total_stock_price

    print(f'Du häsch {stock_quantity} {selected_stock_key} für je CHF {selected_stock_price} gkauft. ')
    input(f'Dim Konto sind CHF {total_stock_price} abzoge worde.')

    bank()


def select_stock(stock_list):
    keys = list(stock_list.keys())
    for key, value in stock_list.items():
        print(f'Nr.{keys.index(key)} {key}: CHF {value}')

    while True:
        try:
            stock_selection = input_int("Gib d'Nummere vo dinere Aktie ih > ")
            selected_stock_key = keys[stock_selection]
            if stock_selection < 0:
                print('Ungültigi Uswahl')
                continue
        except IndexError:
            print('Ungültigi Uswahl')
        else:
            break

    return selected_stock_key


def sell_stock():
    stocks, krypto, other = randomize_stock_values()
    all_stocks = {}
    all_stocks.update(stocks)
    all_stocks.update(krypto)
    all_stocks.update(other)

    show_player_stocks()

    player_stocks_valued = {player_stock: all_stocks[player_stock] for player_stock in player_stocks}

    player_stocks_keys = player_stocks_valued.keys()
    player_stocks_values = player_stocks_valued.values()

    input('So vill sind die grad wert:\n ')

    print()
    for player_stock_key, player_stock_value in zip(player_stocks_keys, player_stocks_values):
        print(f'{player_stock_key}: CHF {player_stock_value}')

    continue_selling = input_selection(['y', 'n'], ['Ja', 'Nei'], '\nWetsch immerno verchaufe? ')
    if continue_selling == 'n':
        bank()

    selected_stock = select_stock(player_stocks_valued)
    selected_stock_value = player_stocks_valued[selected_stock]

    input(f'{selected_stock} hät en momentane Marktwert vo CHF {selected_stock_value}')

    stock_occurrences = count_stocks(player_stocks)
    selected_stock_quantity = stock_occurrences[selected_stock]

    while True:
        sell_quantity = input_int('Wieviel ' + selected_stock + ' wetsch du verchaufe? > ')
        if selected_stock_quantity < sell_quantity:
            print(f'Du häsch nume {selected_stock_quantity} {selected_stock}')
        else:
            total_selling_value = sell_quantity * selected_stock_value
            sell_confirmation = input_selection(['y', 'n'], ['Ja', 'Nei'],
                                                'Bisch du dir sicher, dass du ' + str(sell_quantity) +
                                                ' ' + selected_stock + ' für ' + str(
                                                    total_selling_value) + ' verchaufe wetsch? ')
            if sell_confirmation == 'y':
                break
            if sell_confirmation == 'n':
                sell_stock()  # go back to selling terminal

    for i in range(sell_quantity):
        player_stocks.remove(selected_stock)

    player.balance += total_selling_value

    input(f'Du häsch {sell_quantity} {selected_stock} für je CHF {selected_stock_value} verchauft, ')
    input(f'dim Konto sind CHF {total_selling_value} guetgschribe worde. ')

    bank()


def show_player_stocks():
    stock_occurrences = count_stocks(player_stocks)

    stock_names = stock_occurrences.keys()
    stock_quantities = stock_occurrences.values()

    print('\nDas sind dini Aktie: ')
    for stock, quantity in zip(stock_names, stock_quantities):
        print(f'{stock}: {quantity}')

    input()


def count_stocks(stock_list):
    unique_stocks = []
    for stock in stock_list:
        if stock not in unique_stocks:
            unique_stocks.append(stock)

    stock_occurrences = {stock: stock_list.count(stock) for stock in unique_stocks}

    return stock_occurrences


def randomize_stock_values():
    stocks = {'Tesla': randint(100, 150),
              'Microsoft': randint(250, 300),
              'Gamestop': randint(5, 100)
              }

    krypto = {'Bitcoin': randint(15000, 50000),
              'Ethereum': randint(1000, 4000),
              'Dogecoin': randint(1, 10)
              }

    other = {'Weed': randint(10, 15),
             'Kokain': randint(50, 200),
             'Crack': randint(60, 100)
             }

    return stocks, krypto, other


# -------------- investing ------------------


def heist():
    heist_mode = input_selection(['a', 's', 'c'], ['Aggressiv', 'Stealth', 'Chaotisch'],
                                 'Wie wetsch du de Überfall durefüehre?')
    if heist_mode == 'a':
        success_chance = heist_preparation('a')
    elif heist_mode == 's':
        success_chance = heist_preparation('s')
    elif heist_mode == 'c':
        success_chance = heist_preparation('c')
    else:
        success_chance = None

    heist_success = evaluate_heist_success(success_chance)
    if heist_success:
        reward = randint(500, 10000)
        player.balance += reward
        input(f'Din Überfall isch erfolgrich gsi und du häsch CHF {reward} gchlaut. ')
    else:
        input("Du häsch din Überfall schlimm verkackt, häsch aber chöne abhaue. ")


def evaluate_heist_success(success_chance):
    random = randint(1, 100)
    success_array = list(range(1, success_chance))
    if random in success_array:
        heist_success = True
    else:
        heist_success = False

    return heist_success


def heist_preparation(heist_mode):
    allowed_items = []
    if heist_mode == 'a':
        allowed_categories = ['rifle', 'assault rifle']
        for item in all_items:
            if item in player_inventory and (item.category in allowed_categories
                                             or item.top_level_category == 'explosive'):
                allowed_items.append(item)

        print()
        input('Du häsch dich dezue entschide, de Überfall aggressiv durezfüehre.')
        input("Was für Items wetsch für de überfall opfere? (je höcher s'Level vom Item, desto besser dini Chance.) ")

    if heist_mode == 's':
        allowed_categories = ['handgun']

        for item in all_items:
            if item in player_inventory and (item.category in allowed_categories):
                allowed_items.append(item)

        print()
        input('Du häsch dich dezue entschide, de Überfall Stealthig durezfüehre.')
        input("Was für Items wetsch für de überfall opfere? (je höcher s'Level vom Item, desto besser dini Chance.) ")

    if heist_mode == 'c':
        allowed_categories = ['meme']

        for item in all_items:
            if item in player_inventory and (item.category in allowed_categories):
                allowed_items.append(item)

        if not allowed_items:
            input('Du bsitzisch keis erlaubts Item für die Überfallsart. ')
            heist()

        print()
        input('Du häsch dich dezue entschide, de Überfall Chaotisch durezfüehre.')
        input("Was für Items wetsch für de überfall opfere? (je höcher s'Level vom Item, desto besser dini Chance.) ")

    heist_items = []
    while True:
        selected_item = select_item(allowed_items)
        player_inventory.remove(selected_item)
        allowed_items.remove(selected_item)
        heist_items.append(selected_item)
        continue_item_selection = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Wetsch du witeri Items mitneh? ')
        if continue_item_selection == 'n':
            break
        if not allowed_items:
            input('Du häsch kei vverfüegbari Items meh zum mitneh. ')
            break

    print()
    print('Folgendi Items opferisch du für de Heist: ')
    for item in heist_items:
        print(f'{item.name}  -  Level {item.req_skill_lv}')
    input()
    heist_items_quantity = 0
    heist_items_level_sum = 0
    for item in heist_items:
        heist_items_quantity += 1
        heist_items_level_sum += item.req_skill_lv

    success_chance_percent = heist_items_level_sum * heist_items_quantity

    print(f'Dini momentani Erfolgschance lit bi {success_chance_percent} %. ')
    confirmation = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Wetsch du de Überfall würklich durefüehre? ')
    if confirmation == 'n':
        bank()

    return success_chance_percent


# --------------------------------------------- bank ---------------------------------------------

# --------------------------------------------- game -------------------------------------------

@dataclass
class DiniMueter:
    mass: int
    health: int
    mood: int
    anger: int
    boredom: int
    confusion: int

    def __str__(self):
        return (f'Masse: {self.mass}'
                f'\nGsundheit: {self.health} \nStimmig: {self.mood} '
                f'\nHässigkeit: {self.anger} \nLangwiili: {self.boredom}'
                f'\nVerwirrtheit: {self.confusion}')


def initialize_dm():
    """
    initializes all DM properties to a random value in given intervals
    :return:
    """
    print('initialize_dm() is being executed')
    dm_mass, dm_health, dm_mood, dm_anger, dm_boredom, dm_confusion = randomize_dm_properties()
    new_dini_mueter = DiniMueter(dm_mass, dm_health, dm_mood, dm_anger, dm_boredom, dm_confusion)

    return new_dini_mueter


def randomize_dm_properties():
    """
    randomizes DM properties on an given interval
    :return dm properties:
    """
    print('randomize_dm_properties() is being executed')
    import random
    dm_mass = random.randint(100, 250)
    dm_health = random.randint(40, 100)
    dm_mood = random.randint(40, 100)
    dm_anger = random.randint(1, 50)
    dm_boredom = random.randint(1, 50)
    dm_confusion = random.randint(1, 20)

    return dm_mass, dm_health, dm_mood, dm_anger, dm_boredom, dm_confusion


def show_dm_properties(dini_mueter, show_influence, used_item):
    print()
    if show_influence and used_item is not None:
        if used_item.infl_mass >= 0:
            print(f'Masse: {dini_mueter.mass} Kg  (+ {used_item.infl_mass})')
        else:
            print(f'Masse: {dini_mueter.mass} Kg  ({used_item.infl_mass})')
        if used_item.infl_health >= 0:
            print(f'Gsundheit: {dini_mueter.health} HP  (+ {used_item.infl_health})')
        else:
            print(f'Gsundheit: {dini_mueter.health} HP  ({used_item.infl_health})')
        if used_item.infl_mood >= 0:
            print(f'Stimmig: {dini_mueter.mood} MP  (+ {used_item.infl_mood})')
        else:
            print(f'Stimmig: {dini_mueter.mood} MP  ({used_item.infl_mood})')
        if used_item.infl_anger >= 0:
            print(f'Hässigkeit: {dini_mueter.anger} AP  (+ {used_item.infl_anger})')
        else:
            print(f'Hässigkeit: {dini_mueter.anger} AP  ({used_item.infl_anger})')
        if used_item.infl_boredom >= 0:
            print(f'Langwili: {dini_mueter.boredom} BP  (+ {used_item.infl_boredom})')
        else:
            print(f'Langwili: {dini_mueter.boredom} BP  ({used_item.infl_boredom})')
        if used_item.infl_confusion >= 0:
            print(f'Verwirrtheit: {dini_mueter.confusion} CP  (+ {used_item.infl_confusion})')
        else:
            print(f'Verwirrtheit: {dini_mueter.confusion} CP  ({used_item.infl_confusion})')
        input()
    elif not show_influence or used_item is None:
        print(f'Masse: {dini_mueter.mass} Kg')
        print(f'Gsundheit: {dini_mueter.health} HP')
        print(f'Stimmig: {dini_mueter.mood} MP')
        print(f'Hässigkeit: {dini_mueter.anger} AP')
        print(f'Langwili: {dini_mueter.boredom} BP')
        print(f'Verwirrtheit: {dini_mueter.confusion} CP')
        input()
    else:
        input('ERROR in show_dm_properties()')


def calculate_dm_prop_infl(dini_mueter, used_item):
    dini_mueter.mass += used_item.infl_mass
    dini_mueter.health += used_item.infl_health
    dini_mueter.mood += used_item.infl_mood
    dini_mueter.anger += used_item.infl_anger
    dini_mueter.boredom += used_item.infl_boredom
    dini_mueter.confusion += used_item.infl_confusion

    dini_mueter = DiniMueter(dini_mueter.mass, dini_mueter.health, dini_mueter.mood, dini_mueter.anger,
                             dini_mueter.boredom, dini_mueter.confusion)

    return dini_mueter


def handle_critical_dm_property(death_messages, player_xp_change):

    messages_count = 0
    for message in death_messages:
        if message:  # just to make PyCharm happy
            messages_count += 1

    message = death_messages[randint(0, messages_count - 1)]

    input(message + ', rest in piss. ')

    if player_xp_change:
        player.xp += player_xp_change
        input(f'Du häsch {player_xp_change} XP becho. ')

    check_player_xp()

    user_selection = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Neui Mueter Spawne?')
    if user_selection == 'y':
        game()
    else:
        main_menu()


# --------------------------------------------- game -------------------------------------------
# ------------------------------------ main ----------------------------------------------------

def main():
    print('Willkomme zum Dini Mueter Simulator v3.0! (DEV Edition Alpha Phase)')
    main_menu()


def main_menu():
    user_selection = input_selection(['g', 's', 'b', 'i', 'l', 'ch', 'c', 'x'],
                                     ['Game Starte', 'Shop', 'Bank', 'Inventar', 'Level ahzeige', 'Cheat Code igeh',
                                      'Credits', 'Beände'], '\nWas wetsch du mache?  ')
    if user_selection == 'g':
        game()
    if user_selection == 's':
        shop()
    if user_selection == 'b':
        bank()
    if user_selection == 'i':
        show_player_inventory()
    if user_selection == 'l':
        print_skill_lv_bar()
        print()
        input()
        main_menu()  # I know, I know
    if user_selection == 'ch':
        enter_cheat_code()
    if user_selection == 'c':
        play_credits()
    if user_selection == 'x':
        user_cofirmation = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Bisch der sicher? ')
        if user_cofirmation == 'y':
            end_program(optional_message=None)
        else:
            main_menu()   # ja, ja ich weiss gopfedammi


def bank():
    user_selection = ''
    while user_selection != 'x':
        user_selection = input_selection(['k', 'i', 'u', 'm', 'x'],
                                         ['Kontostand ahzeige', 'Investiere', 'Usraube', 'Mini Aktie', 'Bank verlah'],
                                         '\nWillkomme i de Bank, was wetsch du mache? ')
        if user_selection == 'k':
            if player.balance < 100:
                input(f'Din momentane Kontostand isch: {player.balance} Stutz. (Das heisst du bisch broke.)')
            elif player.balance >= 100:
                input(f'Din momentane Kontostand isch: {player.balance} Stutz. (Mach mer nüt, du Bonz.)')
            else:
                input('PLAYER BALANCE ERROR IN BANK()')

        if user_selection == 'i':
            invest()

        if user_selection == 'u':
            heist()

        if user_selection == 'm':
            show_player_stocks()

        if user_selection == 'x':
            main_menu()


def shop():
    user_selection = ''
    while user_selection != 'x':
        user_selection = input_selection(['c', 's', 'x'], ['Chaufe', 'Sortimänt', 'Shop verlah'],
                                         '\nWillkomme im Shop, was wetsch du mache?')
        if user_selection == 'c':
            buy_items()
        if user_selection == 's':
            items_shop = all_items
            compactness = input_selection(['a', 'k'], ['Alli Eigeschafte', 'Kompakt'], 'Was sött alles ahzeigt werde?')
            if compactness == 'a':
                show_items(items_shop, 'show all properties')
            if compactness == 'k':
                show_items(items_shop, 'show only names and price')

        if user_selection == 'x':
            main_menu()


def game():
    user_selection = ''
    while user_selection != 'x':
        user_selection = input_selection(['t', 'x'], ['test', 'exit'], 'willkomme i de testumgäbig vom GAME')
        if user_selection == 't':
            continue_playing = 'y'
            dini_mueter = initialize_dm()

            while continue_playing == 'y':
                print('Dinere Mueter gahts hütt so: ')

                show_dm_properties(dini_mueter, False, used_item=None)
                print('Was wetsch du uf sie ahwände? ')
                selected_item = select_item(player_inventory)
                print(f'Du wändisch {selected_item.name} ah')

                dini_mueter = calculate_dm_prop_infl(dini_mueter, used_item=selected_item)

                if dini_mueter.health <= 0:
                    death_messages = ['Dini Mueter isch gstorbe', 'Dini mueter hät is Gras bisse',
                                      'Dini Mueter isch verreckt',
                                      "D'Existänz vo dinere mueter isch brutal beändet worde",
                                      'Dini Mueter isch terminiert worde',
                                      ]
                    handle_critical_dm_property(death_messages, player_xp_change=20)

                elif dini_mueter.mood <= 0:
                    death_messages = ['Dini Mueter hät sich umbracht', 'Dini Mueter hät sich erhängt',
                                      'Dini Mueter hätt sich mit emne Toaster grilliert',
                                      'Dini Mueter hät sich de Chopf mit Blei vollpumpt',
                                      'Dini Mueter isch vonere Brugg gumbet',
                                      'Dini Mueter hätt sich im zurüsee ertränkt'
                                      ]
                    handle_critical_dm_property(death_messages, player_xp_change=15)

                elif dini_mueter.mass <= 0:
                    death_messages = ['Dini Mueter isch verfettet und amne Herzinfakt gtorbe',
                                      'Dini Mueter isch zu fett worde und kollabiert',
                                      'Dini Mueter isch so fett worde, sie isch en Berg abegrollt und gtorbe',
                                      'Us dinere Mueter isch es schwarzes Loch entstande']
                    handle_critical_dm_property(death_messages, player_xp_change=10)

                elif dini_mueter.anger >= 100:
                    input('Dini Mueter isch ab jetzt huere hässig. ')
                    # TODO: consequences for critical secondary DM properties
                elif dini_mueter.boredom >= 100:
                    input('Diniere Mueter isch es huere langwiilig. ')
                elif dini_mueter.confusion >= 100:
                    input('Dini Mueter isch hert verwirrt. ')

                input('Enter drucke zum Status überprüefe')
                show_dm_properties(dini_mueter, True, used_item=selected_item)

                continue_playing = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Wetsch wiitermache? ')
                if continue_playing == 'y':
                    pass
                if continue_playing == 'x':
                    main_menu()

        if user_selection == 'x':
            main_menu()


def enter_cheat_code():

    user_cheat_code = input('Gib de Cheat Code ih (illegal) > ')

    if user_cheat_code == 'DERYANISCHFETT':
        player.balance += 1000
        input("Cheat Code aktiviert - Dim Konto sind CHF 1'000 guetgschribe worde. ")

    elif user_cheat_code == 'SHREKISCHLIEBISHREKISCHLÄBE':
        player.xp += 10000
        input("Cheat Code aktiviert - Du häsch 10'000 XP becho. ")
        check_player_xp()

    elif user_cheat_code == '3.141592654':
        for i in range(100):
            player_stocks.append('Tesla')
        input('Cheat Code aktiviert - Du häsch 100 Tesla Aktie becho. ')

    elif user_cheat_code == 'DINIFETTIMUETER':
        pass

    elif user_cheat_code == '420':
        for i in range(1000):
            player_stocks.append('Weed')
        input('Cheat Code aktiviert - Du häsch 1 Kg Weed becho. ')

    elif user_cheat_code == 'TRUPP26':
        player_inventory.append(item_secret_firedragon)
        input('Cheat Code aktiviert - Du häsch de geheimi Fürdrache becho!!!!!!!')

    elif user_cheat_code == 'DEFYNNISCHENSPAST':
        player.balance += 10
        input('Cheat Code aktiviert - True dis, da häsch 10 Stutz. ')

    else:
        end_program('De Cheat Code gits nöd, du döfsch nüme spile. ')

    main_menu()


def play_credits():
    from time import sleep
    print('  ---- Dini Mueter Simulator v3.0 ----')
    sleep(1)
    print()
    print('           -- Entwicklig -- ')
    print()
    sleep(1)
    print('Projektleiter:        Jan Atzgerstorfer')
    sleep(1)
    print('Lead Entwickler:      Jan Atzgerstorfer')
    sleep(1)
    print('Gameplay Entwickler:  Jan Atzgerstorfer')
    sleep(1)
    print('UI Entwickler:        Jan Atzgerstorfer')
    sleep(1)
    print()
    print('             -- Design --')
    print()
    sleep(1)
    print('Lead Designer:        Jan Atzgerstorfer')
    sleep(1)
    print('Gameplay Designer:    Jan Atzgerstorfer')
    sleep(1)
    print('UI Designer:          Jan Atzgerstorfer')
    sleep(1)
    print('UX Designer:          Jan Atzgerstorfer')
    sleep(1)
    print()
    print('             -- Story --')
    print()
    print('Idee:                 Rafael Banz')
    sleep(1)
    print('Konzept:              Jan Atzgerstorfer')
    sleep(1)
    print()
    print('          -- Atzgerware Ltd. --')
    print()
    sleep(1)
    print('CEO:                  Jan Atzgerstorfer')
    sleep(1)
    print('')

    main_menu()


def end_program(optional_message):
    from datetime import datetime
    now = datetime.now()
    current_year = now.year
    if optional_message is not None:
        input(optional_message)
        input(f'© {current_year} Atzgerware Ltd. - Alli Rächt vorbehalte (mis Programm) ')
        exit()
    else:
        input('Danke, dass du de Dini Mueter Simulator v3.0 gsillt häsch. ')
        input(f'© {current_year} Atzgerware Ltd. - Alli Rächt vorbehalte (mis Programm) ')
        exit()

add_achievement(achievement_4)
show_player_achievements()
# ------------------------------------ main ----------------------------------------------------
