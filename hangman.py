
import random

DB_PATH = "./files/data.txt"



def load_db():
	with open(DB_PATH, "r", encoding = "utf-8") as f:
		words = [word for word in f]

	return words


def display_interface(word_state):
	print("HANGMAN GAME" + "\n")
	print(word_state)



def pick_random_word(words):
	random_index = random.randrange(0,len(words),1)
	return words[random_index]

def get_letter_list(word):
	return [word[i] for i in range(len(word))]

def check_input(word_to_play, word_state, input_letter, blank_count):
	letter_found = False
	for index in range(len(word_to_play)):
		if input_letter == word_to_play[index]:
			word_state[index] = input_letter
			letter_found = True
			blank_count = blank_count - 1

	return {"state" : word_state, "result": letter_found, "spaces": blank_count}


def game_session():
	attemps = 10
	words = load_db()

	word_to_play = pick_random_word(words).strip()
	word_to_play = get_letter_list(word_to_play)
	word_state = ["_" for i in range(len(word_to_play))]
	print(str(word_state) + "\n")
	blank_count = len(word_state)
	print("empty spaces: " + str(blank_count))

	IS_COMPLETED = False
	while (attemps > 0) and ( not IS_COMPLETED ):
		input_letter = str(input())
		output = check_input(word_to_play, word_state, input_letter, blank_count)
		blank_count  = output["spaces"]
		if output["result"] == False:
			attemps = attemps - 1
		print("empty spaces: " + str(output["spaces"] ))

		if output["spaces"] == 0:
			IS_COMPLETED = True

		print("Attemps: " + str(attemps))
		display_interface(output["state"])





def main():
	game_session()

if __name__ == '__main__':
	main()