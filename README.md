# ValueRounder
Just a value rounder for python made for myself. Made for fun.

Only supports positive numbers, for now.

Rounds decimal digits >= 5 to the next possible value. Digits < 5 are deleted.

E.g

<b>0.9 -> 1</b> | <b>0.5 -> 1</b> | <b>0.4 -> 0</b> | <b>0.1 -> 0</b> | <b>0.444445 -> 1</b>

THIS DOES NOT WORK LIKE `math.ceil` (<b><i>0.1 -> 1</b></i>) <b><i>OR</i></b> built-in `round` (<b><i>0.444445 -> 0</b></i>)
