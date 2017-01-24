#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random

class Funcs():
	def __init__(self):
		self.max = 5
	def round(self, a):
		var = list(self.modifier(float(a)))
		self.modifier2(var, 1)
		self.modifier3(var)
		return self.format(var)
	def modifier(self, a):
		for i in str(a):
			try:
				yield int(i)
			except ValueError:
				yield str(i)
	def modifier2(self, a, max=False):
		int_counter, float_counter = (False, False)
		if max <= 0:
			max = False
		for i in a:
			if i != '.':
				int_counter += 1
			else:
				break
		for i in reversed(a):
			if i != '.':
				float_counter += 1
			else:
				break
		for i in reversed(a):
			if len(a) == int_counter+1:
				break
			elif i == '.':
				pass
			elif i < self.max:
				if max:
					if int_counter+max+1 >= len(a):
						break
					else:
						a.pop(-1)
				else:
					a.pop(-1)
			elif i >= self.max:
				if max:
					if int_counter+max+1 >= len(a):
						break
					else:
						a.pop(-1)
						if a[-1] == '.':
							a[-2] += 1
						else:
							a[-1] += 1
				else:
					a.pop(-1)
					if a[-1] == '.':
						a[-2] += 1
					else:
						a[-1] += 1
			print a                    
	def modifier3(self, a):
		for i in a:
			if i >= 10:
				if a[0] is 10:
					break
				else:
					return self.modifier4(a)
	def modifier4(self, a, l=list(), n=list()):
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
	def format(self, a):
		int_counter, float_counter = (False, False)
		var = list(self.modifier(float(str(str().join(str(e) for e in a)))))
		for i in a:
			if i != '.':
				int_counter += 1
			else:
				break
		for i in reversed(a):
			if i != '.':
				float_counter += 1
			else:
				break
		if float_counter:
			return float(str(str().join(str(e) for e in a)))
		else:
			return int(float(str(str().join(str(e) for e in a))))
if __name__ == '__main__':
	#Just as an example
	Functions = Funcs()
	random = float(random.random()*100)
	print "Original:%s" % str(random)
	print "Result:%s" % str(Functions.round(random))
