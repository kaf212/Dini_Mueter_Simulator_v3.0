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


#


# --------- player stuff ------