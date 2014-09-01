# def countdown_recursive(n):
# 	if n <= 1:
# 		print 'Blastoff!'
# 	else:
# 		print n
# 		countdown(n-1)

# def countdown_while(n):
# 	while n > 0:
# 		print n
# 		n = n - 1
# 	print 'Blastoff!'

# countdown_while(2)


# import math

# def sqrt_Newton(a, x):
# 	y = 0
# 	epsilon = 0.001
# 	while True:
# 		print x
# 		y = (x + a/x) / 2
# 		if abs(y-x) < epsilon:
# 			x = y

# sqrt_Newton(4, 3)

# def traversal_practice(word):
# 	index = 0
# 	while index < len(word):
# 		letter = word[index]
# 		print letter
# 		index = index + 1

# def backwards(word):
# 	index = len(word) - 1
# 	while index >= 0:
# 		letter = word[index]
# 		print letter
# 		index = index - 1

# backwards('word')

# def duck_names():
# 	prefixes = 'JKLMNOPQ'
# 	suffix = 'ack'
# 	for letter in prefixes:
# 		if letter == 'Q' or letter == 'O':
# 			print letter + "u" + suffix
# 		else:
# 			print letter + suffix

# duck_names()

# def slice_test(word):
# 	print word[:]

# slice_test('Pechman')

# def letter_count(word, letter):
# 	count = word.count(letter)
# 	print count

# letter_count("banana","b")

# def count(word, substring):
# 	index = word.count(substring)
# 	print index

# count('banana', 'a')


# def rotate_word(word, integer):
# 	"""Rotates each letter in the word by 'integer' number of places.

# 	TODO: Handle upper case, lower case and other characters
# 	"""
# 	new_word = ''
# 	for letter in word:
# 		new_letter = chr(ord(letter) + integer)
# 		new_word = new_word + new_letter
# 	print new_word

# rotate_word('cheer', 7)

def rotate_letter(letter, n):
	"""Rotate letter by n places.  Does not change other characters

	letter: single-letter string
	n: int

	Returns: single-letter string
	"""
	if (not isinstance(n, int) or 
		not isinstance(letter, str) or 
		len(letter) > 1):
		print "Error: Fix your inputs!!"
		return

	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		# print letter
		return letter

	c = ord(letter) - start
	i = (c + n) % 26 + start
	# print chr(i)
	return chr(i)

def rotate_word(word, n):
	"""Rotates all letters in word by n places.  Does not change other character

	word: string
	n: integer

	Returns: string
	"""

	if (not isinstance(n, int) or not isinstance(word, str)): 
			print "Error: Fix your inputs!!"
			return

	new_word = ''

	for letter in word:
		new_letter = rotate_letter(letter, n)
		new_word = new_word + new_letter
	print new_word
	return new_word

rotate_word('Cheer', 7)