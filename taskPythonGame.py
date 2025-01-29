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
#A game creation that gives you a story line on your choices..
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#transform to lowerCase
winnerCard = 'You win'
gameoverMessage = "Fall into hole. Game Over"
questionOne = input("Choose left or Right").lower()
if(questionOne == 'right'):
    print(gameoverMessage)
elif(questionOne == 'left'):
    questionTwo = input("Swim or wait").lower()
    #print('Welcome to stage Two')
    if(questionTwo == 'wait'):
        print('welcome to stage 3')
        chooseDoor = input("Choose a door between Red, Yellow or Blue.. Think wisely ... :)").lower()
        if(chooseDoor == 'blue'):
            print(winnerCard)
        elif(chooseDoor == 'red'):
            print('Burned by fire. Game over')
        elif(chooseDoor == 'yellow'):
            print('Eaten by beasts. Game Over.')
        else:
            print(gameoverMessage)

    else:
        print(gameoverMessage)

else:
    print(gameoverMessage + 'why::****')




