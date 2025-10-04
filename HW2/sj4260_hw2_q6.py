# sorted list
# finding two elements that add up to target
# theta(n)
# approach: two pointers

def two_sum (srt_lst, target):
    left = 0
    right = len(srt_lst)-1

    while left < right:
        if (srt_lst[left] + srt_lst[right]) == target: # match found
            return (left, right)
        elif (srt_lst[left] + srt_lst[right]) < target: # smaller than target, but right can't get any bigger
            left += 1
        elif (srt_lst[left] + srt_lst[right]) > target: # bigger than target
            right -= 1
    return None


# Usage
srt_lst = [-2,7,11,15,20,21]
target = 22
print(two_sum(srt_lst, target))