
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'test_yamada_public_goods'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    MULTIPLIER = 2
    ENDOWMENT = cu(1000)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    for player in players:
        player.payoff = C.ENDOWMENT - player.contribution + group.individual_share
class Player(BasePlayer):
    contribution = models.CurrencyField(label='あなたは寄付金をいくら支払いますか？', min=0)
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
page_sequence = [Contribute, ResultsWaitPage, Results]