
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'test_yamada_prisoners_dilemma_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    ENDOWMENT = cu(0)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

class Round1(Page):
    form_model = 'player'

class Round2(Page):
    form_model = 'player'

class Round3(Page):
    form_model = 'player'

class Round4(Page):
    form_model = 'player'

class Round5(Page):
    form_model = 'player'

class Result(Page):
    form_model = 'player'

page_sequence = [Round1, Round2, Round3, Round4, Round5, Result]
