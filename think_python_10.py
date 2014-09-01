# #  Exercise 1

# def nested_sum(parent_list):
# 	total = 0
# 	for i in parent_list:
# 		total += sum(i)
# 	print total
# 	return total

# nested_sum([[1,2,3,4],[5,6,7,8]])



# # Exercise 2

# def capitalize_all(t):
# 	res = []
# 	for s in t:
# 		res.append(s.capitalize())
# 	return res

# def capitalize_nested(t):
# 	""" 
# 	t: Nested parent_list
# 	Returns: Nested list
# 	"""
# 	for i in t:
# 		capitalize_all(i)

# def only_upper(t):
# 	res = []
# 	for s in t:
# 		if s.isupper():
# 			res.append(s)
# 	return res


# Exercise 3

# def list_sum(t):
# 	res = []
# 	tally = 0
# 	for s in t:
# 		tally += t[s-1]
# 		res.append(tally)
# 	print res
# 	return res

# list_sum([1, 2, 3, 4])



# Exercise 4

# def middle(t):
# 	del t[0]
# 	del t[-1]
# 	print t

# middle([1, 2, 3, 4])



# Exercise 6

# def is_sorted(t):
# 	original = t[:]
# 	# print original
# 	t.sort()
# 	# print t
# 	for i in range(len(t)):
# 		# print t[i]
# 		# print original[i]
# 		if t[i] != original[i]:
# 			print False
# 			return False
# 	print True
# 	return True	


# is_sorted([1, 2, 4, 5])


# Exercise 7

# def is_anagram(a, b):
# 	"""
# 	a: string
# 	b: string
# 	Returns: boolean
# 	"""
# 	if len(a) != len(b):
# 		return False
# 	else:
# 		a_list = list(a)
# 		a_list.sort()
# 		b_list = list(b)
# 		b_list.sort()	
# 		# print a_list
# 		# print b_list

# 	for i in range(len(a)):
# 		if a_list[i] != b_list[i]:
# 			print False
# 			return False
# 	print True
# 	return True


# is_anagram('heavy rain', 'hire anavy')


# Exercise 8

# import random

# def has_duplicates(t):
# 	"""
# 	t: list
# 	returns: boolean
# 	"""
# 	return len(t) != len(set(t))

# # has_duplicates([1, 1, 2, 3, 4])

# def birthday_paradox(n):
# 	yes_count = 0
# 	total_count = 0
# 	for total_count in range(0,10000):
# 		ages = []
# 		for i in range(0,n):
# 			r = random.randint(0, 365)
# 			ages.append(r)
# 		if has_duplicates(ages):
# 			yes_count +=1
# 	incidence = yes_count/float(total_count + 1)
# 	print incidence

# birthday_paradox(23)



# Exercise 9

# def remove_dumplicates(t):
# 	ans = []
# 	t.sort()
# 	print t
# 	for i in range(len(t)-1):
# 		if t[i] != t[i+1]:
# 			ans.append(t[i])
# 			print "ans = ",
# 			print t[i]
# 	print "final answer = ",
# 	print ans
# 	return ans

# remove_dumplicates([5, 4, 4, 3, 3, 2, 1, 1, 1, 1])


# Exercse 10

# import time

def create_list_append():
	fin = open('words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

# # create_list_append()

# def create_list_idiom():
# 	fin = open('words.txt')
# 	t = []
# 	for line in fin:
# 		word = line.strip()
# 		t = t + [word]
# 	return t

# start_time = time.time()
# t = create_list_idiom()
# elapsed_time = time.time() - start_time

# print len(t)
# print t[:10]
# print elapsed_time, 'seconds'


# Exercise 11:

def bisect(word):
	word_index = 0
	n = 0
	t = create_list_append()
	if word not in t:
		# print 'Please enter a correct word!'
		return
	high = len(t)
	low = 0
	while word_index == 0:
		n += 1
		i = (high + low) / 2
		# print i
		guess = t[i]
		# print 'guess', guess
		if word == t[i]:
			word_index = i
			# print n, 'attempts'
			# print 'word index is', word_index
			return word_index
		elif word > t[i]:
			low = i
		else:
			high = i


# bisect('words')


# Exercise 12

def reverse_word(word):
	new_word = word[::-1]
	return new_word


def reverse_pair_list():
	solution = []
	t = create_list_append()

	for i in t:
		pair = []
		# print i
		r = reverse_word(i)
		# print r
		if type(bisect(r)) == int:
			pair.append([i, r])
			solution.append(pair)

	print solution


reverse_pair_list()