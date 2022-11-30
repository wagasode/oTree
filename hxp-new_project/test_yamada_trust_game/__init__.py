
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'test_yamada_trust_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(10)
    MULTIPLICATION_FACTOR = 3
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    sent_amount = models.CurrencyField(label='プレイヤーBに対していくら投資しますか？')
    sent_back_amount = models.CurrencyField(label='プレイヤーAに対していくら返還しますか？')
def sent_back_amount_choices(group: Group):
    return currency_range(
        0,
        group.sent_amount * C.MULTIPLICATION_FACTOR,
        1
    )
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLICATION_FACTOR - group.sent_back_amount
class Player(BasePlayer):
    pass
class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group == 1
class WaitForP1(WaitPage):
    pass
class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']
    timeout_seconds = 60
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group == 2
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        group = player.group
        return dict(
            tripled_amount = group.sent_amount * C.MULTIPLICATION_FACTOR
        )
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results]