#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

### If you're going to make use of this piece of code, it's ok, just, If you want to make me feel proud of my work, make sure you add a comment above this code (Like this one) mentioning my username, something like "guekho64", so if for coincidence I find your project and read its source code, it'll feel great to read that line of code! (It really doesn't matter if you only add my username alone or with extra text, it'll be good anyways :D) ###

import random

class Funcs():
	def __init__(self):
		self.max = 5
	def round(self, a):
		var = list(self.modifier(float(a)))
		self.modifier2(var)
		self.modifier3(var)
		return int(float(str(''.join(str(e) for e in var))))			
	def modifier(self, a):
		for i in str(a):
			if str(i) == '.':
				yield str(i)
			else:
				yield int(i)
	def modifier2(self, a, counter=0):
		for i in a:
			if i != '.':
				counter += 1
			else:
				break
		for i in reversed(a):
			if len(a) == counter+1:
				break
			elif i == '.':
				pass
			elif i < self.max:
				a.pop(-1)
			elif i >= self.max:
				a.pop(-1)
				if a[-1] == '.':
					a[-2] += 1
				else:
					a[-1] += 1
	def modifier3(self, a):
		for i in a:
			if i >= 10:
				if a[0] is 10:
					break
				else:
					return self.modifier4(a)
	def modifier4(self, a, l=[], n=[]):
		for i in reversed(a):
			try:
				a[(n.pop(-1)-1)] += l.pop(-1)
				return self.modifier3(a)
			except:
				if i == '.':
					pass
				elif i >= 10:
					l.append(1)
					n.append(a.index(i))
					a[a.index(i)] = 0
				elif i < 10:
					l.append(0)
					
if __name__ == '__main__':
	#Just as an example
	Functions = Funcs()
	random = random.random()*(random.random()*1000)
	print "Original:%s" % str(random)
	print "Result:%s" % str(Functions.round(random))
