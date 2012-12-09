import random

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)
player_input = raw_input("rock, paper, or scissors? ")
player_choice = player_input.lower()

def game():
	
	global computer_choice
	global player_choice

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
	else:
		print False

game()
