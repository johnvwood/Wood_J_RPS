from random import randint
from gameFunctions import winlose, gamelives

while gamelives.player is False:


	print("************************")
	print("FIGHT ALLEN THE UNDEFEATED IN RPS\n\n")
	print("Your lives:", gamelives.player_lives, "/", gamelives.total_lives, "\n")
	print("Allen's lives:", gamelives.computer_lives, "/", gamelives.total_lives, "\n")
	print("************************")

	player = input("Type rock, paper or scissors\n\n")
	player == player.lower()
	
	print("------------------")
	print("You chose ", player, "\n")	
	print("Allen chose ", gamelives.computer)
	print("------------------")

	if player.lower() == "quit":
		exit()
	elif gamelives.computer == player:
		print("Tie.\n")


	elif player.lower() == "paper":
		if gamelives.computer == "scissors":
			print("Haha you suck. Allen's", gamelives.computer, "sliced your pathetic", player, ".", "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You got lucky. Your", player, "blinded Allen's", gamelives.computer, "and caused it to implode.", "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	elif player.lower() == "scissors":
		if gamelives.computer == "rock":
			print("Unfortunately, Allen's antique", gamelives.computer, "decimated your", player, ".", "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You won fare and square. Your", player, "slaughtered Allen's weak", gamelives.computer, ".", "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	elif player.lower() == "rock":
		if gamelives.computer == "paper":
			print("Are you even trying? Allen's stealthy", gamelives.computer, "assasinated your clumsy", player, ".", "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("Congratulations, you win. Your", player, "vibed on Allen's", gamelives.computer, ".", "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1
	else:
		print("That aint a valid choice buddy.")


	if gamelives.player_lives == 0:
		winlose.winorlose("lose")
		
	elif gamelives.computer_lives == 0:
		winlose.winorlose("won")

	else:
		gamelives.player = False
		gamelives.computer = gamelives.choices[randint(0,2)]

		