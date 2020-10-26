class PlayerOne:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Weapons:
    def __init__(self, swordtype, swordattack, armor):
        self.swordtype = swordtype
        self.swordattack = swordattack
        self.armor = armor

class Potions:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

'''
YourAttack = 25

def itsasword():
    weapons = ["Wooden Sword", "Bronze Sword", "Iron Sword", "Steel Sword", "Steel Greatsword"]

    global YourAttack
    swordtype = ""

    for i in weapons[4]:
        if i == 0:
            swordtype = weapons[i]
            YourAttack += 25
            i += 1
        elif i == 1:
            swordtype = weapons[i]
            YourAttack += 25
            i += 1
        elif i == 2:
            swordtype = weapons[i]
            YourAttack += 25
            i += 1
        elif i == 3:
            swordtype = weapons[i]
            YourAttack += 25
            i += 1
        else:
            swordtype = weapons[i]
            YourAttack += 25
            i += 1
    return swordtype

for i in range(5):
    print(itsasword(), YourAttack)
'''   