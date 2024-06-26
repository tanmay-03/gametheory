# -*- coding: utf-8 -*-
"""GT18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19yoI8wMD-TCRUy_38oQcShIKZpqa451J

Design a Tick-tac-Toe game (3x3 and 4x4). Decide all possible strategies. Define
Nash equilibrium from there.
"""

import random

class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def is_winner(self, player):
        # Check rows, columns, and diagonals for winning condition
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)) or \
               all(self.board[j][i] == player for j in range(self.size)) or \
               all(self.board[i][i] == player for i in range(self.size)) or \
               all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
                return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

def basic_strategy(game):
    # Start from the center if available, otherwise start from a random corner
    center = game.size // 2
    if game.board[center][center] == ' ':
        return center, center
    else:
        return random.choice([(0, 0), (0, game.size - 1), (game.size - 1, 0), (game.size - 1, game.size - 1)])

def play_game(size):
    game = TicTacToe(size)
    game.print_board()

    while True:
        row, col = basic_strategy(game)
        if game.make_move(row, col):
            game.print_board()
            if game.is_winner(game.current_player):
                print(f'Player {game.current_player} wins!')
                break
            elif game.is_board_full():
                print('It\'s a draw!')
                break
            game.switch_player()

# Play 3x3 Tic-tac-Toe
print("3x3 Tic-tac-Toe")
play_game(3)

# Play 4x4 Tic-tac-Toe
print("\n4x4 Tic-tac-Toe")
play_game(4)

""" Prisoners dilemma: design an effective cooperative game. Decide all
possible strategies. Define Nash equilibrium from there.
"""

import random
def prisoner_dilemma(player1_choice,player2_choice):
    #define payoff values
    betray_payoff = 3
    cooperate_payoff = 2
    temptation_payoff = 5
    silent_payoff = 1

    #both players betray
    if player1_choice == 'red' and player2_choice =='red':
        return betray_payoff, betray_payoff

    #player 1 betray and player 2 cooperate
    elif player1_choice == 'red' and player2_choice =='green':
        return temptation_payoff , slient_payoff

    #player 1 cooperate and player 2 betray
    elif player1_choice == 'green' and player2_choice =='red':
        return slient_payoff , temptation_payoff

    #both player cooperate
    elif player1_choice == 'green' and player2_choice =='green':
        return cooperate_payoff, cooperate_payoff

    else:
        #invalid choices
        return 0,0

def main():
    print("prisoner's dilemma game")
    print("choose 'green' or 'red'")

    pchoice = ['red' , 'green']
    #get choice from players
    player1_choice = input("player 1 choice:")
    player2_choice = random.choice(pchoice)

    #calculate payoffs
    player1_payoff ,  player2_payoff = prisoner_dilemma(player1_choice,player2_choice)

    #display results
    print(f"\nPlayer 1 payoff:{player1_payoff}")
    print(f"\Player 2 payoff:{player1_payoff}")

if __name__ == "__main__" :
    main()

"""Nash equilibrium"""

def prisoner_dilemma(x, y):
 if x == 'confess':
    if y == 'confess':
        return 'Both convic receive 3 year sentence.'
    elif y == 'deny':
        return 'X receives a 8 years sentence. Y receives 2 years sentence.'
    elif x == 'deny':
      if y == 'confess':
         return 'X receives 2 years sentence. Y receives 8 years sentence.'
    elif y == 'deny':
       return 'Both convict receive a moderate sentence of 6 years.'

x = input("X, enter 'confess' or 'deny': ").lower()
y = input("Y, enter 'confess' or 'deny': ").lower()

result = prisoner_dilemma(x, y)
print(result)

"""Design and check Mixed Strategies and Mixed Strategy Nash
Equilibrium for a game.
"""

import numpy as np
from scipy.optimize import linprog

# Payoff matrix for Player 1 (rows) and Player 2 (columns)
payoff_matrix_player1 = np.array([[3, 0], [5, 1]])

#The transpose of the payoff matrix for Player 2
payoff_matrix_player2 = np.array([[3, 5], [0,1]])

#Flatten the payoff matrices to use in linear programming
c = -payoff_matrix_player2.flatten ()

#Coefficients for the equality constraint (sum of probabilities equals 1)
A_eq = np.ones((1, len (c)))

#Right-hand side of the equality constraint
b_eq = np.array([1.0])

#Bounds for the probabilities (each probability is between 0 and 1)
bounds = [(0, 1) for _ in range(len(c))]

#Solve the linear programming problem to find mixed strategy nash equilibrium
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

#Mixed strategies for both players

mixed_strategy_player1 = result.x
mixed_strategy_player2 = 1 - mixed_strategy_player1

print("Mixed Strategy Nash Equilibrium for the Prisoner's Dilemma:")
print("Player 1:", mixed_strategy_player1)

print("Player 2:", mixed_strategy_player2)

"""Find the min max and saddle point of game"""

def prisoners_dilemma(player1_choice, player2_choice):
    if player1_choice == 'cooperate' and player2_choice == 'cooperate':
        return "Both players get 2 years in prison"
    elif player1_choice == 'betray' and player2_choice == 'cooperate':
        return "Player 1 goes free, Player 2 gets 5 years in prison"
    elif player1_choice == 'cooperate' and player2_choice == 'betray':
        return "Player 1 gets 5 years in prison, Player 2 goes free"
    elif player1_choice == 'betray' and player2_choice == 'betray':
        return "Both players get 4 years in prison"

#Example usage:

player1_decision = 'cooperate'

player2_decision = 'brtray'

result = prisoners_dilemma(player1_decision, player2_decision)
print(result)

"""Impliment Bayesian game"""

import random

class CricketGame:
    def __init__(self, total_overs):
        self.total_overs = total_overs
        self.players = ["Player A", "Player B"]
        self.current_batsman = None
        self.current_bowler = None
        self.runs_scored = 0
        self.wickets_lost = 0

    def toss(self):
        return random.choice(self.players)

    def start_game(self):
        print("Welcome to the Cricket Game!")
        print("Toss time...")
        winning_toss = self.toss()
        print(f"{winning_toss} won the toss and chose to bat.\n")

        if winning_toss == "Player A":
            self.current_batsman = "Player A"
            self.current_bowler = "Player B"
        else:
            self.current_batsman = "Player B"
            self.current_bowler = "Player A"

    def play_ball(self):
        runs = random.randint(0, 6)
        print(f"{self.current_batsman} scores {runs} runs!")

        if runs == 0:
            print(f"{self.current_batsman} is OUT!")
            self.wickets_lost += 1
        else:
            self.runs_scored += runs

    def switch_sides(self):
        self.current_batsman, self.current_bowler = self.current_bowler, self.current_batsman

    def display_scoreboard(self):
        print("\nScoreboard:")
        print(f"{self.current_batsman}: {self.runs_scored}/{self.wickets_lost} (Overs: {self.total_overs})\n")

    def play(self):
        self.start_game()

        for over in range(1, self.total_overs + 1):
            print(f"Over {over} begins!")
            for ball in range(1, 7):
                input("Press Enter to bowl...")  # Simulating the user pressing Enter to bowl
                self.play_ball()

                if self.wickets_lost == 2:
                    print("All wickets lost! Game over.")
                    break

            self.display_scoreboard()
            self.switch_sides()

        print("Game Over!")
        self.display_scoreboard()

# Example usage
total_overs = 2
cricket_game = CricketGame(total_overs)
cricket_game.play()

"""Write a python code to implement social choice function"""

from collections import Counter

def majority_vote(choices):
    """
    Determine the majority choice from a list of choices.

    Args:
    - choices: A list of choices (e.g., ['A', 'B', 'A', 'C', 'A', 'B']).

    Returns:
    - The majority choice.
    """
    # Count occurrences of each choice
    choice_counts = Counter(choices)

    # Find the choice with the maximum count
    majority_choice = max(choice_counts, key=choice_counts.get)

    return majority_choice

# Example usage:
votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
print("Majority Choice:", majority_vote(votes))

"""To desing 3 incentive game based on class discussion"""

import random
flights={
    ("New York","London","Summer"):1000,
    ("New York","London","Winter"):800,
    ("Los Angeles","Tokyo","Summer"):1500,
    ("Los Angeles","Tokyo","Winter"):1200,
    ("Chicago","Paris","Summer"):900,
    ("Chicago","Paris","Winter"):700
}

def flight_fare_estimation():

    origin, destination, season = random.choice(list(flights.keys()))

    actual_fare = flights[(origin,destination,season)]

    guess = int(input(f"How much do you think a flight form{origin} to {destination} in {season} cost? "))

    difference = abs(guess - actual_fare)

    if difference == 0:
        points = 100
    elif difference <= 100:
        points = 75
    elif difference <= 200:
        points = 50
    elif difference <= 500:
        points = 25
    else:
        points = 0

    print(f"The actual fare for a flight from {origin} to {destination} in {season} is {actual_fare}.")
    print(f"Your guess was {guess}.")
    print(f"You earned {points} points.\n")

for i in range(3):
    print(f"Game {i+1}")
    flight_fare_estimation()

import random


employees = {
    ("Software Engineer", "Level 1", "0-2 years"): 88000,
    ("Software Engineer", "Level 2", "2-5 years"): 100000,
    ("Software Engineer", "Level 3", "5+ years"): 120000,
    ("Data Scientist", "Level 1", "0-2 years"): 90000,
    ("Data Scientist", "Level 2", "2-5 years"): 110000,
    ("Data Scientist", "Level 3", "5+ years"): 130000
}


def employee_salary_estimations():

    job_title, level, experience = random.choice(list(employees.keys()))

    actual_salary = employees[(job_title, level, experience)]

    guess = int(input(f"What do you think a {job_title} at {level} level with {experience} of experience earns? "))

    difference = abs(guess - actual_salary)

    if difference == 0:
        points = 100
    elif difference <= 1000:
        points = 75
    elif difference <= 5000:
        points = 50
    elif difference <= 10000:
        points = 25
    else:
        points = 0

    print(f"The actual salary for a {job_title} at {level} level with {experience} of experience is {actual_salary}.")
    print(f"Your guess was {guess}.")
    print(f"You earned {points} points.\n")


for i in range(3):
    print(f"Game {i+1}")
    employee_salary_estimations()

import random

products = {
    ('Samsung Galaxy S21', '128GB', 'Phantom Black'): 700,
    ('Apple iPhone 13', '256GB', 'Midnight'): 1200,
    ('Google Pixel 6', '128GB', 'Stormy Black'): 900,
    ('OnePlus 10', '256GB', 'Nebula Black'): 1000,
    ('Xiaomi Mi 12', '256GB', 'Cosmic Gray'): 800
}


def product_value_estimation():

    product, actual_value = random.choice(list(products.items()))
    product_name, product_specs_1, product_specs_2 = product

    guess = int(input(f"What do you think a {product_name} with {product_specs_1}, {product_specs_2} is worth in the market? "))

    difference = abs(guess - actual_value)

    if difference == 0:
        points = 100
    elif difference <= 100:
        points = 75
    elif difference < 200:
        points = 50
    elif difference <= 500:
        points = 25
    else:
        points = 0

    print(f"The actual value of a {product_name} with {product_specs_1}, {product_specs_2} is {actual_value}.")
    print(f"Your guess was {guess}.")
    print(f"You earned {points} points.\n")


for i in range(3):
    print(f"Game {i + 1}:")
    product_value_estimation()