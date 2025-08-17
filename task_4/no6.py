
# Task 6: Word Analyzer
word = input("input a word: ") # Ask the user to input a word
print(len(word)) # Print the length of the word

upper_case = word.isupper() #Check if it is all uppercase, all lowercase, or title case
lower_case = word.islower()
title = word.istitle()

reversed_word = word[::-1] # Reverse the word using slicing
print(reversed_word)
