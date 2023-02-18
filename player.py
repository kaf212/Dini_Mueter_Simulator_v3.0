from dataclasses import dataclass
from datetime import datetime
from item import initialize_items
from achievement import initialize_achievements
from item import Item, find_item

all_items = initialize_items()
all_achievements = initialize_achievements()

# --------- player stuff --------



@dataclass
class Player:
    skill_lv: int
    xp: int
    balance: float
    inventory: list
    stocks: list
    achievements: list
    data_game: dict
    data_items: dict
    data_financial: dict
    data_misc: dict
    data_translations: dict

    def add_item(self, item):
        if item in all_items:
            self.inventory.append(item)
        else:
            raise Exception(f'Tried adding invalid item "{item}", you dumb fuck. ')

    def add_achievement(self, achievement_id):
        player_achievements_ids = []
        for achievement in self.achievements:
            player_achievements_ids.append(achievement.id)

        if achievement_id not in player_achievements_ids:
            added_achievement = None
            for achievement in all_achievements:
                if achievement.id == achievement_id:
                    added_achievement = achievement

            added_achievement.status = 'new'
            added_achievement.time_earned = datetime.now()
            self.achievements.append(added_achievement)


# player = Player(skill_lv=1, xp=90, balance=500.0,
#                 inventory=find_item('id', ['colt_m1911', 'm16a1', 'rpg_7', 'medkit']),
#                 stocks=['Microsoft', 'Microsoft', 'Tesla', 'Bitcoin'],
#                 achievements=[],
#                 data_game={'killed_mothers': 0,
#                            'damage_dealt': 0,
#                            },
#                 data_items={'purchased_items_firearm': 0,
#                             'purchased_items_explosive': 0,
#                             'purchased_items_consumable': 0,
#                             'purchased_items_videogame': 0,
#                             'purchased_items_meme': 0
#                             },
#                 data_financial={'total_spendings': 0,
#                                 'total_earnings': 0,
#                                 'purchased_stocks': 0,
#                                 'purchased_crypto': 0
#                                 },
#                 data_misc={'invalid inputs': 0,
#                            'entered cheat codes': 0,
#                            },
#                 data_translations={'killed_mothers': 'Killti Müetere',
#                                    'damage_dealt': 'Verursachte Schade',
#
#                                    'purchased_items_firearm': 'Gkaufti Schusswaffe',
#                                    'purchased_items_explosive': 'Gkaufte Sprängstoff',
#                                    'purchased_items_consumable': 'Gkaufti Konsumware',
#                                    'purchased_items_videogame': 'Gkaufti Videospiel Items',
#                                    'purchased_items_meme': 'Gkaufti Meme Items',
#
#                                    'total_spendings': 'Usgabe total',
#                                    'total_earnings': 'Ihname total',
#                                    'purchased_stocks': 'Gkaufti Aktie',
#                                    'purchased_crypto': 'Gkaufts Krypto'
#                                    }
#                 )


# --------- player stuff ------