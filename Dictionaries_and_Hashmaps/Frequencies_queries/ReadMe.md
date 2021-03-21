Problem statement and test cases can be found [here](https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps).


</p>The first version of the code was implemented using "brute force". The logic seems to be correct, however the code is  too slow, with test cases 10 and 11 failing due to timeout.</p>

<p align="justify">The second version of the code improved in terms of speed. The substitution of the "if" statements with "try - except" commands allowed it to pass test case 10, but not 11.</p>

<p align="justify">In the Discussions section, there was a very interesting idea: to use a "reverse look up". The notion is that if you also use a dictionary to store which frequencies correspond to which numbers, then this will have at worst as many keys as the original dictionary and, so, the look up will be at worst as slow, but a speed up is expected. This was implemented in the code, using the "reverseDict", storing, for each frequency, a list of numbers that appear that number of times. This final version of the code finally passed all the tests.</p>
