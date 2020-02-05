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
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 15

    instructions_template = 'prisoner/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(-200)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(100)
    both_defect_payoff = c(0)


class Subsession(BaseSubsession):
    
    #randomize every 5 rounds
    def creating_session(self):
        all_set = True
        for g in self.get_groups():            
            if g.round_number != 1:
                g.max_round_num = g.in_round(g.round_number - 1).max_round_num
                g.new_round_num = g.in_round(g.round_number - 1).new_round_num
                print('this one comes first', g.round_number, 'and round', g.new_round_num, 'and max', g.max_round_num)
                if g.round_number <= g.max_round_num:                
                    all_set = False
                    print('it is false')
        if all_set:
            print('true dat')
            self.group_randomly()
            for g in self.get_groups():
                m = 1
                while random.random() <= 0.75:
                    m += 1
                g.max_round_num = m + g.round_number - 1
                g.new_round_num = m
                print('for', g.round_number, 'round is', g.new_round_num, 'and max is', g.max_round_num)
       

    

class Group(BaseGroup):
    max_round_num = models.IntegerField()
    new_round_num = models.IntegerField()


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

