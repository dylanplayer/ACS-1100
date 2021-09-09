# Here is the double function

def double(number):
	return number * 2

first_number = double(100)
second_number = double(25)

print(first_number) # 200
print(second_number) # 50

#TODO: Cuber. This function should multiply three numbers and return the answer

def cuber(a, b, c): 
	return a * b * c

cuber(3, 3, 3) # Should return 27

#TODO: Write a function to generate product

def product(a, b):
	return a * b

# double 3 and cube 2 and return the product
print(product(double(3), cuber(2,2,2)))

