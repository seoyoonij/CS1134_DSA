
'''
!! CHECK VITAMIN ANSWERS AS WELL !!
'''


# 1. Palindrome checker, two pointers moving inward
def is_palindrome (s):
    for i in range(len(s)//2): # runtime: O(n)
        if s[i] != s[-(i+1)]: # compare pairs from each end
            return False
    return True


# 2. Reverse vowels, two pointers moving inward
def reverse_vowels(input_str):
    vowels = "aeiou"
    front_vowel = float('nan') # mark index of vowel from front: [i], initialized n/a
    front_count = 0
    back_vowel = float('nan') # mark index of vowel from back: [-(i+1)], initialized n/a
    back_count = 0
    while (front_vowel < back_vowel):
        #issue: how to match timing that either one updates get noticed? without skipping an update in count
        for i in range(len(input_str)): # O(n)
            if front_count == back_count: # swap
                input_str[front_vowel], input_str[back_vowel] = input_str[back_vowel], input_str[front_vowel]
            if input_str[i] in vowels:
                front_vowel = i
                front_count += 1
            if input_str[-(i+1)] in vowels:
                back_vowel = -(i+1)
                back_count += 1
    list_str = list(input_str) # list constructor guarantees Theta(n)
    return "".join(list_str)