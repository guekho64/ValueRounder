# ValueRounder
Just a value rounder for python &amp; nothing else. Made for fun.

Only supports positive numbers, for now.

Rounds decimal digits >= 5 to the next possible value. Digits less than 5 are deleted.

E.g

0.9 -> 1
0.5 -> 1
0.4 -> 0
0.1 -> 0

THIS DOES NOT WORK LIKE `math.ceil`! (0.1 -> 1)
