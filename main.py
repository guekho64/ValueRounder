#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random
class Funcs():
	class Rounder():
		def __init__(self):
			self.limit = 10
			self.max= 5
		def round(self, a, dec):
			var = list(self.modifier(float(a)))
			self.modifier2(var, dec)
			self.modifier3(var)
			if dec:
				return float(str(str().join(str(e) for e in var)))
			else:
				return int(float(str(str().join(str(e) for e in var))))
		def modifier(self, a):
			for i in str(a):
				try:
					yield int(i)
				except ValueError:
					yield str(i)
		def modifier2(self, a, max=int(), negative=-1):
			int_counter, decimal_counter = (0, 0)
			if max <= 0:
				max = 0
			for i in a:
				if i != '.':
					int_counter += 1
				else:
					break
			for i in reversed(a):
				if i != '.':
					decimal_counter += 1
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
					a.pop(-1)
				elif i >= self.max:
					if max:
						if int_counter+max+1 >= len(a):
							break
					a.pop(-1)
					while True:
						try:
							a[negative] += 1
							break
						except TypeError:
							negative -= 1
		def modifier3(self, a, negative=1, l=dict(), n=dict()):
			for j, i in enumerate(reversed(a), start=1):
				if len(l) and len(n):
					try:
						a[(n.values()[-1]-negative)] += l.values()[-1]
						n.clear()
						l.clear()
						for b, c in enumerate(reversed(a), start=1):
							if c is self.limit:
								if b is not len(a):
									self.modifier3(a)
						return
					except TypeError:
						negative += 1
				else:
					if i == ".":
						pass
					elif j is len(a):
						pass
					elif i >= self.limit:
						l[j] = 1
						n[j] = a.index(i)
						a[a.index(i)] = 0
					elif i < self.limit:
						l[j] = 0
if __name__ == '__main__':
	#Just as an example
	Functions = Funcs()
	#random = 999.4555555
	random = ((random.random()*100)**2)*random.random()
	#random = random.random()
	#random = 9.999
	print "Original:%s" % str(random)
	print "Result:%s" % str(Functions.Rounder().round(random, 6))
