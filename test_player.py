import pytest
from datetime import datetime

from _pytest import monkeypatch

from main import check_player_data
from player import Player
from item import Item
from item import initialize_items
from achievement import Achievement, initialize_achievements, find_achievement


@pytest.fixture
def player():
    return Player(skill_lv=1, xp=90, balance=500.0,
                  inventory=[],
                  stocks=['Microsoft', 'Microsoft', 'Tesla', 'Bitcoin'],
                  achievements=[],
                  data_game={'killed_mothers': 0,
                             'damage_dealt': 0,
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


@pytest.fixture
def not_existing_item():
    return Item('test_item_1', 'Test item 1', 'firearm', 'rifle', '1st test item', price=20.0, req_skill_lv=2,
                infl_mass=0, infl_health=-10, infl_mood=-10, infl_anger=15, infl_boredom=-15, infl_confusion=0)


@pytest.fixture
def all_items():
    return initialize_items()


@pytest.fixture
def all_achievements():
    return initialize_achievements()


def test_add_item(player, all_items):
    for item in all_items:
        player.add_item(item)

    assert player.inventory == all_items


def test_add_not_existing_item(player, not_existing_item):
    try:
        player.add_item(not_existing_item)
    except Exception:
        assert True
    else:
        assert False


def test_add_achievement(player, all_achievements):
    for achievement in all_achievements:
        player.add_achievement(achievement.id)

    test_passed = True
    for achievement in player.achievements:
        if achievement.status != 'new' or achievement.time_earned != datetime.now():
            raise Exception('Test add achievement failed, status != "new" or time_earned not correct. ')







