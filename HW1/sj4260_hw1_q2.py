'''
# Constraints
    # Given a list of N numbers, circular shift left by k
    # Do not create new list
'''
# 2a. Circular shift left
def shift(lst,k):
   for i in range (k):
        elem = lst.pop(0) # remove first element
        lst.append(elem) # place in the back

# Usage
lst = [1,2,3,4,5,6]
shift (lst, 2)
print(lst)

    
# 2b. Circular shift with direction
def shift(lst,k, right = False):
    for i in range (k):
        elem = lst.pop(-1 if right else 0)
        if right: # by default, left-shift
            lst.insert(0, elem)
        else: 
            lst.append(elem)
    
# Usage
lst = [1,2,3,4,5,6]
shift (lst, 2, True) # right-shift
print(lst)

