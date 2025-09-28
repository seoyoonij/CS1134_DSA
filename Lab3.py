# 1a. Reverse list order
def reverse_list(lst):
    for i in range(len(lst)//2): # integer division
        a = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-i] = a


# 1b. Reverse list order
def reverse_list(lst, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = 0

    i = low
    for i in range((high-low+1)//2):
        a = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-i] = a


# 2. Generator
def powers_of_two(n): # take in number n and return first n powers of 2
    for i in range(1, n+1):
        yield 2 ** i    

for val in powers_of_two(3):
    print(val, end= ", ")


# 3. Two pointers
'''
Conditions:
    # move all zeros to the end
    # preserve original order of non-zeros
    # swap in-place w/o extra list
    # O(n)
Logic:
    # ignore zeros, bring all non-zeros to front
    # once done with non-zeros, fill rest with zeros
    # 2 pointers: reader scans & writer pauses where non-zero is moved to
    # when list is all read, fill anything after writer as 0
'''
def move_zeros(nums):
    write = 0 # where the next non-zero should go

    for read in range(len(nums)):
        # enters at the next non-zero after write
        if (nums[read] != 0): 
            nums[write] = nums[read]
            write += 1 # if read=0, write cursor pauses there
    for i in range(write, len(nums)):
        nums[i] = 0


# 4. 
def shift (lst, k):
    reverse_list(lst) # reverse whole list
    reverse_list(lst, 0, k+1) # reverse from 0 to k
    reverse_list(lst,k,len(lst)-1) # reverse from k to len(lst)-1








