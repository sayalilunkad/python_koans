#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

# from runner.koan import *
import random


class DiceSet(object):
    def __init__(self):
        self._values = list()
        self.accumulated_score = 0
        self.num_count = dict()

    def get_values(self):
        return self._values

    # n = number of dice rolled at once
    def roll(self, n=5):
        # Creates list of values of one roll
        self._values = list()
        for r in range(n):
            self._values.append(random.randint(1, 6))
        self.number_count()
        score = self.calc_chance()
        return score

    def number_count(self):
        # Counts the occurances of numbers rolled.
        self.num_count = {}.fromkeys(self._values, 0)
        # Calculates value accociated with number rolled.
        self.num_score = {}.fromkeys(self._values, 0)
        for i in self._values:
            self.num_count[i] += 1

    def score_sum(self):
        '''
        This calculates the score for one roll of dice
        according to the rules below:
        Three 1's => 1000 points
        Three 6's =>  600 points
        Three 5's =>  500 points
        Three 4's =>  400 points
        Three 3's =>  300 points
        Three 2's =>  200 points
        One   1   =>  100 points
        One   5   =>   50 points
        '''
        ''' 1000 points on 3 ones'''
        try:
            self.num_score[1] = (self.num_count[1] // 3) * 1000
        except Exception:
            pass
        '''100 points for  one which is not in set of 3 ones'''
        try:
            self.num_score[1] += (self.num_count[1] % 3) * 100
        except Exception:
            pass
        '''50 points for 5 which is not in set of 5 ones'''
        try:
            self.num_score[5] += (self.num_count[5] % 3) * 50
        except Exception:
            pass
        '''Any number in range 2-7 repeated
        3 times = number * 100 points'''
        for r in range(2, 7):
            try:
                self.num_score[r] += (self.num_count[r] // 3) * 100 * r
            except Exception:
                pass

        turn_score = sum(self.num_score.values())
        return turn_score

    def calc_chance(self):
        turn_score = self.score_sum()
        self.accumulated_score += turn_score
        if self.accumulated_score < 300:
            return self.accumulated_score
        elif turn_score == 0:
            return 0
        else:
            zeros = self.num_count.values().count(0)
            if zeros == 0:
                self.roll(5)
            else:
                self.roll(zeros)


class game(object):
    '''
    Terminology:
        turn_score: score for each roll.
        accumulated_score: sum of score after each turn.
        total_score:  total score of each player.

    Game flow:
    Round:
        Turn:
            if new turn:
                Roll the dice
                if turn_score>=300
                "Player in the game"
                else Round ends
            else:
                if turn_score=0:
                accumulated_score=0
                round ends
                else:
                Goto Turn: Roll the non-scoring dices again
            if all 5 are scoring dice:
            Goto new turn
            if total_score >=3000
                Goto Final Round
            if  player decided to stop:
                total_score+=accumulated_score

        End Game:
        Final Round:
            New turn for each player
            winner = highest_score(accumulated_score+turn_score)
    '''

    def __init__(self, number_of_players=3):
        # List of players.
        self.players = list()
        # Initializing list of player with names.
        self.init_player(number_of_players)
        # Dictionary containing players and their total scores.
        self.total_score = dict()
        # Initialize total score dict.
        self.init_total_score()
        # Winner name
        self.winner = str()
        self.accumulated_score = 0

    def init_player(self, number_of_players):
        # Initializes player list with player names.
        for number_of_players in range(number_of_players):
            self.players.append('player' + str(number_of_players+1))

    def init_total_score(self):
        # Initializes total score to 0 for all players.
        self.total_score = {}.fromkeys(self.players, 0)

    def get_winner(self):
        return self.winner

    def turn(self, player):
        # One throw of set of dice
        dice = DiceSet()
        round_score = dice.roll(5)
        try:
            self.total_score[player] += round_score
        except Exception:
            pass
        return self.total_score[player]

    def round(self):
        i = 0
        while i<10:
            for player in self.players:
                self.turn(player)
            i += 1

        self.final_round()

    def final_round(self):
        for player in self.players:
            self.turn(player)
        winner_score = max(self.total_score.values())
        for name, score in self.total_score.items():
            if score == winner_score:
                self.winner = name

    '''
class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        trial = game()
        player_list = trial.players
        print player_list
        # self.assertEqual(['player0', 'player1', 'player2'], player_list)
        # trial.init_total_score(player_list)

    def test_score(self):

        #Test to calculate scores
        #5 1 3 4 1 50 + 2 * 100 = 250
        #1 1 1 3 1 1000 + 100 = 1100
        #2 4 4 5 4 400 + 50 = 450
        #
#       dice = DiceSet()
#       test = dice.roll(5)
#       print test
#       self.assertEqual(score(test), 150)
        self.assertEqual(score([5, 1, 3, 4, 1]), 250)
        self.assertEqual(score([1, 1, 1, 3, 1]), 1100)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)
        pass
    '''
if __name__ == '__main__':
    greed = game()
    greed.round()
    print("The Winner is", greed.get_winner())
