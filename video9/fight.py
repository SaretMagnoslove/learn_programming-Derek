import random

class Warrior:
    def __init__(self, name, health=100):
        self.health = health
        self.name = name
    def attack(self):
        self.Damage = random.randint(1,10)
        print('{} attacks and deals {} points of damage...'.format(self.name,self.Damage))
def main():
    Lancelot = Warrior('Lancelot')
    Elric = Warrior('Elric')

    while True:
        Lancelot.attack()
        Elric.health -= Lancelot.Damage
        print('Elric\'s health is now',Elric.health)
        if Elric.health <= 0:
            print('Lancelot won - game over!')
            break
        Elric.attack()
        Lancelot.health -= Elric.Damage
        print('Lancelot\'s health is now',Lancelot.health)
        if Lancelot.health <= 0:
            print('Elric won - game over!')
            break

main()

