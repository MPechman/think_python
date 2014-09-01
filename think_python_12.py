# Exercise 1

def sumall(*args):
	ans = sum(args)
	print ans

# sumall(1, 2, 3, 4)


# s = 'abc'
# t = [0, 1, 2]
# t = zip(s, t)
# print t
# for letter, number in t:
# 	print letter, number

# for index, element in enumerate('abc'):
# 		print index, element

# Exercise 2

def create_language():
	t = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	# print t[:10]
	return t

# create_language()

import random

def sort_by_length(words):
    t = []
    for word in words:
    	t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

# Exercise 3

def make_histogram(s):
	d = dict()
	for c in s:
		c = c.lower()
		d[c] = d.get(c, 0) + 1
	return d

def most_frequent(s):
	d = make_histogram(s)
	t = []
	for x, freq in d.iteritems():
		t.append((freq, x))
	print t

	t.sort(reverse = True)


	res = []
	for freq, x in t:
		res.append(x)
	print res
	return res

# most_frequent('This is just a test')


# Exercise 4

def anagram_dictionary():
	language = create_language()
	# language = language[:10000]
	# language = ['retainers', 'ternaries']

	d = dict()
	for word in language:
		key = tuple(sorted(word))
		val = [word]
		# print val

		if key in d:
			temp = d[key]
			# print temp
			temp.append(word)
			# print temp
			d[key] = temp
		else:
			d[key] = val
	
	# print d[key]
	# print d
	return d

# anagram_dictionary()

def anagrams():
	res = []
	d = anagram_dictionary()
	for v in d.values():
		if len(v) > 1:
			res.append(v)
	# print res
	return res

# anagrams()

def anagrams_ordered():
	d = anagram_dictionary()

	res = []
	for v in d.values():
		if len(v) > 1:
			res.append((len(v), v))

	res.sort(reverse = True)

	for x in res:
		print x

# anagrams_ordered()

def filter_length(n):
	res = {}
	t = anagrams()
	print t
	# for signature, words in t:
	# 	if len(signature) == n:
	# 		res[signature] = words
	# print res

filter_length(8)