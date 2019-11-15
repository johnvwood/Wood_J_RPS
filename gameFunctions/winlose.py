from random import randint
from gameFunctions import gamelives

def winorlose(status):
	#print("called win or lose")
	print("************************")
	
	print("You", status, "!!!!! Would you like to try again?")
	
	choice = input("y / n ")
	#print(choice)

	if (choice == "n"):
		print("You chose to quit.")
		exit()

	elif (choice == "y"):

		gamelives.player_lives = 3
		gamelives.computer_lives = 3
		gamelives.total_lives = 3
		gamelives.player = False
		gamelives.computer = gamelives.choices[randint(0,2)]

	else: 
		print("Make a valid choice please.")
		winorlose(status)

	