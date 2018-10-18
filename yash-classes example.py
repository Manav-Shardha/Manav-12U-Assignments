class Monster:

    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health

    def fight(self, other):
        global hit
        if self.health > 0:
            while self.health >= 0 and other.health >= 0:
                hit = (self.attack-other.defense)
                other.health -= hit
                print(str(self.name) + " did " + str(hit) + " damage to " + str(other.name), "\n")
                '''if hit <= 0:
                    hit = 0
                    print(str(self.name) + " did 0 damage to " + str(other.name))
                else:
                    pass'''
        else:
            print(str(other.name) + " wins, it has " + str(other.health) + " health left!")



ogre = Monster("Ogre", 3, 0, 5)
gary = Monster("Gary", 5, 4, 8)
for counter in range(1):
    x = gary.fight(ogre)
    y = ogre.fight(gary)
