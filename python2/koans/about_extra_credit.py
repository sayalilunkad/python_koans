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

from runner.koan import *

class DiceSet(object):
    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        self._values = []
        for r in range(0, n):
            self._values.append(random.randint(1, 6))


def score(dice):
    '''
    This calculates the score for one roll of dice according to the rules below:
    Three 1's => 1000 points
    Three 6's =>  600 points
    Three 5's =>  500 points
    Three 4's =>  400 points
    Three 3's =>  300 points
    Three 2's =>  200 points
    One   1   =>  100 points
    One   5   =>   50 points
    '''
    numbers = {}.fromkeys(range(1, 7), 0)

    for d in dice:
        numbers[d] += 1
    sum = (numbers[1] // 3) * 1000

    sum += (numbers[1] % 3) * 100

    sum += (numbers[5] % 3) * 50

    for r in range(2, 7):
        sum += (numbers[r] // 3) * 100 * r
    return sum


class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass
    def test_score():
        self.assertEqual(score([5, 1, 3, 4, 1]), 250)
        pass
