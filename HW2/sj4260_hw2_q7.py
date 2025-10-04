# given a list of sequence of 0s followed by a sequence of 1s
# finds index of the first 1
# theta(log(n))

def findChange (lst01):
    left = 0
    right = len(lst01)-1
    curr_one = None

    while left <= right:
        mid = (left + right) //2 # jumping to middle points make it log(n)
        if (lst01[mid] == 0): # need to check right side
            left = mid + 1
        elif (lst01[mid] == 1): # need to check left side
            right = mid -1
            curr_one = mid
    return curr_one


# Usage
lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
print(findChange(lst01))