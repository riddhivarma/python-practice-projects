print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('In which direction would you like to go? Type "Left" or "Right" : ').lower()
if choice1=="left":
    choice2 = input('You have now reached the sea. There is an island in the middle of sea. Would you like to '
                           'swim through the sea, or wait for a boat? Type "Swim" or "Wait" : ').lower()
    if choice2== "swim":
        print("Game Over! The great crocodile has eaten you.")
    elif choice2== "wait":
        print("You got the boat and now have reached the island. There are 3 great doors in front of you.")
        choice3=input('Which colour door would you like to open? Type "Red", "Yellow" or "Blue" : ').lower()
        if choice3=="red":
            print("Oops! You died of poisonous air. Game Over!")
        elif choice3=="yellow":
            print("Omg you found the treasure. Congrats babygirl, YOU WIN!")
        elif choice3=="blue":
            print("Oops! The Dementor is waiting for you here. Game Over.")
        else:
            print("This colour door is not present!")
    else:
        print("This mode of travel is not available.")
elif choice1=="right":
    print("Oh No! You fell in the large hole, Game Over!")
else:
    print("Invalid direction")


