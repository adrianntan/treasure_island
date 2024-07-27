print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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


choice_fork = input("You find yourself at a crossroads. Where do you want to go? Type 'left' or 'right'\n").lower()
if choice_fork == "right":
          print("You fell into a trap door. Game over.")
elif choice_fork == "left":
          choice_river = input("You reach a raging river! You can either cross to the other side by swimming or wait for a boat. Do you want to swim or wait? Type 'swim' or 'wait'\n").lower()
          if choice_river == "swim":
                    print("You are attacked by multiple piranhas and drown. Game over.")
          elif choice_river == "wait":
                    print("You make it through the river unharmed and say goodbye to the kind sailor.")
                    choice_door = input("In front of you now is a house with three doors in different colors. Pick one to walk through. Type 'red', 'blue', or 'yellow'\n.").lower()
                    if choice_door == "red":
                              print("You walk into a burning room and are unable to get out. Game over.")
                    elif choice_door == "blue":
                              print("You walk into a room full of hungry beasts and get eaten. Game over.")
                    elif choice_door == "yellow":
                              print("You walk into a room full of treasure! You win!")
                    else:
                              print("You walk through a nonexistent door and find yourself in the void. Game over.")
          else:
                    print("You turn into a skeleton. Game over.")
else:
          print("You continue to walk in circles in the chosen direction and lose your mind. Game over.")