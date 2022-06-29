from otree.api import *
import random

Cu = Currency
doc = """
An experiment that presents lottery choices to participants. Choices with varying attributes(options ranging from sure payoff to 3 likely payoffs) are presented at random. 
A randomly selected round is picked for payment at the end of the last round.
Read payoff and probability from csv"""


# TO Do
# Participants choices are not stored after randomization
# I created a variable to store them in player named choice_in__round, but it is always empty after the game is played
# I need to be able to pick values from the csv for each question to calculate reward
# Thank you


class C(BaseConstants):
    NAME_IN_URL = 'description'
    questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8','q9', 'q10', 'q11', 'q12',]
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = len(questions)
    PARTICIPATION_FEE = cu(8)
    CURR_EX = 0.2



class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.questions, round_numbers))
            p.participant.task_rounds = task_rounds

    for p in subsession.get_players():
        round_numbers = list(range(1, C.NUM_ROUNDS + 1))
        random.shuffle(round_numbers)
        selected_round = random.randint(1, C.NUM_ROUNDS)
        p.participant.selected_round = selected_round


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_rounds = models.IntegerField()
    age = models.IntegerField(label='What is your age?', min=17, max=65)
    gender = models.StringField(
        choices=[['Female', 'Female'], ['Male', 'Male'], ['Prefer not to say', 'Prefer not to say']],
        label='Gender',
        widget=widgets.RadioSelect,
    )
    is_experimented = models.BooleanField(
        label='Have you participated in similar experiments in the past?',
        choices=[[True, 'Yes'],
                 [False, 'No']
                 ],
        widget=widgets.RadioSelect,

    )
    education = models.StringField(
        label='What is your level of education?',
        choices=[['Primary', 'Primary'], ['Secondary', 'Secondary'], ['Tertiary', 'Tertiary'],
                 ['Prefer not to say', 'Prefer not to say']],
        widget=widgets.RadioSelect,
    )
    risk_taking = models.StringField(
        label='How will rate your desire to take risk on a scale 0f 1 to 10?',
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'],
                 ['7', '7'], ['8', '8'], ['9', '9'], ['10', '10']],
        widget=widgets.RadioSelectHorizontal,
    )

    q1 = models.StringField(
        choices=[[['You have 80% chance to win 4 and 0 otherwise', 4, 0, '80%', '0%'],
                  'You have 80% chance to win 4 and 0 otherwise', ],
                 [['You have 100% chance to win 3.2.', 3.2, 3.2, '100%'],
                  'You have 100% chance to win 3.2.', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q2 = models.StringField(
        choices=[[['You have 10% chance to win 32 and 0 otherwise', 32, 0, '10%', '0%'],
                  'You have 10% chance to win 32 and 0 otherwise', ],
                 [['You have 100% chance to win 3.2.', 3.2, 3.2, '100%'],
                  'You have 100% chance to win 3.2.', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q3 = models.StringField(
        choices=[[['You have 14% chance to win 23 and 0 otherwise', 23, 0, '14%', '0%'],
                  'You have 14% chance to win 23 and 0 otherwise', ],
                 [['You have 100% chance to win 3.2.', 3.2, 3.2, '100%'],
                  'You have 100% chance to win 3.2.', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q4 = models.StringField(
        choices=[[['You have 98% chance to win 3.26 and 0 otherwise', 3.26, 0, '98%', '0%'],
                  'You have 98% chance to win 3.26 and 0 otherwise', ],
                 [['You have 100% chance to win 3.2', 3.2, 3.2, '100%'],
                  'You have 100% chance to win 3.2', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q5 = models.StringField(
        choices=[[['You have 20% chance to win 16 and 0 otherwise', 16, 0, '20%', '0%'],
                  'You have 20% chance to win 16 and 0 otherwise', ],
                 [['You have 75% chance to win 2.6 and 25% to win 5', 2.6, 5, '75%', '25%'],
                  'You have 75% chance to win 2.6 and 25% to win 5', ]
                 ],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q6 = models.StringField(
        choices=[[['You have 85% chance to win 3.8 and 0 otherwise', 3.8, 0, '85%', '0%'],
                  'You have 85% chance to win 3.8 and 0 otherwise', ],
                 [['You have 75% chance to win 3.4 and 25% to win 2.6', 3.4, 2.6, '75%', '25%'],
                  'You have 75% chance to win 3.4 and 25% to win 2.6', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q7 = models.StringField(
        choices=[[['You have 10% chance to win 24 and 90% chance to win 2.5', 24, 2.5, 0, '10%', '32%'],
                  'You have 10% chance to win 24, 90% chance to win 2.5', ],
                 [['You have 100% chance to win 3.2', 3.2, 3.2, '100%'],
                  'You have 100% chance to win 3.2', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q8 = models.StringField(
        choices=[[['You have 40% chance to win 6; 40% chance to win 2 and 0 otherwise', 6, 2, 0, '40%', '40%'],
                  'You have 40% chance to win 6, 40% chance to win 2 and 0 otherwise', ],
                 [['You have 100% chance to win 3.2', 3.2, 3.2, '100%'],
                  'You have 100% chance to win 3.2', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q9 = models.StringField(
        choices=[[['You have 10% chance to win 30; 40% chance to win 0.5 and 0 otherwise', 30, 0.5, 0, '10%', '40%'],
                  'You have 10% chance to win 30, 40% chance to win 0.5 and 0 otherwise', ],
                 [['You have 50% chance to win 5 and 50% chance to win 1.4', 5, 1.4, '50%', '50%'],
                  'You have 50% chance to win 5,50% chance to win 1.4', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q10 = models.StringField(
        choices=[[['You have 60% chance to win 5; 35% chance to win 0.6 and 0 otherwise', 5, 0.6, '60%', '35%'],
                  'You have 60% chance to win 5, 35% chance to win 0.6 and 0 otherwise', ],
                 [['You have 50% chance to win 5 and 50% chance to win 1.4', 5, 1.4, '50%', '50%'],
                  'You have 50% chance to win 5 and 50% chance to win 1.4', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    q11 = models.StringField(
        choices=[[['You have 15% chance to win 16; 50% chance to win 1.6 and 0 otherwise', 16, 1.6, 0, '15%', '50%'],
                  'You have 15% chance to win 16, 50% chance to win 1.6 and 0 otherwise', ],
                 [['You have 35% chance to win 5; 30% chance to win 2.5 and 2 otherwise',5, 2.5, 2, '35%', '30%'],
                  'You have 35% chance to win 5, 30% chance to win 2.5 and 2 otherwise']],
        doc='Players decision', widget=widgets.RadioSelect,
    )
    q12 = models.StringField(
        choices=[[['You have 42% chance to win 7.2; 40% chance to win 0.45 and 0 otherwise', 7.2, 0.45, 0, '42%', '40%'],
                  'You have 42% chance to win 7.2, 40% chance to win 0.45 and 0 otherwise', ],
                 [['You have 40% chance to win 4; 40% chance to win 3.4 and 2 otherwise', 4, 3.4, 2, '40%', '40%'],
                  'You have 40% chance to win 4, 40% chance to win 3.4 and 2 otherwise']],
        doc='Players decision', widget=widgets.RadioSelect,
    )

    response = models.StringField()
    choice_in_round = models.StringField()
    choice = models.IntegerField()
    selected_round = models.StringField()


# FUNCTIONS
# To randomize choices
def choices(player: Player):
    import random
    choices = [['1'],
               ['2']
               ]
    random.shuffle(choices)
    return choices


# PAGES
class DemographicInformation(Page):
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['age', 'gender', 'is_experimented', 'education', 'risk_taking']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass


class Introduction(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == 1

# create dict for answers to each question
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                                  10: "10", 11: "11", 12: "12"}


class Instruction(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass


class StartPage(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == 1


class PartialFeedback(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


class Q1(Page):
    form_model = 'player'
    form_fields = ['q1']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q1']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "choice_in_round": player.in_rounds(1, C.NUM_ROUNDS),
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.choice = player.in_rounds(1, C.NUM_ROUNDS) == player.q1
        choice = {}
        choice[player.q1] = player.in_rounds(1, C.NUM_ROUNDS)
        print(choice)
        player.session.answers[1] = player.q1


class Q2(Page):
    form_model = 'player'
    form_fields = ['q2']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[2] = player.q2
    # @staticmethod
    # def vars_for_template(player: Player):
    #     player.participant.vars['q1'] = Q1
    #     return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))


class Q3(Page):
    form_model = 'player'
    form_fields = ['q3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q3']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(choice_in_round=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[3] = player.q3


class Q4(Page):
    form_model = 'player'
    form_fields = ['q4']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q4']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(choice_in_round=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[4] = player.q4


class Q5(Page):
    form_model = 'player'
    form_fields = ['q5']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q5']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[5] = player.q5


class Q6(Page):
    form_model = 'player'
    form_fields = ['q6']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q6']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[6] = player.q6


class Q7(Page):
    form_model = 'player'
    form_fields = ['q7']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q7']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[7] = player.q7


class Q8(Page):
    form_model = 'player'
    form_fields = ['q8']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q8']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[8] = player.q8


class Q9(Page):
    form_model = 'player'
    form_fields = ['q9']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q9']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[9] = player.q9


class Q10(Page):
    form_model = 'player'
    form_fields = ['q10']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q10']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[10] = player.q10


class Q11(Page):
    form_model = 'player'
    form_fields = ['q11']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q11']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(player_in_rounds=player.in_rounds(1, C.NUM_ROUNDS))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[11] = player.q11

class Q12(Page):
    form_model = 'player'
    form_fields = ['q12']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['q12']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "player_in_rounds": player.in_rounds(1, C.NUM_ROUNDS),
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[12] = player.q12

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.session.answers[12] = player.q12
        import random
        participant = player.participant
        # if it's the last round,select a random round from the 10 questions and play the lottery chosen by the participant for the payoff.
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            participant.selected_round = random_round
            player.selected_round = str(random_round)
            # player_in_selected_round = player.in_round(random_round)


class RandomRound(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    q4 = models.StringField(
        choices=[[['You have 98% chance to win 3.26 and 0 otherwise', 3.26, 0, '98%', '0%'],
                  'You have 98% chance to win 3.26 and 0 otherwise', ],
                 [['You have 100% chance to win 3.2', 3.2, 3.2], 'You have 100% chance to win 3.2', ]],
        doc='Players decision', widget=widgets.RadioSelect,
    )
    @staticmethod
    def vars_for_template(player: Player):
        probability = random.randint(1, 100)
        split = player.session.answers[player.participant.selected_round].split(",")

        if split[3] == "100%":
            answer = split[1].replace("[", "").replace("]", "")
        elif int(split[3].replace("%", "").replace("'", "").replace(" ", "").replace("[", "").replace("]", "")) >= probability:
            answer = split[1].replace("[", "").replace("]", "")
        elif int(split[4].replace("%", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "")) >= probability:
            answer = split[2].replace("[", "").replace("]", "")
        else:
            answer = 0
        #answer = 32
        return {
            # "answers": player.session.answers[player.participant.selected_round]
            "answer": answer,
            "question": player.session.answers[player.participant.selected_round].split(",")[0].replace("[", "").replace("'", "").replace(";", ","),
            "participationfee": 8,
            "result": (float(answer) * 0.2) + 8,
            "info": player.session.answers[player.participant.selected_round],
             "probability number" : probability
        }


class Results(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Introduction,Instruction, StartPage, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12,
                 DemographicInformation, RandomRound]

# @staticmethod
# def vars_for_template(player):
#    a = player.num_apples * 10
#    return dict(
#        a=a,
#        b=1 + 1,
#    )
# before_next_page()
