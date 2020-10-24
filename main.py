YourHealth = 100
DragonHealth = 200
YourAttack = 25
DragonAttack = 50
SpecialAttackCounter = 0
SpecialAttack = 0
Defense = False
BattleOver = False
DamagePotion = 3
HealingPotion = 3

def BattleAttack():

    global YourAttack
    global DragonHealth
    global BattleOver
    
    DragonHealth -= YourAttack
    print ("Your attack is", YourAttack)

    if DragonHealth > 0:
        print("Dragons health is now", DragonHealth)
    else:
        print("Dragons health is now 0. Congratulations! you win!!!")
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
            BattleDragonAttack(DragonAttack, Defense)
        elif PlayerChoice == "No" or PlayerChoice == "no" or PlayerChoice == "N" or PlayerChoice == "n":
            print("You can use you special next turn if you want")
        else:
            print("INVALID INPUT, PLEASE TRY AGAIN")


    
def BattleStatus():

    global DragonHealth
            
    print("You are fighting the great Dragon Maculon(",DragonHealth,"HP)")
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

def BattleDragonAttack(DragonAttack, Defense):

    global YourHealth
    global BattleOver

    if BattleOver == False:
        if Defense == True:
            print("The dragon attacks, but you are defending")
            YourHealth -= (DragonAttack / 2)
        else:
            print("The dragons attacks! and deals", DragonAttack, "damage")
            YourHealth -= DragonAttack

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
        BattleDragonAttack(DragonAttack, Defense)

    SpecialAttackCounter += 1
