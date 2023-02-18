from dataclasses import dataclass
from datetime import datetime

# --------- achievement stuff ---------
@dataclass
class Achievement:
    id: int
    name: str
    description: str
    reward: float
    status: str
    time_earned: datetime = datetime(1970, 1, 1, 12, 00)

    def __str__(self):
        return f'-- {self.name} --\n{self.description}\nVerdient: {self.time_earned_formatted}\nCHF {self.reward}'

    @property
    def time_earned_formatted(self):
        time_earned_formatted = datetime.strftime(self.time_earned, '%H:%M:%S')
        return time_earned_formatted

    # @property
    # def status(self):
    #     if self.status not in ['new', 'old', 'not earned']:
    #         raise ValueError('Invalid Achievement Status')


def initialize_achievements():
    return [Achievement(1, 'Test Achievement', 'En test du Dubbel', 1000000.0, status='not earned'),
            Achievement(2, 'Test Achievement 2', 'De zweiti Test du Dubbel', 500000.0, status='not earned'),
            Achievement(3, 'Mueter-Killer', 'Leg dini erschti Mueter um', 100.0, status='not earned'),
            Achievement(4, 'Arschloch', 'Duen erfolgrich en Cheat code ihlöse', -50.0, status='not earned'),
            Achievement(5, 'r/WallStreetBets Immigrant', 'Chauf en Aktie', 75.0, status='not earned'),
            Achievement(6, 'Kulturkänner', 'Chauf es Meme Item im Shop', 120.0, status='not earned'),
            Achievement(7, 'Dully', 'Wähl e inexistänti Option us', -20, status='not earned')
            ]


all_achievements = initialize_achievements()


def find_achievement(id):
    found_achievement = None
    for achievement in all_achievements:
        if achievement.id == id:
            found_achievement = achievement

    if found_achievement:
        return found_achievement
    else:
        input('invalid achievement id')


# --------- achievement stuff ---------