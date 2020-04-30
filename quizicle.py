import random

class Card:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

class Quiz:
	def __init__(self, cards):
		self.cards = cards
		self.correct = 0
		self.question_count = 0

def phil_cards():
	cards = [
		Card("What is Phil's favorite color?", "Blue..no, Green!"),
		Card("What is Phil's favorite movie?", "Fight Club"),
		Card("What is Phil's favorite band?", "The Neighborhood"),
		Card("What is Phil's favorite sport?", "Lacrosse"),
		Card("What did Phil study in college?", "Economics"),
		Card("Where did Phil grow up?", "Ohio"),
		Card("Where did Phil go to College?", "University of Kentucky"),
		Card("True or False, Phil drive Conan O'Brien's Porsche?", "True")
	]
	return cards

def math_cards():
	cards = [
		Card("2 + 2 =", "4"),
		Card("2 - 2 =", "0"),
		Card("2 * 2 =", "4"),
		Card("2 / 2 =", "1"),
		Card("2 ^ 2 =", "4")
	]
	return cards

def random_question(cards):
	card = random.choice(cards)
	print(card.question)
	response = raw_input('answer: ')
	if response.lower() == card.answer.lower():
		print("Correct!")
	else:
		print("Incorrect, the answer is: // % s //"% card.answer)

def start_quiz(cards):
	cards = cards
	quiz = Quiz(cards)
	while cards:
		card = random.choice(cards)
		print(card.question)
		response = raw_input('answer: ')
		if response.lower() == card.answer.lower():
			quiz.correct += 1
			print("Correct!")
		else:
			print("Incorrect, the answer is: // % s //"% card.answer)
		quiz.question_count += 1
		new_cards = cards.remove(card)
		start_quiz(new_cards)
		print("You got % s out of % s correct"% (quiz.correct, quiz.question_count))
	return
	# Using the line below will print '0 correct' for each iteration, but also print the correct total at the end
	# print("You got % s correct"% quiz.correct)

# random_question(phil_cards())
start_quiz(math_cards())
