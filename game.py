from player import Player
from point import Point
from team import Team
from constants import *

for i in range(10):
    ninjas.append(Player('Player {}'.format(i+1),
                         'Ninja',
                         Point(5, 0, 0)
                         ))
    pirates.append(Player('Player {}'.format(i+11),
                          'Pirate',
                          Point(-5, 0, 0)
                          ))


for i in range(len(ninjas)):
    print(ninjas[i])

for i in range(len(pirates)):
    print(pirates[i])


class Game:
    def __init__(self, number_players=0, teams=[], players=[]):
        """
        Initialize the game

        :param n: <int> Number of players
        """
        self.number_players = number_players
        self.teams = teams
        self.players = players

    def create_players(self)
        return list()

    def create_teams(self):
        for i in range(self.number_players):
            for team in TEAMS:
                self.teams.append()
