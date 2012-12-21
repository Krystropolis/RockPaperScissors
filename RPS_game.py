import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

def game():
	global computer_choice

	player_choice = raw_input("rock, paper, or scissors? ").lower()

	if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
		print "That is not a valid choice."
		game()
	else:
		if player_choice == computer_choice:
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "TIE!"
		elif player_choice == "rock" and computer_choice == "paper":
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "The computer won! :("
		elif player_choice == "rock" and computer_choice == "scissors":
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "You won! :)"
		elif player_choice == "paper" and computer_choice == "rock":
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "You won! :)"
		elif player_choice == "paper" and computer_choice == "scissors":
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "The computer won! :("
		elif player_choice == "scissors" and computer_choice == "paper":
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "You won! :)"
		elif player_choice == "scissors" and computer_choice == "rock":
			print "You chose " + player_choice + "."
			print "The computer chose " + computer_choice + "."
			print "The computer won! :("

game()
