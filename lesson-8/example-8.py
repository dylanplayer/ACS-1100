'''
Before Sunday Night Football, you want to go shopping for your favorite snacks! 

Let's create a shopping list with your favorite snacks to eat!
'''

#TODO: create a list of strings containing your favorite snacks
favorite_snacks = ["goldfish", "poptarts", "fruit"]

#TODO: open a new file called "shopping_list.txt" for write
shopping_list = open("shopping_list.txt", "w")

# #TODO: finish this loop to write your favorite snacks to the shopping_list.txt file

for snack in favorite_snacks:
    shopping_list.write(snack + "\n")

# outfile.close()
shopping_list.close()

# Notice how the above code overwrites the data with each loop. 
# Let's modify our code to write multiple lines of code to the file!


'''
TODO: 

1. Creating a function called write_shopping_list() that has one parameter called snacks. This function takes a list of strings.

2. You function should write to the file using .writelines() 

'''


