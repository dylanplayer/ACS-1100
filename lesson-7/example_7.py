#TODO: Using a for loop, print out each color from the list 
# called colors.
colors = ["red", "orange", "green", "blue", "purple"]
       # [    0,        1,        2,     3,        4]
          

for color in colors:  
  print(color)

# For however many colors are in the list called colors
# exectute this for loop
for i in range(len(colors)):
  color = colors[i]
  print(color + " is awesome!") 


#TODO: Create a list of 4 names.
#TODO: Using a for loop, print out each name with " is 
# awesome!" added after each name.
names = ["Mike", "Bob", "Joe", "Dave"]
for name in names:
  print(f"{name} is awesome!")

print("------------")

#TODO: create a list of five integers
#TODO: print the sum of the numbers in the list
numbers = [0,1,2,3,4]
total = 0
for num in numbers:
  total += num
print(f"Total: {total}")
print("------------")

#TODO: After calulcating the sum, calculate the average.
# To calculate average, we take the sum divided by the 
# number of elements in the list called numbers
average = total / len(numbers)
print(f"Average: {average}")

print("------------")

# Redo these with range() 
for i in range(len(names)):
  print(f"{names[i]} is awesome!")
print("------------")

total = 0
for i in range(len(numbers)):
  total += numbers[i]
print(f"Total: {total}")
print("------------")