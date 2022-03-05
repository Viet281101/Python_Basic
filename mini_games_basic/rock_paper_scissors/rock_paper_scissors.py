
import random


def play():
	user = input("What's your choice? R' for rock, 'P' for paper, 'S' for scissors\n").lower()
	computer = random.choice(['r', 'p', 's'])

	if user == computer:
		return 'It\'s a tie'


	## 	R > S 	;	 S > P 	;	 P > R
	if is_win(user, computer):
		return 'You won!'

	return 'You lost!'


def is_win(player, opponent):
	# return true if player wins
	if (player == 'r' and opponent == 's') \
		or (player == 's' and opponent == 'p') \
		or (player == 'p', and opponent == 'r'):
			return True


def main():
	print(play)




if __name__ == '__main__':
	main

