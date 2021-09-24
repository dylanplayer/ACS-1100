'''
Print numbers 0 to 10, but skip 3
continue'''

number = 0
while number <= 10:

  if number == 3:
    number += 1
    
  
  print(number)
  number += 1

print("------------------")

# Print the write a while loop that counts to 10 and prints 
# each number unless the number is divisible by 3 which case 
# you should print "Fizz"

for num in range(1, 11):
  if(num % 3 == 0):
    print("Fizz")
  else:
    print(num)

