Problem statement and test cases can be found at:
https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

The first version of the code was implemented using "brute force". The logic seems to be correct, however the code is  too slow, with test cases 10 and 11 failing due to timeout.

The second version of the code improved in terms of speed. The substitution of the "if" statements with "try - except" commands allowed it to pass test case 10, but not 11.
The discussions in the forum indicated that there could be a problem in the "boilerplate code" (input-output), but they also indicated something interesting:
For the freqCheck, instead of having just a dictionary where numbers correspond to frequencies, we can have a "reverse map", where frequenicies map to integers.
This last "reverseDict" will be, in the worst case scenario, as big as the original freqDict and so a speedup is expected in the lookup.
