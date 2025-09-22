def fibs(n):
    prev_sum, curr_sum = 1, 1 # initial conditions
    for i in range(n):
        yield prev_sum
        prev_sum, curr_sum = curr_sum, prev_sum+curr_sum # update in one-line: or else curr_sum uses new prev_sum value

# Test 
for curr in fibs(8):
    print(curr, end=" ")