# This while loop prints count until 100, but it breaks when 
# the counter reaches 25 

counter = 0

while counter < 100:
  print(f"Counter: {counter}")
  counter += 1

  # If counter is 25, loop breaks
  if counter == 25:
    break


# Write a for loop that counts backwards from 50 to 
# 0. 

for num in range(50, 0, -1):
  print(num)