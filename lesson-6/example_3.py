'''
Deep down inside you're a cat person! 🐈
Cat people collect cats and obsess over 
cat details! 
'''

cats = ["Bill", "Bob", "Joe"]

# TODO: Print the cat list! 
print(cats)

# TODO: You just got your first cat: "Bert"
# Add it to the cat_names list with append!
cats.append("Bert")
print(cats)

# You just got two more cats! Someone 
# put them in an array and left them at your
# house: ["Clawdia", "Eunice"]
# TODO: Extend at_names with the new cats in the 
# list above. Use cat_names.extend()
cats.extend(["Clawdia", "Eunice"])
print(cats)

# TODO: You found a cat walking home yesterday
# It's name is "Alfie". You always keep your 
# cats organized in alphabetical, you're
# obsessed remember? Use cat_names.prepend()
cats.insert(0, "Alfie")
print(cats)

# TODO: You just found another cat named "Duff"
# Put Duff in the cat_list in alphabetical order 
# use cat_list.insert()
cats.insert(2, "Duff")
print(cats)

# TODO: These Cats are ruining your furniture
# Give one away. Use cat_list.remove() to 
# remove "Eunice"
cats.remove("Eunice")
print(cats)

# TODO: I think "Alfie" has to go he keeps 
# horking up fur balls! he should be first in 
# the list you can use: cat_list.pop()
cats.pop()
print(cats)

# TODO: Actually you've had a revelation and 
# decided you're a dog person after all. Clear
# the cat_list with cat_list.clear()
cats.clear()
print(cats)
