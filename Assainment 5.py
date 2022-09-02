'''
Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
Take radius as user input and calculate the area.
'''


radius = 30                                 
area_of_circle = 3.14 * radius ** 2         
print('Area of a circle:', area_of_circle)


radius = 30                                 
circumference_of_circle = 3.14 * radius * 2         
print('circumference of circle:', circumference_of_circle)


import math
r = float(input("enter radius of your choice:"))
print(f"The area of circle with radius {r} is {round(math.pi * r * r,2)}")
