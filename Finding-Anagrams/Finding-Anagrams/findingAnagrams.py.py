# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word1 = input("enter the first word: ")
    word2 = input("enter the second word: ")

    if (sorted(word1) == sorted(word2)):
        print(True)
    else:
        print(False)

