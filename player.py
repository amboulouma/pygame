from point import Point


class Player:
    def __init__(self, name='', team='', position=Point(0, 0, 0), health=100, mana=0, time=0, score=0, best_score=0):
        self.name = name
        self.team = team
        self.position = position
        self.health = health
        self.mana = mana
        self.time = time
        self.score = score
        self.best_score = best_score

    def __str__(self):
        return "Player({}, {}, {}, {})".format(self.name, self.team, self.health, self.position)

    def move(self, destination=Point(0, 0, 0)):
        self.position = destination

    def rest(self, time):
        self.time -= time
        self.mana += time*TIME_TO_MANA

    def attack(self, attack, player):
        self.mana -= ATTACK_TO_MANA[attack]
        self.time -= ATTACK_TO_TIME[attack]
        player.health -= ATTACK_TO_TIME[attack]
