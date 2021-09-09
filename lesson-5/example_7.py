# The random lib has functions for generating random values
import random 

# Use random to generate random numbers like this: 
print(random.randint(1, 6)) # print random number from 1 to 6

# TODO: Print a random number between 0 and 1
print(random.randint(0, 1))

# TODO: Generate a random number between 0 and 1 
# If the number is 0 print "Heads" if not print "Tails"
num = random.randint(0 ,1)
if num == 0:
	print("Heads")
else:
	print("Tails")

# I hear Dungeons and Dragons is popular. It's an 
# RPG game. Characters are defined by characteristics 
# like strength, intelligence and desxterity.
# These stats have a value of 3 to 18. Thats a random 
# number from 1 to 6 three times 

# TODO: Write a function that generates three random
# numbers from 1 to 6 adds them together and returns 
# the results 

def roll3d6(): 
	a = random.randint(1, 6)
	b = random.randint(1, 6)
	c = random.randint(1, 6)
	return a + b + c

# TODO: Characters have attributes of strength
# intelligence and dexterity each has a value of 3 - 18
# Define three variables str, int, and dex below
# Use your function to generate the values. 

str = roll3d6()
int = roll3d6()
dex = roll3d6()

# TODO: Every character starts with amount of gold pieces
# gp is equal to 3 - 18 * 10. Write a function that returns 
# start gp. Use the function above to generate a number from 
# 3 to 18 multiply the value returned by 10 and return it. 
# It's imortant you use the other function here (DRY!)

def startingGP(): 
	return roll3d6() * 10

# TODO: Define a variable for gp and assign it a value: 

gp = startingGP()

# TODO: If your strength is highest you should be a 
# fighter, if you intelligence is highest you should 
# be a wizard, if your dexterity is highest you should 
# play a rogue. 
# Print a characters best profesion below by looking 
# at the numbers you generated. 

if str > int and str > dex:
	print("Character is a fighter")
elif int > str and int > dex:
	print("Character is a wizard")
elif dex > str and dex > int:
	print("Character is a rouge")
else:
	print("Character is a not classified")