class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Soldier(Unit):
    def __init__(self, name, health, attack_power):
    #    super().__init__(self, name, health)
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack1(self, target2):
        target2.health -= self.attack_power
    def yron1(self, health, target2):
        health -= Archer.attack2(self, target2)
class Archer(Unit):
    def __init__(self, name, health, range_attack_power):
        #super().__init__(self, name, health)
        self.name = name
        self.health = health
        self.range_attack_power = range_attack_power
    def attack2(self, target):
        target.health -= self.range_attack_power
    def yron2(self, health, target):
        health -= Soldier.attack1(self, target)
def voyna(target, target2):
    target.attack1(target2)

def heal():
    heal1 = 25
    heal2 = 30
    if Soldier.health <= 0:
        Soldier.health += heal1
    if Archer.health <= 0:
        Archer.health += heal2


#unit1 = Unit("beluga", 100)
soldier1 = Soldier("sgvsc", 100,25)
archer1 = Archer("sxcbnmxc",100,20)
print(voyna(soldier1, archer1))