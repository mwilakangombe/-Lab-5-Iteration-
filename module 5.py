
# Mwila Kangombe
# 2/20/2022
# This program performs varuous functions that require inputs and interaction.

# 1. This code prints “Hello World” to the screen 100 times.

for i in range(100):
    print("Hello World")

# 2a. This code prints each of the numbers on a new line.

    nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in nums:
    print(i)

# 2b. This code prints each number and its square on a new line.

for i in nums:
    print(str(i) + " " +str(i**2))

#3. This code asks the user for the number of sides, the length of the side, 
# the color of the line, and the fill color of a regular polygon. The program also draws the 
# polygon and fills it in.

import turtle    

wn = turtle.Screen()    
alex = turtle.Turtle()   
sides = int(input("Enter the number of sides: "))    
angle = 360 / sides    
length = int(input("Enter the length of sides: "))    
line_color = input("Enter the color of the lines: ") 
alex.color(line_color)    
fill_color = input("Enter the fill color for the polygon:" )    
alex.fillcolor(fill_color)    
alex.begin_fill()    
for i in range(sides):    
        alex.forward(length)  
        alex.left(angle)    
alex.end_fill()


# 4. This code iterates integers from 1 to 50. For multiples of three it 
# "prints Divisible by three" instead of the number and for the multiples of five it prints "Divisible by 
# five". For numbers which are multiples of both three and five it prints “Divisible by both”.

for p in range(1,51):
    if(p%3==0 and p%5==0):
        print(str(p)+" is Divisible by both three and five")
    elif(p%5==0):
        print(str(i)+" is Divisible by five")
    elif(p%3==0):
        print(str(i)+" is Divisble by three")
    else:
        print("",end="")

# 5. A program to draw some kind of picture.

import turtle as t

g = 110

for i in range(8):
  t.forward(g)
  t.right(120)
