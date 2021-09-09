
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

print("WELCOME TO MADLIBS")

word1 = input("Enter an adjective: ")
word2 = input("Enter a noun: ")
word3 = input("Enter a verb in the past tense: ")
word4 = input("Enter an adverb: ")
word5 = input("Enter an adjective: ")
word6 = input("Enter a noun: ")
word7 = input("Enter a noun: ")

line1 = f"Today I went to the zoo. I saw a(n) {word1}"
line2 = f"{word2} jumping up and down in its tree."
line3 = f"He {word3} {word4} through the large tunnel"
line4 = f"that led to its {word5} {word6}. I got some"
line5 = f"peanuts and passed them through the cage"
line6 = f"to a gigantic gray {word7} towering above"
line7 = f"my head. Feeding that animal made me hungry."


print(line1, line2, line3, line4, line5, line6, line7)