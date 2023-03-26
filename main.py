# --------------------------------------- global resources -----------------------------------------------
from datetime import datetime, timedelta
import os
from random import randint
from dataclasses import dataclass

from colours import *
from player import Player
from item import find_item, initialize_items
import csv

# --------- item stuff ----------------


all_items = initialize_items()

# --------- item stuff ----------------

# --------- player stuff --------


player = Player(skill_lv=1, xp=90, balance=500.0,
                inventory=find_item('id', ['colt_m1911', 'm16a1', 'rpg_7', 'medkit']),
                stocks=['Microsoft', 'Microsoft', 'Tesla', 'Bitcoin'],
                achievements=[],
                data_game={'killed_mothers': 0,
                           'damage_dealt': 0,
                           'playtime': timedelta()
                           },
                data_items={'purchased_items_firearm': 0,
                            'purchased_items_explosive': 0,
                            'purchased_items_consumable': 0,
                            'purchased_items_videogame': 0,
                            'purchased_items_meme': 0
                            },
                data_financial={'total_spendings': 0,
                                'total_earnings': 0,
                                'purchased_stocks': 0,
                                'purchased_crypto': 0
                                },
                data_misc={'invalid inputs': 0,
                           'entered cheat codes': 0,
                           },
                data_translations={'killed_mothers': 'Killti Müetere',
                                   'damage_dealt': 'Verursachte Schade',
                                   'playtime': 'Spilziit',

                                   'purchased_items_firearm': 'Gkaufti Schusswaffe',
                                   'purchased_items_explosive': 'Gkaufte Sprängstoff',
                                   'purchased_items_consumable': 'Gkaufti Konsumware',
                                   'purchased_items_videogame': 'Gkaufti Videospiel Items',
                                   'purchased_items_meme': 'Gkaufti Meme Items',

                                   'total_spendings': 'Usgabe total',
                                   'total_earnings': 'Ihname total',
                                   'purchased_stocks': 'Gkaufti Aktie',
                                   'purchased_crypto': 'Gkaufts Krypto'
                                   }
                )


# --------- player stuff ------
# --------- player data -------


def check_player_data():
    # input('check_player_data()')
    if player.data_game['killed_mothers'] == 1:
        player.add_achievement(3)
    if player.data_financial['purchased_stocks'] == 1:
        player.add_achievement(5)
    if player.data_items['purchased_items_meme'] == 1:
        player.add_achievement(6)

    new_achievements_earned = False
    for achievement in player.achievements:
        if achievement.status == 'new':
            new_achievements_earned = True

    if new_achievements_earned:
        show_player_achievements('new')


time_start = datetime.now()


def count_playtime():
    playtime = datetime.now() - time_start
    player.data_game['playtime'] = playtime
    print(f'Spilziit: {playtime}')


# --------- achievement stuff ---------


# --------- achievement stuff ---------
# --------------------------------------- global resources -----------------------------------------------
# --------------------------------------------- input -------------------------------------------

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


# ----------------------------------------------- input ------------------------------------------------
# ----------------------------------------------- saves ------------------------------------------------

def initialize_save_dir():
    if not os.path.exists('saves'):
        os.mkdir('saves')


def save_game(name=f'{datetime.now().day}-{datetime.now().month}-{datetime.now().year}'):
    save_file_path = f'saves/{name}.csv'
    attributes = ['key', 'value']

    old_values = []
    if os.path.exists(save_file_path):
        with open(save_file_path, 'r', encoding='utf-8') as csv_file:
            dict_reader = csv.DictReader(csv_file, fieldnames=attributes)
            next(csv_file)
            for line in dict_reader:
                old_values.append(line)
    else:
        with open(save_file_path, 'w', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=attributes)
            csv_writer.writeheader()

    with open(save_file_path, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=attributes)
        csv_writer.writeheader()

        csv_writer.writerow({'key': 'skill_lv', 'value': player.skill_lv})
        csv_writer.writerow({'key': 'xp', 'value': player.xp})
        csv_writer.writerow({'key': 'balance', 'value': player.balance})
        for item in player.inventory:
            csv_writer.writerow({'key': 'item', 'value': item.id})
        for stock in player.stocks:
            csv_writer.writerow({'key': 'stock', 'value': stock})
        for achievement in player.achievements:
            csv_writer.writerow({'key': 'achievement', 'value': achievement.id})


def validate_save_filename(filename: str) -> bool:
    # if os.path.exists(f'saves/{filename}.csv'):
    #     print('Das file gits scho. ')
    #     return False
    if filename == '':
        print('Das isch kein gültige Dateiname. ')
    #  return False
    invalid_chars = [' ', '.', '/', '%', '|', ',', "'", '"']
    for char in invalid_chars:
        if char in filename:
            print(f'De name döf nöd "{char}" enthalte. ')
            return False
    return True


def enter_filename() -> str:
    filename_invalid = True
    filename = None
    while filename_invalid:
        filename = input('Gib en Dateiname ih > ')
        if validate_save_filename(filename):
            filename_invalid = False

    return filename


def load_save_file(filename):
    with open(f'saves/{filename}.csv', 'r', encoding='utf-8') as csv_file:
        next(csv_file)
        attributes = ['key', 'value']
        csv_reader = csv.DictReader(csv_file, fieldnames=attributes)
        for line in csv_reader:
            key = line['key']
            value = line['value']
            if key == 'skill_lv':
                player.skill_lv = int(value)
            if key == 'xp':
                player.xp = int(value)
            if key == 'balance':
                player.balance = float(value)
            if key == 'item':
                if not check_item_occurrence(value, 'player_inventory'):
                    player.add_item(find_item('id', [value]))
            if key == 'stock':
                player.stocks.append(value)
    print_success(f'De Spielstand "{filename}" isch erfolgrich glade worde. ')
    input()
    main_menu()


def save_game_ui():
    user_selection = input_selection(['e', 'n'], ['Exisierende Spielstand', 'Neui Datei'],
                                     'Wo wetsch du dis Spiel speichere? ')
    if user_selection == 'e':
        selected_file = select_save_file()
        selected_file = remove_filetype(selected_file)
        save_game(selected_file)
        print_success(f'De Spielstand "{selected_file}" isch erfolrich gspeichered worde. ')
        input()
    else:
        filename = enter_filename()
        if os.path.exists(f'saves/{filename}.csv'):
            user_selection = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Die Datei gits scho, wetsch si überschribe? ')
            if user_selection == 'y':
                os.remove(f'saves{filename}.csv')
                save_game(filename)
                print_success(f'De Spielstand "{filename}" isch erfolrich gspeichered worde. ')
                input()
            else:
                main_menu()
        else:
            save_game(filename)
            print_success(f'De Spielstand "{filename}" isch erfolrich gspeichered worde. ')
            input()
    main_menu()


def list_save_files() -> list:
    for index, file in enumerate(os.listdir('saves')):
        print(f'{index}\t{file}')

    return os.listdir('saves')


def select_save_file() -> str:
    files = list_save_files()
    while True:
        user_index = input_int('I welli Datei wetsch du speichere? ')
        try:
            selected_file = files[user_index]
        except IndexError:
            print('Das isch e ungültigi Uswahl. ')
        else:
            return selected_file


def remove_filetype(filename) -> str:
    str_tuple = filename.partition('.')
    str_list = list(str_tuple)
    str_list.pop(-1)
    str_list.pop(-1)
    filename = ''.join(str_list)
    return filename


initialize_save_dir()


# ----------------------------------------------- saves ------------------------------------------------


# --------------------------------------------- items ------------------------------------------

def show_items(item_list, printed_properties):
    """
    prints all items
    :param printed_properties:
    :param item_list:
    should be printed
    :return: none
    """
    # print('show_items() is being executed')
    if printed_properties == 'show all properties':
        for item in item_list:
            print('--------------------------')
            print(item)
            print('--------------------------')
            input()
    elif printed_properties == 'show only names':
        for item in item_list:
            print(f'Nr. {item_list.index(item)}: {item.name}')
        input()
    elif printed_properties == 'show only names and price':
        for item in item_list:
            print(f'Nr. {item_list.index(item)}: {item.name}  CHF {item.price}')
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
            os.system('cls')
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
            os.system('cls')
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
            os.system('cls')
            break

    return selected_item


def check_item_occurrence(target_id, scope):
    if scope not in ['all_items', 'player_inventory']:
        raise ValueError(f'Invalid scope "{scope}" given. ')
    if scope == 'all_items':
        for item in all_items:
            if item.id == target_id:
                return True
    elif scope == 'player_inventory':
        for item in player.inventory:
            if item.id == target_id:
                return True
    return False


# --------------------------------------------- items ------------------------------------------
# -------------------------------------------- player ------------------------------------------


def show_player_inventory():
    # print('show_player_inventory() 3 executed')
    compactness = ''
    while compactness != 'x':
        compactness = input_selection(['a', 'k', 'x'], ['Alli Eigeschafte', 'Kompakt', 'zrugg zum Hauptmenü'],
                                      'Was sött alles ahzeigt werde?')
        if compactness == 'a':
            show_items(player.inventory, 'show all properties')
        if compactness == 'k':
            show_items(player.inventory, 'show only names')
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
def show_player_achievements(achievement_status):
    if achievement_status == 'old':
        if player.achievements:
            for achievement in player.achievements:
                if achievement.status == 'old':
                    print()
                    print(f'-- {achievement.name} -- ')
                    print(f'{achievement.description}')
                    print(f'Verdient: {achievement.time_earned_formatted}')
                    print(f'CHF {achievement.reward}')
                    input()
        else:
            input('Du häsch no kei Achievements verdient, du Noob. ')

    elif achievement_status == 'new':
        for achievement in player.achievements:
            if achievement.status == 'new':
                print('---------------------')
                print('  Neus Achievement! ')
                print(achievement)
                print('---------------------')
                # input()

        for achievement in player.achievements:
            if achievement.status == 'new':
                achievement.status = 'old'

    else:
        input('invalid argument given when called show_player_achievements(). ')
    main_menu()


# -------------------------------------------- achievements ------------------------------------------
# -------------------------------------------- statistics ------------------------------------------
def show_player_statistics():
    user_selection = input_selection(['g', 'i', 'f'], ['Game Statistik', 'Item Statistik', 'Finanzielli Statistik'],
                                     'Welli Statistik wetsch du ahluege?')
    try:
        if user_selection == 'g':
            for key, value in player.data_game.items():
                print(f'{player.data_translations[key]}: {value}')
        if user_selection == 'i':
            for key, value in player.data_items.items():
                print(f'{player.data_translations[key]}: {value}')
        if user_selection == 'f':
            for key, value in player.data_financial.items():
                print(f'{player.data_translations[key]}: {value}')
            gross_profit = player.data_financial['total_earnings'] - player.data_financial['total_spendings']
            try:
                gross_profti_ratio = gross_profit * 100 / player.data_financial['total_earnings']
            except ZeroDivisionError:
                gross_profti_ratio = 'N/A'
                print(f'\nBruttgwünn: CHF {gross_profit}\nBruttogwünnquote: {gross_profti_ratio}')
            else:
                gross_profti_ratio = round(gross_profti_ratio, 2)
                print(f'\nBruttgwünn: CHF {gross_profit}\nBruttogwünnquote: {gross_profti_ratio}%')

    except KeyError:
        input('KeyError in show_player_statistics(), probably translation error. check player_data_translations for '
              'debugging. ')

    input()
    main_menu()


# -------------------------------------------- statistics ------------------------------------------

# --------------------------------------------- shop --------------------------------------------


def buy_items():
    # print('buy_items() is being executed')
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
        player.add_item(selected_item)
        input(f'{selected_item.name} isch dim Inventar hinzuegfüegt worde. ')
        transact_money(-selected_item.price)
        input(f'{selected_item.price} Stutz sind dim Konto abzoge worde. ')


# --------------------------------------------- shop --------------------------------------------

# --------------------------------------------- bank ---------------------------------------------
# -------------- transaction ------------------
def transact_money(amount):
    player.balance += amount
    if amount >= 0:
        player.data_financial['total_earnings'] += amount
    else:
        player.data_financial['total_spendings'] -= amount  # total amount should be shown positive in statistics


# -------------- transaction ------------------

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
        player.stocks.append(selected_stock_key)

    transact_money(-total_stock_price)

    print(f'Du häsch {stock_quantity} {selected_stock_key} für je CHF {selected_stock_price} gkauft. ')
    input(f'Dim Konto sind CHF {total_stock_price} abzoge worde.')

    if selected_stock_key in ['Microsoft', 'Tesla', 'Gamestop']:
        player.data_financial['purchased_stocks'] += stock_quantity
    if selected_stock_key in ['Bitcoin', 'Ethereum', 'Dogecoin']:  # permanent temporary solution
        player.data_financial['purchased_crypto'] += stock_quantity

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

    player_stocks_valued = {player_stock: all_stocks[player_stock] for player_stock in player.stocks}

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

    stock_occurrences = count_stocks(player.stocks)
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
        player.stocks.remove(selected_stock)

    transact_money(total_selling_value)

    input(f'Du häsch {sell_quantity} {selected_stock} für je CHF {selected_stock_value} verchauft, ')
    input(f'dim Konto sind CHF {total_selling_value} guetgschribe worde. ')

    bank()


def show_player_stocks():
    stock_occurrences = count_stocks(player.stocks)

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
        transact_money(reward)
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
            if item in player.inventory and (item.category in allowed_categories
                                             or item.top_level_category == 'explosive'):
                allowed_items.append(item)

        print()
        input('Du häsch dich dezue entschide, de Überfall aggressiv durezfüehre.')
        input("Was für Items wetsch für de überfall opfere? (je höcher s'Level vom Item, desto besser dini Chance.) ")

    if heist_mode == 's':
        allowed_categories = ['handgun']

        for item in all_items:
            if item in player.inventory and (item.category in allowed_categories):
                allowed_items.append(item)

        print()
        input('Du häsch dich dezue entschide, de Überfall Stealthig durezfüehre.')
        input("Was für Items wetsch für de überfall opfere? (je höcher s'Level vom Item, desto besser dini Chance.) ")

    if heist_mode == 'c':
        allowed_categories = ['meme']

        for item in all_items:
            if item in player.inventory and (item.category in allowed_categories):
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
        player.inventory.remove(selected_item)
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
# --------------------------------------------- casino ---------------------------------------------
def roulette():
    user_selection = None
    user_nr = None
    user_odd_or_even = None
    user_colour = None
    while user_selection != 'x':
        user_selection = input_selection(['f', 'g', 'z', 's', 'x'],
                                         ['Farb', 'Grad/Ungrad', 'Zahl', 'Spile', 'Roulette verlah'],
                                         'Uf was wetsch du setze? ')
        if user_selection == 'f':
            user_colour = input_selection(['r', 'f'], ['Rot', 'Schwarz'], 'Uf welli Zahl wetsch du setze? ')
        if user_selection == 'g':
            user_odd_or_even = input_selection(['g', 'u'], ['Grad', 'Ungrad'], 'Grad oder ungrad? ')
        if user_selection == 'z':
            nr_invalid = True
            while nr_invalid:
                user_nr = input_int('Uf welli Zahl wetsch du setze? ')
                if 0 < user_nr < 36:
                    print('Die Zahl isch ungütig, du Depp. ')
                else:
                    nr_invalid = False
        if user_selection == 's':
            break
        if user_selection == 'x':
            casino()

    user_bet = None
    bet_invalid = True
    while bet_invalid:
        user_bet = input_int('Wievill wetsch du setze? ')
        if user_bet < 0 or user_bet > player.balance:
            print('Das isch en ungültige Betrag. ')
        else:
            bet_invalid = False

    number = randint(0, 36)

    number_odd_even = None
    if number != 0:
        if number % 2 == 0:
            number_odd_even = 'g'
        else:
            number_odd_even = 'u'

    colour = None
    if number == 0:
        colour = 'g'
    elif 1 <= number >= 10 or 19 <= number >= 28:
        if number % 2 == 0:
            colour = 'b'
        else:
            colour = 'r'
    elif 11 <= number >= 18 or 26 <= number >= 36:
        if number % 2 == 0:
            colour = 'r'
        else:
            colour = 'b'

    if colour == 'r':
        print(f"D'Dahl {number} (ROT) isch zoge worde. ")
    elif colour == 'b':
        print(f"D'Dahl {number} (SCHWARZ) isch zoge worde. ")
    else:
        print(f"D'Dahl {number} (GRÜEN) isch zoge worde. ")

    win = None
    if user_nr == number:
        win = user_bet * 36
    if user_colour == colour:
        win = user_bet * 2
    if user_odd_or_even == number_odd_even:
        win = user_bet * 2

    transact_money(-user_bet)

    if win:
        transact_money(user_bet * 36)
        input(f'Du häsch CHF {win} gwunne! ')
    roulette()


# --------------------------------------------- casino ---------------------------------------------


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

    def randomize_properties(self):
        """
        randomizes DM properties on an given interval
        :return dm properties:
        """
        import random
        self.mass = random.randint(100, 250)
        self.health = random.randint(40, 100)
        self.mood = random.randint(40, 100)
        self.anger = random.randint(1, 50)
        self.boredom = random.randint(1, 50)
        self.confusion = random.randint(1, 20)

        return self.mass, self.health, self.mood, self.anger, self.boredom, self.confusion

    def calculate_prop_infl(self, used_item):
        self.mass += used_item.infl_mass
        self.health += used_item.infl_health
        self.mood += used_item.infl_mood
        self.anger += used_item.infl_anger
        self.boredom += used_item.infl_boredom
        self.confusion += used_item.infl_confusion

        dini_mueter = DiniMueter(self.mass, self.health, self.mood, self.anger,
                                 self.boredom, self.confusion)

        return dini_mueter

    def show_properties(self, show_influence, used_item):
        print()
        if show_influence and used_item is not None:
            if used_item.infl_mass >= 0:
                print(f'Masse: {self.mass} Kg   ', end='')
                print_green(f'(+ {used_item.infl_mass})')
            else:
                print(f'Masse: {self.mass} Kg  ', end='')
                print_red(f'({used_item.infl_mass})')
            if used_item.infl_health >= 0:
                print(f'Gsundheit: {self.health} HP  ', end='')
                print_green(f'(+ {used_item.infl_health})')
            else:
                print(f'Gsundheit: {self.health} HP  ', end='')
                print_red(f'({used_item.infl_health})')
            if used_item.infl_mood >= 0:
                print(f'Stimmig: {self.mood} MP  ', end='')
                print_green(f'(+ {used_item.infl_mood})')
            else:
                print(f'Stimmig: {self.mood} MP  ', end='')
                print_red(f'({used_item.infl_mood})')
            if used_item.infl_anger >= 0:
                print(f'Hässigkeit: {self.anger} AP  ', end='')
                print_green(f'(+ {used_item.infl_anger})')
            else:
                print(f'Hässigkeit: {self.anger} AP  ', end='')
                print_green(f'({used_item.infl_anger})')
            if used_item.infl_boredom >= 0:
                print(f'Langwili: {self.boredom} BP  ', end='')
                print_red(f'(+ {used_item.infl_boredom})')
            else:
                print(f'Langwili: {self.boredom} BP  ', end='')
                print_red(f'({used_item.infl_boredom})')
            if used_item.infl_confusion >= 0:
                print(f'Verwirrtheit: {self.confusion} CP  ', end='')
                print_green(f'(+ {used_item.infl_confusion})')
            else:
                print(f'Verwirrtheit: {self.confusion} CP  ', end='')
                print_red(f'({used_item.infl_confusion})')
            input()
        elif not show_influence or used_item is None:
            print(f'Masse: {self.mass} Kg')
            print(f'Gsundheit: {self.health} HP')
            print(f'Stimmig: {self.mood} MP')
            print(f'Hässigkeit: {self.anger} AP')
            print(f'Langwili: {self.boredom} BP')
            print(f'Verwirrtheit: {self.confusion} CP')
            input()
        else:
            input('ERROR in show_dm_properties()')


def initialize_dm():
    """
    initializes all DM properties to a random value in given intervals
    :return:
    """
    new_dini_mueter = DiniMueter(0, 0, 0, 0, 0, 0)
    new_dini_mueter.randomize_properties()
    return new_dini_mueter


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
    check_player_data()
    count_playtime()

    user_selection = input_selection(['g', 's', 'b', 'c', 'i', 'l', 'a', 'st', 'ch', 'c', 'sp', 'ld', 'x'],
                                     ['Game Starte', 'Shop', 'Bank', 'Casino', 'Inventar', 'Level ahzeige',
                                      'Achievements',
                                      'Statistike', 'Cheat Code igeh',
                                      'Credits', 'Spielstand Speichere', 'Spielstand Lade', 'Beände'],
                                     '\nWas wetsch du mache?  ')
    if user_selection == 'g':
        game()
    if user_selection == 's':
        shop()
    if user_selection == 'b':
        bank()
    if user_selection == 'c':
        casino()
    if user_selection == 'i':
        show_player_inventory()
    if user_selection == 'l':
        print_skill_lv_bar()
        print()
        input()
        main_menu()  # I know, I know
    if user_selection == 'a':
        show_player_achievements('old')
    if user_selection == 'st':
        show_player_statistics()
    if user_selection == 'ch':
        enter_cheat_code()
    if user_selection == 'c':
        play_credits()
    if user_selection == 'sp':
        save_game_ui()
    if user_selection == 'ld':
        filename = select_save_file()
        filename = remove_filetype(filename)
        load_save_file(filename)
    if user_selection == 'x':
        user_confirmation = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Bisch der sicher? ')
        if user_confirmation == 'y':
            end_program(optional_message=None)
        else:
            main_menu()  # ja, ja ich weiss gopfedammi


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


def casino():
    user_selection = None
    while user_selection != 'x':
        user_selection = input_selection(['r', 'x'], ['Roulette', 'Casino verlah'],
                                         '\nWillkomme im Casino, was wetsch du mache?')
        if user_selection == 'r':
            roulette()
        if user_selection == 'x':
            main_menu()


def game():
    user_selection = ''
    while user_selection != 'x':
        user_selection = input_selection(['t', 'x'], ['test', 'exit'], 'willkomme i de testumgäbig vom GAME')
        if user_selection == 't':
            os.system('cls')
            continue_playing = 'y'
            dini_mueter = initialize_dm()

            while continue_playing == 'y':
                print('Dinere Mueter gahts hütt so: ')

                dini_mueter.show_properties(False, used_item=None)
                print('Was wetsch du uf sie ahwände? ')
                selected_item = select_item(player.inventory)
                print(f'Du wändisch {selected_item.name} ah')

                dini_mueter.calculate_prop_infl(used_item=selected_item)

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
                dini_mueter.show_properties(True, used_item=selected_item)

                continue_playing = input_selection(['y', 'n'], ['Ja', 'Nei'], 'Wetsch wiitermache? ')
                if continue_playing == 'y':
                    os.system('cls')
                if continue_playing == 'x':
                    main_menu()

        if user_selection == 'x':
            main_menu()


def enter_cheat_code():
    user_cheat_code = input('Gib de Cheat Code ih (illegal) > ')

    if user_cheat_code == 'DERYANISCHFETT':
        transact_money(1000)
        input("Cheat Code aktiviert - Dim Konto sind CHF 1'000 guetgschribe worde. ")

    elif user_cheat_code == 'SHREKISCHLIEBISHREKISCHLÄBE':
        player.xp += 10000
        input("Cheat Code aktiviert - Du häsch 10'000 XP becho. ")
        check_player_xp()

    elif user_cheat_code == '3.141592654':
        for i in range(100):
            player.stocks.append('Tesla')
        input('Cheat Code aktiviert - Du häsch 100 Tesla Aktie becho. ')

    elif user_cheat_code == 'DINIFETTIMUETER':
        pass

    elif user_cheat_code == '420':
        for i in range(1000):
            player.stocks.append('Weed')
        input('Cheat Code aktiviert - Du häsch 1 Kg Weed becho. ')

    elif user_cheat_code == 'TRUPP26':
        item = find_item('id', ['secret_firedragon'])
        player.add_item(item)
        input('Cheat Code aktiviert - Du häsch de geheimi Fürdrache becho!!!!!!!')

    elif user_cheat_code == 'DEFYNNISCHENSPAST':
        transact_money(10)
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


main()

# ------------------------------------ main ----------------------------------------------------
