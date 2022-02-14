# Basic rock paper scissors program. I want the user to select from three options, rock paper or scissors, and then I want the computer to pick one of the three options at random. If the computer selects the same option as the player, the player will be prompted to choose again. If the player's option beats the computer's, the player wins, and vice versa. There will be a prompt to play again afterwards, allowing the user to continuously play while the program is open.

from random import choice

def new_game(): # Setting conditions for a new round
	user_wins = False
	computer_wins = False
	user_and_computer_draw = False
	users_choice = None
	computers_choice = None
	
possible_choices = {0:"Rock", 1:"Paper", 2:"Scissors"}

winner_messages = {0:"You won!", 1:"You lost...", 2:"It's a draw!"} #Game will draw if user and computer choose same throw

def try_again():
	while True:
		new_game_confirm = input("To play another round, enter 'y', or enter 'n' to close the program.\n")
		if new_game_confirm in ('y', 'n'):
			break
		print("Please enter 'y' or 'n'.")
	if new_game_confirm == 'y':
		new_game()
	else:
		print("Thanks for playing!")
		exit()

def win_conditions(user, computer):
	if users_choice == possible_choices[0]: # Player chooses rock
		if computers_choice == possible_choices[2]:
			user_wins = True
			print(winner_messages[0])
		elif computers_choice == possible_choices[1]:
			computer_wins = True
			print(winner_messages[1])
		else:
			user_and_computer_draw = True
			print(winner_messages[2])
	if users_choice == possible_choices[1]: # Player chooses paper
		if computers_choice == possible_choices[0]:
			user_wins = True
			print(winner_messages[0])
		elif computers_choice == possible_choices[2]:
			computer_wins = True
			print(winner_messages[1])
		else:
			user_and_computer_draw = True
			print(winner_messages[2])
	if users_choice == possible_choices[2]: # Player chooses scissors
		if computers_choice == possible_choices[1]:
			user_wins = True
			print(winner_messages[0])
		elif computers_choice == possible_choices[0]:
			computer_wins = True
			print(winner_messages[1])
		else:
			user_and_computer_draw = True
			print(winner_messages[2])

new_game()

while True:
	while True:
		users_choice = input("Please select an option below:\n 0) Rock\n 1) Paper\n 2) Scissors\n")
		try:
			users_choice = int(users_choice)
		except ValueError:
			users_choice = None
		if users_choice in possible_choices:
			break
		print("Please enter 0, 1, or 2.")
	users_choice = possible_choices[users_choice]
	print("You have chosen: {}".format(users_choice))
	computers_choice = choice(possible_choices)
	print("The computer has chosen: {}".format(computers_choice))
	win_conditions(users_choice, computers_choice)
	try_again()
