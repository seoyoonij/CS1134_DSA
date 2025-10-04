# returns generator
# Theta(sqrt(num)): iterate up to sqrt(num)
# for complementary factors a and b, cannot have both a,b bigger than sqrt(num) bc then a*b > num (contradiction).
# at least one of all pairs would be before sqrt(num).

import math

def factors(num):
    comp_fact = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            yield i
            if i != num // i: # avoid storing factors twice for perfect squares
                comp_fact.append(num//i) # store the complementary factor
    for comp in reversed(comp_fact):
        yield comp
   

# Test
for curr_factor in factors(100):
    print (curr_factor)