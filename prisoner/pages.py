from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    timeout_seconds = 100
    form_model = 'player'
    form_fields = ['player_name']
    def is_displayed(self):
        return self.round_number == 1

class NameWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['cooperate']
    def vars_for_template(self):
        
        return {
            'opponent_name': self.player.other_player().in_round(1).player_name,
            }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        opponent = self.player.other_player()
        
        return {
            'my_decision': self.player.decision_label(),
            'other_player_decision': opponent.decision_label(),
            'same_choice': self.player.cooperate == opponent.cooperate,
            'total_payoff': sum([p.payoff for p in self.player.in_rounds(self.round_number - ((self.round_number - 1) % 5), self.round_number)]),
            # TODO: total payoff only for that specific person FIX!
        }

class InteractionOverWaitPage(WaitPage):
    wait_for_all_groups = True
    title_text = "The interaction is now over."
    body_text = "Wait until all groups are done so you can be paired with someone new."
    def is_displayed(self):
        return self.round_number % 5 == 0


page_sequence = [
    Introduction,
    NameWaitPage,
    Decision,
    ResultsWaitPage,
    Results,
    InteractionOverWaitPage
]
