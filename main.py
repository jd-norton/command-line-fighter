from villians import villain
import random

YourHealth = 100
YourAttack = 25
SpecialAttackCounter = 0
SpecialAttack = 0
Defense = False
BattleOver = False
DamagePotion = 3
HealingPotion = 3

#assigning a villain
villain1 = random.choice(["Frog", "Tornado", "Dragon"])

if villain1 == "Frog":
    villain1 = villain("Frog", 50, 30)
elif villain1 == "Tornado":
    villain1 = villain("Tornado", 100, 40)
else:
    villain1 = villain("Dragon", 200, 50)




def BattleAttack():

    global YourAttack
    global BattleOver
    
    villain1.health -= YourAttack
    print ("Your attack is", YourAttack)

    if villain1.health > 0:
        print(villain1.name, "'s health is now", villain1.health)
    else:
        print(villain1.name, "'s health is now 0. Congratulations! you win!!!")
        BattleOver = True

    if YourAttack > 25:
        YourAttack = 25

def BattleDefense():
    
    print("You are in defensive mode")
    global Defense
    Defense = True

def BattlePotions():

    global HealingPotion
    global DamagePotion
    global YourHealth
    global YourAttack

    print("(1).Health Potion(",HealingPotion, ")\n(2).Damage(",DamagePotion, ")\n(B)Back")
    Potion = input("What Potions would you like to use?\n") 
    if Potion == "1" or Potion == "Health Potion" or Potion == "health potion":
        if HealingPotion > 0:
            YourHealth += 50
            HealingPotion -=1
            print("Your health is now", YourHealth)
            print("You now have", HealingPotion, "Healing Potion/s")
            BattlePotions()
        else:
            print("Sorry, you don't have anymore healing potions")
            BattlePotions()
    elif Potion == "2" or Potion == "Damage Potion" or Potion == "damage potion":
        if DamagePotion > 0:
            YourAttack += 10
            DamagePotion -=1
            print("Your attack is now", YourAttack)
            print("You now have", DamagePotion, "Damage Potion/s")
            BattlePotions()
        else:
            print("Sorry, you don't have anymore damage potions")
            BattlePotions()
    elif Potion == "B" or Potion == "Back" or Potion == "b":
        BattleStatus()
    else:
        print("INVALID INPUT, PLEASE TRY AGAIN")
        
def BattleSpecialAttack():

    global SpecialAttackCounter
    global SpecialAttack
    global YourAttack
    
    if SpecialAttackCounter % 4 == 0 and SpecialAttackCounter != 0:
        SpecialAttack += 1
        
    if SpecialAttack > 0:
        PlayerChoice = input("Your special ability is active. Do you want to use it? (Y) OR (N)")
        if PlayerChoice == "Yes" or PlayerChoice == "yes" or PlayerChoice == "Y" or PlayerChoice == "y":
            SpecialAttack -=1
            YourAttack *= 3
            BattleAttack()
            BattleVillainAttack(Defense)
        elif PlayerChoice == "No" or PlayerChoice == "no" or PlayerChoice == "N" or PlayerChoice == "n":
            print("You can use you special next turn if you want")
        else:
            print("INVALID INPUT, PLEASE TRY AGAIN")


    
def BattleStatus():
            
    print("You are fighting a(", villain1.name , " ", villain1.health,"HP)")
    print("What do you want to do? Your Health:", YourHealth)
    BattleMove = input("(1).Attack" + "\n(2).Defend" + "\n(3).Potions\n")

    if BattleMove == "1" or BattleMove == "Attack" or BattleMove == "attack":
        BattleAttack()
    elif BattleMove == "2" or BattleMove == "Defend" or BattleMove == "defend":
        BattleDefense()
    elif BattleMove == "3" or BattleMove == "Potions" or BattleMove == "Potions":
        BattlePotions()
    else:
        print("INVALID INPUT, PLEASE TRY AGAIN")
        BattleStatus()

#villain method
def BattleVillainAttack(Defense):

    global YourHealth
    global BattleOver

    if BattleOver == False:
        if Defense == True:
            print("The ", villain1.name, " attacks, but you are defending")
            YourHealth -= (villain1.attack / 2)
        else:
            print("The ", villain1.name, " attacks! and deals", villain1.attack, "damage")
            YourHealth -= villain1.attack

        if YourHealth >0:
            print("Your health is now", int(YourHealth))
        else:
            print("Your health is 0. Game over")
            BattleOver = True
    
while BattleOver == False:

    BattleSpecialAttack()

    if BattleOver == False:
        BattleStatus()

    if BattleOver == False:
        BattleVillainAttack(Defense)

    SpecialAttackCounter += 1
