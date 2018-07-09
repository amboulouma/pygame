from player import Player


class Team:
    def __init__(self, name='', size=0, players=[]):
        self.name = name
        self.size = size
        self.players = players

    def add(self, player):
        self.players.append(player)
