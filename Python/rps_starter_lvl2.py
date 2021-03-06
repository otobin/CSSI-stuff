#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random


def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    player_move = raw_input("Enter a move: |r|p|s|")
    return player_move
    # TODO


def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    return "rps"[random.randint(0,2)]


def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    if player_move == comp_move:
        return "tie"
    elif (player_move == "r" and comp_move == "s") or  \
        (player_move == "s" and comp_move == "p") or \
        (player_move == "p" and comp_move == "r"):
        return "player"
    else:
        return "computer"

    # TODO


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    print("Player Score: %s" % player_wins)
    print("Computer Score: %s" % comp_wins)
    print("Ties: %s" % ties)


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""
    if short_move == 'r':
        return "Rock"
    elif short_move == 'p':
        return "Paper"
    else:
        return "Scissors"


player_wins = 0
computer_wins = 0
ties = 0
numRounds = int(raw_input("How many rounds do you want to play?"))
for i in range(0, numRounds):
    player_move = get_player_move()
    computer_move = get_computer_move()
    winner = determine_winner(player_move, computer_move)
    if winner == "player":
        player_wins += 1
    elif winner == "computer":
        computer_wins += 1
    else:
        ties += 1
    print("The winner is: " + winner)
    print_scoreboard(player_wins, computer_wins, ties)
