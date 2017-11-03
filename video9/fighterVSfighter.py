# fighter VS fighter Dundgeon And Dragons Style

import random

class fighter:
    def __init__(self,name,HP = 14,AC=4,THACO=17,MaxDamage=8):
        self.name = name
        self.HP = HP
        self.AC = AC
        self.THACO = THACO
        self.MaxDamage = MaxDamage
    def attack(self):
        attack = random.randint(1,20)
        damage = random.randint(1,self.MaxDamage)
        return (attack, damage)
class Battle:
    def StartFight(self,fighter1,fighter2):
        while True:
            if self.GetAttackResult(fighter1,fighter2) == 'Game Over':
                print('Game Over')
                break
            if self.GetAttackResult(fighter2,fighter1) == 'Game Over':
                print ('Game Over')
                break
    @staticmethod
    def GetAttackResult(fighterA,fighterB):
        fighterAattack,fighterAdamage = fighterA.attack()
        if fighterAattack > fighterA.THACO - fighterB.AC:
            fighterB.HP -= fighterAdamage
            print('{} hit and deals {} damage'.format(fighterA.name,fighterAdamage))
            print('{} is down to {} HP'.format(fighterB.name,fighterB.HP))
        else:
            print ('{} misses'.format(fighterA.name))
        if fighterB.HP <= 0:
            print ('{} had Died'.format(fighterB.name))
            return 'Game Over'
        else:
            print ('...and the battle continues...')
def main():
    Lancelot = fighter(name='Lancelot')
    Galahad = fighter(name='Galahad')

    battle = Battle()
    battle.StartFight(Lancelot,Galahad)

main()

        


