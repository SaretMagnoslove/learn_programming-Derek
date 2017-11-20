import random

class Warrior:
    def __init__(self,name='warrior',health=0,maxdamage=0,maxblock=0):
        self.name = name
        self.health = health
        self.maxdamage = maxdamage
        self.maxblock = maxblock
    def attack(self):
        damage = random.randint(1,self.maxdamage)
        return damage
    def block(self):
        block = random.randint(1,self.maxblock)
        return block
class Battle:
    def startfight(self,warrior1,warrior2):
        while True:
            if self.getattackresult(warrior1,warrior2) == 'Game Over':
                print('Game Over')
                break
            if self.getattackresult(warrior2,warrior1) == 'Game Over':
                print('Game Over')
                break
    @staticmethod
    def getattackresult(warriorA,warriorB):
        warriorAdamage = warriorA.attack()
        warriorBblock = warriorB.block()
        damage2warriorB = warriorAdamage-warriorBblock
        if damage2warriorB <0: damage2warriorB = 0
        warriorB.health -= damage2warriorB

        print('{} attacks {} and deals {} damage'.format(warriorA.name,warriorB.name,
        damage2warriorB))
        print('{} is down to {} health'.format(warriorB.name,warriorB.health))

        if warriorB.health <= 0:
            print('{} had Died and {} is victorious'.format(warriorB.name,
            warriorA.name))
            return "Game Over"
        else:
            return "...and battle is on..."
def main():
    maximus = Warrior('Maximus',50,20,10)
    galaxion = Warrior('Galaxion',50,20,10)

    battle = Battle()
    battle.startfight(maximus,galaxion)

main()







    