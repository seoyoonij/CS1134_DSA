# odd numbers first, even numbers second
# internal order doesn't matter
# do not create new local list
# runtime = theta(n)
# approach: swap places using two pointers

def split_parity(lst):
    left = 0
    right = len(lst)-1

    while left < right: # theta(n)
        if lst[left] % 2 == 1: # move on if odd, stop when even.
            left += 1
        elif lst[right] % 2 == 0: # move on if even, stop when odd. elif makes sure only one pointer moves within one iteration
            right -= 1
        else: # swap
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    return lst
    
# Usage
lst = [2,4,6,1,8,10]
print(split_parity(lst))