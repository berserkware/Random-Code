import random

nonvowels = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u"]

print("Length of word:")
low = int(input())
     

def Generate():
    word = ""
    for i in range(low):
        ran = random.randrange(0, 2)
        if ran == 1:
            word += nonvowels[random.randrange(0, len(nonvowels))]
        else:
            word += vowels[random.randrange(0, len(vowels))]

    
    print(word)

    print("Length of word:")
    low = int(input())
    Generate()

    Generate()