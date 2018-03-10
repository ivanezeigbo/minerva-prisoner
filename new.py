from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Player(BasePlayer):
    

    cooperate = models.BooleanField(
        choices=[
            [False, 'Defect'],
            [True, 'Cooperate']
        ]
    )
    
    player_name = models.StringField(label="Please type in your name.")
    
    

    def decision_label(self):
        if self.cooperate:
            return 'cooperate'
        return 'defect'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = {
            True:
                {
                    True: Constants.both_cooperate_payoff,
                    False: Constants.betrayed_payoff
                },
            False:
                {
                    True: Constants.betray_payoff,
                    False: Constants.both_defect_payoff
                }
        }

        print ("Hey I'm here")
        print (self.decision_label())
        self.payoff = payoff_matrix[self.cooperate][self.other_player().cooperate]

player = Player()
print (player.cooperate)
