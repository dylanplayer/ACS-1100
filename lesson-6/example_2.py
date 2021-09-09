''''
Welcome to Jess + Joi's Dog Kennel 🦴

Every dog is stored at an index

For example: 
index 0 Henry. 🐕‍🦺
index 2 Wuffles. 🐕
'''

# List of dog names

dogs = ["Henry", "Rookie", "Wuffles", "Nugget"]
# Print the first dog's name 
print(dogs[0])

# TODO: Print the second dog
print(dogs[1])

# TODO: Print the third dog
print(dogs[2])

# TODO: Print the fouth dog
print(dogs[3])

# TODO: Use negative indexing to print the last dog
print(dogs[-1])

# TODO: Use negative indexing to print the names of the other dogs
print(dogs[-2])
print(dogs[-1])
print(dogs[-0])


# Joi and Jess want to split up the work at the kennel. Using list 
# slicing, assign Joi two dogs

# listname[start:stop]

joi_dogs = dogs[0:3]
print(joi_dogs)

# TODO: Assign jess the remaining dogs and print Jess' dogs
jess_dogs = dogs[0:3]
print(jess_dogs)

# TODO: A new dog is visiting the kennel. Make up a name and 
# append that dog to the list use: dogs.append("Name")
dogs.append("Flash")

# TODO: Print the dogs list to check the dogs. 
print(dogs)

# num_visit stores the number of times a dog has visited the kennel
num_visit = [2, 3, 5, 2]

# TODO: The new dog just visited for the first appead a 1 to the 
# num_visits list:
num_visit.append(1)

# TODO: Print each dog and the number of times it has visited: 


# TODO: Put the code above into a function that will print the
# dogs and visits

def printDog(index):
    print(f"{dogs[index]} has visited {num_visit[index]} times")

def printDogs():
    print("---------------------------")
    for i in range(len(dogs)):
        printDog(i)
    print("---------------------------")

printDogs()
# TODO: Imagine it's a new week and the dog's have all visited one 
# more time. Increase each dog's visit by 1
# # add one to Henry's visits

for i in range(len(num_visit)):
    num_visit[i] += 1


# add 1 to Rookie
# add 1 to Wuffles
# add 1 to Nugget

# TODO: Print the names and visits of all dogs again! 
printDogs()


# TODO: Count the dogs in the list with code! Use len()
# to print the number of dogs in the list: len(dogs)
print(f"Number of dogs: {len(dogs)}")

# TODO: The kennel is doing well. We need to know how much 
# money we are making sittting dogs. Look up the amount 
# a kennel might charge for sitting a dog per day. I found
# $21 to $40. Define a variable cost_per_day. 
cost_per_day = 32.00

# TODO: Write a function that returns the amount made for 
# sitting a dog. This function should take the index of the
# dog as a parameter and return the num_visit for that dog 
# times the cost_per_day. 
def getRevenue(index):
    return num_visit[index] * cost_per_day

# TODO: Using the function you created in the previous 
# step print a billing message for each dog. Include the 
# dog's name, the number of visits, cost per visit, and 
# the total bill: 
def printBill(index):
    print(f"{dogs[index]} has visited {num_visit[index]} times total cost is ${getRevenue(index)}")

# TODO: Print a billing message for each dog in your list: 
for i in range(len(dogs)):
    printBill(i)
