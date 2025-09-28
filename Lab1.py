# 1. Scrabble
'''
Logic
# build a letter bank
# store number of occurrence & compare
# that would work like dictionary of char:occurrence
# array of len 26: a-z
# use ASCII values (ord("a")=97, ...)
'''
def can_construct (word, letters):
    letter_bank = [0] * 26
    a = ord("a") # offest: ascii value of a
    for char in letters:
        letter_bank[ord("char")-a] += 1 # record provided number
    for char in word:
        if letter_bank[ord("char"-a)] < 1: # not enough
            return False
        letter_bank[ord("char"-a)] -= 1 # "use" provided char
    return True

# 2. Complex numbers
class Complex:
    def __init__(self, a, b):
        self.real = a
        self.im = b
    def __add__ (self, other):
        return Complex(self.real + other.real, self.im + other.im)
    def __sub__ (self, other):
        return Complex(self.real - other.real, self.im - other.im)
    def __mul__ (self, other):
        return Complex((self.real * other.real - self.im * other .im), (self.real * other.im + self.im * other.real))
    def __repr__ (self, other):
        sign = " + " if self.im >= 0 else sign = " - "
        return f"{self.real} {sign} {abs(self.im)}i"
    def __iadd__ (self, other):
        self += other
        return self
    
# 3. Permutation
import random

# a.
def create_permutation (n):
    perm = [-1] * n # -1 means empty spot
    while (counter >= 0): # use while instead of for to keep looping until all numbers are placed
        index = random.randit(0,n-1)
        if (perm [index] == -1):
            perm[index] = counter
            counter -= 1
        
    return perm

# b.
def scramble_word(word):
    scr = create_permutation(len(word)) # list of scrambled order
    for i in range(len(word)):
        scr[i] = word[scr[i]]
    return " ".join(scr) # to return string

# c. 
word_bank = ["Pokemon", "Digimon"]

def choose_word(words):
    return words[random.randit(0,len(word_bank)-1)]

def guessing_game(word):
    print("Unscramble the word" + scramble_word(word))
    tries = 3
    correct_guess = False
    
    while (tries and not correct_guess):
        guess = input("Try #" + str(4-tries) + ":")
        if word == guess:
            correct_guess = True
        else:
                print("Wrong!")
                tries -= 1
    
    if tries:
        print("You got it!")
    else:
        print("Out of tries!")

pick = choose_word(word_bank)
guessing_game(pick)
