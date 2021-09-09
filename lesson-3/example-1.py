def greet_by_name(name):
	greeting = "Hello, " + name + "!"
	return greeting

a = greet_by_name("Amy")
b = greet_by_name("Bob")
c = greet_by_name("Cat")
d = greet_by_name("Dan")

# Print the variables above to the console
print(a, b, c, d)

# What type is returned? How can you check the type? Do it that here:
print(type(a))

def add_ten(number): 
	new_number = number + 10
	return new_number

# How can you save the values returned by the add_ten function? 
number1 = add_ten(60)
number2 = add_ten(30)
# Print the values returned by the two calls to add_ten above:
print(number1, number2)
# Use add_ten to add 10 to the total of the first two calls to add_ten. 
# The answer should be 120. Print the result below. 
number3 = add_ten(add_ten(100))

print(number3)