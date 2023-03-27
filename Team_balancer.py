"""
A program to create 'balanced' teams for 5-a-side
football using player attributes loaded from
'PlayerList.csv'
"""

import csv
import random
from random import seed
from random import randint
from random import random

def create_teams(x):
    """
    A function to randomly assign players to teams.
    """
    Team1.team.clear()
    Team2.team.clear()
    seed(x)
    for player in players:
        value = random()
        if (value >= 0.5 or len(Team2.team) == len(players)/2) and len(Team1.team) < len(players)/2:
            Team1.team.append(players[player])
        elif value < 0.5 or len(Team1.team) >= len(players)/2:
            Team2.team.append(players[player])

class Player:

    """
    A class to store player info.
    """

    def __init__(self, name, fitness, attack, defense):
        self.name = name
        self.fitness = int(fitness)
        self.attack = int(attack)
        self.defense = int(defense)

    def __repr__(self) -> str:
        s = f"{self.name}"
        return s

class Team:

    """
    A class to represent a 5 a side team.
    """

    def __init__(self):
        self.team = []

    def __repr__(self):
        s = f"{self.team}"
        return s

    def fitness(self):
        """
        Function calculates average fitness of team.
        """
        fitness_average = 0
        for player in self.team:
            fitness_average += player.fitness
        fitness_average /= len(self.team)
        return fitness_average

    def defense(self):
        """
        Function calculates average defense of team.
        """
        defense_average = 0
        for player in self.team:
            defense_average += player.defense
        defense_average /= len(self.team)
        return defense_average

    def attack(self):
        """
        Function calculates average attack of team.
        """
        attack_average = 0
        for player in self.team:
            attack_average += player.attack
        attack_average /= len(self.team)
        return attack_average


# load player info from csv file.
player_file = open("PlayerList.csv", "r", newline='')
csv_reader_players = csv.DictReader(player_file, delimiter=',',
                                    quotechar='"')

# store player info in array of player objects.
players = {}
for row in csv_reader_players:
    players[row["Name"]] = Player(row["Name"], row["Fitness"],
                                  row["Attack"], row["Defense"])

Team1 = Team()
Team2 = Team()

# loop to create teams and determine if
# they are balanced or not.
fitness_difference = 1
attack_diff = 1
defense_diff = 0.5
iterations = 0
changed = False
while True:
    x = randint(1, 10000000000000000000)
    create_teams(x)

    # calculates the average fitness of each team.
    fitness_difference_new = abs(Team1.fitness() - Team2.fitness())

    # calculates the average attack of each team.
    attack_diff_new = abs(Team1.attack() - Team2.attack())

    # calculates the average defense of each team.
    defense_diff_new = abs(Team1.defense() - Team2.defense())

    # conditions to ensure balanced teams.
    attack_condition1 = Team1.attack() > Team2.attack()
    defense_condition1 = Team1.defense() > Team2.defense()

    attack_condition2 = Team2.attack() > Team1.attack()
    defense_condition2 = Team2.defense() > Team1.defense()

    """
    The following code works as such:

    Conditions 1 & 2 - if a team has both a higher attack
    and defense average than the other, the loop restarts.

    Conditions 3-6 - if one team has a higher defence and the other
    team does not have a higher attack, the loop restarts (and vice versa).

    """
    if attack_condition1 and defense_condition1:
        iterations += 1
        continue
    elif attack_condition2 and defense_condition2:
        iterations += 1
        continue
    elif attack_condition1 and defense_condition2 == False:
        iterations += 1
        continue
    elif attack_condition2 and defense_condition1 == False:
        iterations += 1
        continue
    elif defense_condition1 and attack_condition2 == False:
        iterations += 1
        continue
    elif defense_condition2 and attack_condition1 == False:
        iterations += 1
        continue

    # checks the new averages are lower than initial values.
    d = defense_diff_new <= defense_diff
    a = attack_diff_new <= attack_diff
    f = fitness_difference_new <= fitness_difference

    if d and a and f:
        defense_diff = defense_diff_new
        attack_diff = attack_diff_new
        fitness_difference = fitness_difference_new
        y = x
        changed = True
    elif iterations > 10000:
        break
    else:
        iterations += 1
        continue

if changed is True:
    create_teams(y)

# calculates the average fitness of each team.
fitness_difference = abs(Team1.fitness() - Team2.fitness())

# calculates the average attack of each team.
attack_diff = abs(Team1.attack() - Team2.attack())

# calculates the average defense of each team.
defense_diff = abs(Team1.defense() - Team2.defense())

# display attack difference and which team is higher.
s = f"Difference in attack: {round(attack_diff, 2)}\n"
if Team1.attack() > Team2.attack():
    s += "Team 1 >\n"
elif Team2.attack() > Team1.attack():
    s += "Team 2 >\n"
elif attack_diff == 0.0:
    s += "Equal attack!\n"
print(s)

# display defense difference and which team is higher.
s = f"Difference in defense: {round(defense_diff, 2)}\n"
if Team1.defense() > Team2.defense():
    s += "Team 1 >\n"
elif Team2.defense() > Team1.defense():
    s += "Team 2 >\n"
elif defense_diff == 0.0:
    s += "Equal defense!\n"
print(s)

# display fitness difference and which team is higher.
s = f"Difference in fitness: {round(fitness_difference, 2)}\n"
if Team1.fitness() > Team2.fitness():
    s += "Team 1 >\n"
elif Team2.fitness() > Team1.fitness():
    s += "Team 2 >\n"
elif fitness_difference == 0.0:
    s += "Equal fitness!\n"
print(s)


# Print the balanced teams.
print(Team1)
print("")
print(Team2)
if changed is False:
    print("\nTeams not optimised, change initiating values.")
