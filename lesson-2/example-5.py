# Expressions

# Challenges: Write an expression to solve the problems below

# Area of a rectangle with a width of 12 and a length of 23. Area is length * width
rectangle_area = 12 * 23
print("int")
print(type(rectangle_area))

# Seconds in a day? There 60 secs in a min and 60 mins in an hour and 24 hours in a day
day_in_seconds = 60 * 60 * 24
print("int")
print(type(day_in_seconds))

# Area of a circle with a diameter of 10. Are of a circle is 3.14 * radius * radius 
circle_area = 3.14 * 5 * 5
print("float")
print(type(circle_area))

# Convert temperature of 72F to C. Formula is: (f - 32) * 5 / 9
temp_c = (72 - 32) * 5 / 9
print("float")
print(type(temp_c))

# Calculate total cost. Donuts are 0.99 each, specialty donuts are 1.29 each 
# you need 12 regular donuts and 6 specialty donuts

regularCost = .99
specialCost = 1.29
qtyRegular = 12
qtySpecial = 6

total_cost = (regularCost * qtyRegular) + (specialCost * qtySpecial)
print("float")
print(type(total_cost))