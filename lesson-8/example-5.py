'''
Function Practice: 

modify the code you just wrote by 
creating a function called read_candy() 
that takes in the file name as a parameter 
and returns the lines of the file as a list
'''

# STEP 1: Store the name of the file
# TODO: define a variable filename and store the name 
# of the file candy.txt. Ask yourself what the path 
# should be? 
filename = "candy.txt"

def read_candy(filename):
  # Open
  infile = open(filename, 'r')

  # Read
  lines = infile.readlines()

  #Close
  infile.close()

  # Return
  return lines

#TODO: print out all the lines of the candy file
candy_lines = read_candy(filename)
print(candy_lines)

# TODO: Function Practice: modify the code you just wrote 
# by creating a function called read_candy() that takes in 
# the file name as a parameter and returns the lines of the 
# file as a list


# TODO: Read the file flavors.txt Print all of it's lines
flavors = read_candy("choc.txt")
for flavor in flavors:
  print(flavor, end='')

