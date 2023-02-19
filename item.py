from dataclasses import dataclass


# --------- item stuff ----------------

@dataclass
class Item:
    id: str
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


def initialize_items():
    return [Item('colt_m1911', 'Colt M1911', 'firearm', 'handgun', 'E pistole halt', 20.0, 1, 0, -25, -25, 30, -40, 0),
            Item('mk1_frag_grenade', 'Mk.1 Splittergranate', 'explosive', 'anti personnel',
                 'Tätscht und verteilt Metall-Konfetti', 30.0, 1, 0, -50, -40, 40, -50, 0),
            Item('rpg_7', 'RPG-7', 'explosive', 'anti tank', 'Nöd hine ineluege', price=75.0, req_skill_lv=5,
                 infl_mass=-50,
                 infl_health=-50, infl_mood=-30, infl_anger=20, infl_boredom=-15, infl_confusion=0),
            Item('m16a1', 'M16A1', 'firearm', 'assault rifle', 'Wahre Klassiker', price=45.0, req_skill_lv=2,
                 infl_mass=0,
                 infl_health=-15, infl_mood=-10, infl_anger=20, infl_boredom=-15, infl_confusion=0),
            Item('m1_garand', 'M1 Garand', 'firearm', 'rifle', 'Tönt kuul bim Nahlade', price=20.0, req_skill_lv=2,
                 infl_mass=0, infl_health=-10, infl_mood=-10, infl_anger=15, infl_boredom=-15, infl_confusion=0),
            Item('m24', 'M24', 'firearm', 'rifle', 'De Siech isch scheisse lut aber fäggt', price=50.0, req_skill_lv=3,
                 infl_mass=0, infl_health=-35, infl_mood=-15, infl_anger=20, infl_boredom=-15, infl_confusion=0),
            Item('kar98k', 'Kar98k', 'firearm', 'rifle', 'Gar nöd eso churz', price=75.0, req_skill_lv=4,
                 infl_mass=0, infl_health=-25, infl_mood=-15, infl_anger=20, infl_boredom=-15, infl_confusion=0),
            Item('stg_44', 'StG 44', 'firearm', 'assault rifle', 'Ich han die imfall vergoldet in Battlefield V',
                 price=80.0,
                 req_skill_lv=4, infl_mass=0, infl_health=-20, infl_mood=-15, infl_anger=15, infl_boredom=-15,
                 infl_confusion=0),
            Item('glock_17', 'Glock 17', 'firearm', 'handgun', "D'Öschis wüssed wies gaht", price=40.0, req_skill_lv=5,
                 infl_mass=0, infl_health=-10, infl_mood=-10, infl_anger=15, infl_boredom=-15, infl_confusion=0),
            Item('medkit', 'Medikit', 'consumable', 'medical', 'Universale Hälfer', price=10.0, req_skill_lv=1,
                 infl_mass=0,
                 infl_health=30, infl_mood=20, infl_anger=-20, infl_boredom=0, infl_confusion=0),
            Item('diamond_pickaxe', 'Diamante Pickaxe', 'videogame', 'minecraft',
                 'Alte, mit dem chasch fucking Obsidian abbaue', price=100.0, req_skill_lv=10, infl_mass=-50,
                 infl_health=-50, infl_mood=-20, infl_anger=30, infl_boredom=0, infl_confusion=15),
            Item('secret_firedragon', 'De geheimi Fürdrache', 'meme', 'insider', 'Alte, er hätt de geheimi Fürdrache!',
                 price=10000.0, req_skill_lv=100, infl_mass=0, infl_health=-200, infl_mood=-150,
                 infl_anger=100,
                 infl_boredom=-100, infl_confusion=100),
            Item('anti_horny_bat', 'Anti-Hornig-Schleger', 'meme', 'classic', 'Gang is hornig-Gfängniss', price=20.0,
                 req_skill_lv=4, infl_mass=0, infl_health=-5, infl_mood=-20, infl_anger=30,
                 infl_boredom=0, infl_confusion=5)

            ]


all_items = initialize_items()


def find_item(search_criteria, search_term_list):
    found_items = []
    if search_criteria == 'id':
        for item in all_items:
            if item.id in search_term_list:
                found_items.append(item)

    elif search_criteria == 'top_level_category':
        for item in all_items:
            if item.top_level_category in search_term_list:
                found_items.append(item)

    elif search_criteria == 'category':
        for item in all_items:
            if item.category in search_term_list:
                found_items.append(item)

    elif search_criteria == 'req_skill_lv':
        for item in all_items:
            if item.req_skill_lv in search_term_list:
                found_items.append(item)

        else:
            input('invalid search criteria, check find_item() for debugging. ')

    found_items_quantity = 0
    for found_item in found_items:  # TODO: how about use len() here, you dumb fuck?
        found_items_quantity += 1

    if found_items_quantity > 1:  # you have no idea how long it took me to come up with this fix
        return found_items
    if found_items_quantity == 1:
        return found_items[0]


# --------- item stuff ----------------