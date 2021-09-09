# Use if, else, an elif to make decisions in your programs
# Here's an example. 

player_1_score = 1000
player_2_score = 1050

if player_1_score > player_1_score: 
  print("Player 1 is the winner!")
else:
  print("Player 2 is the winner!")

# Predict the winner and run the code. 
print("player 2 is the winner")
# TODO: Who wins if the scores are equal? 
player_1_score = player_2_score
print("player 2 wins if the scores are equal")

if player_1_score == player_2_score:
  print("Player 1 and Player 2 are tied!")
elif player_1_score > player_2_score:
  print("Player 1 is the winner!")
else:
  print("Player 2 is the winner!")

# Here we check if the scores are equal first
# Then check if one os greater than the other. 

# I like cookies but I'll take a scone. Imagine we have 
cookies = 2
scones = 4

# If there are cookies I order one otherwise I order 
# a scone. Write an if else statement. It should print: 
# "I'll take a cookie!" if cookies is greater than 0
# Otherwise it prints: "Give me a scone" 

if cookies > 0:
  print("I'll take a cookie!")
else:
  print("Give me a scone")

# TODO: We need some code to help out the bakery ordering 
# bot. The bot prefers cake, but if cake is not available
# it will order a cookie. If no cookies are left it orders
# a scone. Use if and elif to make the decision:

cookies = 4
rasinCookies = 4
cake = 4
cookie_type = "raisin cookie"

if cake > 0:
  print("I'll take some cake!")
elif cookies > 0:
  print("I'll take a cookie!")
else:
  print("Give me a scone")


# Use an if else statement to check if there are any 
# cookies left: cookies > 0
# If there are no cookies left print: "Darn I wanted a cookie!"
# if the cookie is NOT a raisin cookie print: 
# "I want a cookie!"
# Otherwise print: "Meh!"

if cookies > 0:
  print("I'll take a cookie!")
else:
  print("Darn I wanted a cookie!")

if cookies != rasinCookies:
  print("meh")
else:
  print("I want a cookie!")

