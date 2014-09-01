# Think Python Chapter 9

# Exercise 1

# def print_big_words():
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		if len(line) > 20:
# 			print word

# print_big_words()




# Exercise 2

# def has_no_e(word):
# 	"""Tests whether word does not contain an e

# 	word: string
# 	Returns: boolean
# 	"""

# 	for letter in word:
# 		if letter == 'e':
# 			# print False
# 			return False
# 	# print True
# 	return True

# def no_e_words():
# 	fin = open('words.txt')
# 	no_e_count = 0
# 	word_count = 0
# 	for line in fin:
# 		word = line.strip()
# 		word_count += 1
# 		if has_no_e(word):
# 			print word
# 			no_e_count += 1
# 	word_count = float(word_count)
# 	no_e_percentage = str(no_e_count / word_count)
# 	print 'Percentage of words without e: ' + no_e_percentage

# no_e_words()




# Exercise 3

# def avoids(word, forbidden):
# 	"""Returns True if forbidden string not in word.  Otherwise false

# 	word: string
# 	forbidden: string

# 	Returns: boolean
# 	"""

# 	if forbidden in word:
# 			# print False
# 			return False
# 	# print True
# 	return True

# def allowed_word_percentage(forbidden_string):
# 	"""Returns percentage of words not containing forbidden string

# 	forbidden_string: string

# 	Returns: float
# 	"""

# 	fin = open('words.txt')
# 	allowed_word_count = 0
# 	word_count = 0
# 	for line in fin:
# 		word = line.strip()
# 		word_count += 1
# 		if avoids(word, forbidden_string):
# 			# print word
# 			allowed_word_count += 1
# 	word_count = float(word_count)
# 	allowed_percentage = str(allowed_word_count / word_count)
# 	print 'Percentage of words without forbidden string: ' + allowed_percentage



# Exercise 4

# def character_list(character_string):
# 	""" Creates set of allowed characters from string

# 	character_string: string

# 	Returns: list (set)
# 	"""

# 	chars = []

# 	for n in character_string:
# 		chars.append(n)
# 	chars = list(set(chars))

# 	# print chars
# 	return chars

# character_list('acefhlo')
	
# def uses_only(word, allowed_string):
# 	""" Returns True if word only uses letters from allowed string

# 	word: string
# 	allowed_string: string

# 	Returns: boolean
# 	"""
# 	allowed_chars = character_list(allowed_string)

# 	for c in word:
# 		if c not in allowed_chars:
# 			# print c
# 			return False
# 	# print True
# 	return True

# def limited_allowed_language(allowed_letters):
# 	"""Takes strings allowed in language and returns all words including only those letters

# 	allowed_letters: string

# 	returns: list
# 	"""
# 	new_language = []

# 	fin = open('words.txt')
	
# 	for line in fin:
# 		word = line.strip()
# 		if uses_only(word, allowed_letters):
# 			new_language.append(word)
# 	print new_language
# 	return new_language

# limited_allowed_language('acefhlo')


# Exercise 6:


# def uses_all(word, required_string):
# 	"""Returns True if word contains all required letters

# 	word: string
# 	required_letters: string

# 	Returns: boolean
# 	"""
# 	string_list = character_list(word)

# 	required_list = character_list(required_string)
# 	# print required_list

# 	for i in required_list:
# 		# print i
# 		if i not in string_list:
# 			# print False
# 			return False
# 	# print True
# 	return True

# def limited_required_language(required_letters):
# 	"""Returns list of words using all required characters

# 	required_letters: string

# 	returns: list
# 	"""
# 	new_language = []

# 	fin = open('words.txt')
	
# 	for line in fin:
# 		word = line.strip()
# 		if uses_all(word, required_letters):
# 			new_language.append(word)
	
# 	print new_language
# 	return new_language

# def required_language_count(required_letters):
# 	"""Counts number of words in language limited to words containing required letters

# 	language = list

# 	returns: integer
# 	"""
# 	language = limited_required_language(required_letters)
# 	print len(language)
# 	return len(language)

# required_language_count('aeiouy')




# Exercise 7

# def is_triple_double(word):
# 	i = 0
# 	while i < (len(word) - 5):
# 		if (word[i] == word[i+1] and 
# 			word[i+2] == word[i+3] and
# 			word[i+4] == word[i+5]):
# 			return True
# 		i += 1
# 	return False

# def puzzler():
# 	solution = []
# 	fin = open('words.txt')

# 	for line in fin:
# 		word = line.strip()
# 		if is_triple_double(word):
# 			solution.append(word)
# 	print solution
# 	return solution

# puzzler()




# Exercise 8

# def is_palindrome(word):
# 	# print word == word[::-1]
# 	return word == word[::-1]


# def puzzler_palindrome():
# 	solution = []
# 	for i in range(100000,999999):
# 		first = str(i)
# 		second = str(i + 1)
# 		third = str(i + 2)
# 		fourth = str(i + 3)
# 		if (is_palindrome(first[-4:]) and
# 			is_palindrome(second[-5:]) and
# 			is_palindrome(third[1:-1]) and
# 			is_palindrome(fourth)):
# 			solution.append(i)
# 			print solution
# 			return solution

# puzzler_palindrome()



# Exercise 9

# Note - would 

def puzzler_ages():
	"""Note - would want to refactor into several general formulas for:
	- Filling in string based on difference in length of digits
	- Reversing strings (just for True or False)
	- Conducting count
	- Check for count = 8
	"""
	solution = []
	n = 1
	i = 0
	
	for n in range(0, 100):
		count = 0
		for i in range(0,100):
			j = i + n
			i_age = str(i)
			j_age = str(j)
			difference = len(j_age) - len(i_age)

			if difference > 0:
				i_age = i_age.zfill(difference + 1)

			if i_age == j_age[::-1]:
				count += 1
x			i += 1

		if count == 8:
			solution.append(n)

		n += 1

	print solution

puzzler_ages()
