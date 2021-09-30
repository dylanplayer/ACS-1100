# Examine the code below. 
# What is it doing? 
# Could you make this code better? 

def printevens(num_list):
	"""
	Prints the even indexes of a list of numbers

		Parameters:
			a (list): list of numbers
		
		Returns:
			None
	"""
	index = 0
	while(index < len(num_list)):
		if index % 2 == 0:
			print(num_list[index], end="")
		index += 1

