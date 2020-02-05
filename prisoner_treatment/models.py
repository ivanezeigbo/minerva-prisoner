from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_treatment'
    players_per_group = 2
    num_rounds = 15

    instructions_template = 'prisoner_treatment/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(-200)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(100)
    both_defect_payoff = c(0)

    #payoff if one player decides to punish the other
    punisher_payoff = c(-100)
    punished_payoff = c(-500)
    both_punish_payoff = c(-500)


class Subsession(BaseSubsession):
    #randomize every 5 rounds
    def creating_session(self):
        if self.round_number % 5 == 1:
            print(self.round_number)
            self.group_randomly()
        else:
            self.group_like_round(self.round_number - 1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    

    cooperate = models.IntegerField(
        choices=[
            (0, 'Defect'),
            (1, 'Cooperate'),
            (2, 'Punish')
        ]
    )
    
    player_name = models.StringField(label="Please type in your name.")
    
    

    def decision_label(self):
        if self.cooperate == 1:
            return 'cooperate'
        elif self.cooperate == 0:
            return 'defect'
        else:
            return 'punish'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = {
            1:
                {
                    1: Constants.both_cooperate_payoff,
                    0: Constants.betrayed_payoff,
                    2: Constants.punished_payoff
                },
            0:
                {
                    1: Constants.betray_payoff,
                    0: Constants.both_defect_payoff,
                    2: Constants.punished_payoff,
                },
            2:
                {
                    1: Constants.punisher_payoff,
                    0: Constants.punisher_payoff,
                    2: Constants.both_punish_payoff,
                },
        }
        
        
        self.payoff = payoff_matrix[self.cooperate][self.other_player().cooperate]

