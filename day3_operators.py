# Day 3 - Operators

# Integers
print('Addition: ', 1+2)
print('Subtraction: ', 2-1)
print('Division: ', 4/2)
print('Multiplication: ',2*3) # division prints a floating number
print('Division without remainder: ',7//2) # gives without floating number
print('Modulus: ', 3%2) # Gives the remainder (whats left over)
print('Exponential: ',2**3) # it means 2*2*2 (power of)

# Floats
print('Floating number point , PI', 3.14)
print('Floating point number, gravity', 9.81)

# Complex Numbers 
print('Complex number: ', 1+1j)
print('Multiplying complex number: ',(1+1j)*(1-1j))

#Declaring the variable at the top first 
a=3
b=2
total=a+b
diff=a-b
product=a*b
division=a/b
remainder=a%b
floor_division=a//b
exponential=a**b

print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Calculating Things
radius = 10 # radius of a circle
area_of_circle = 3.14 * radius ** 2  # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N') # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3


# Comparison Operators
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1) # True - because the data values are the same
print('1 is not 2', 1 is not 2) # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - cause coding for all has the word coding
print('a in an:', 'a' in 'an')  # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical Operators
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# Exercise

age=23
height=5.11
complex_number=1+1j
base_of_triangle=float(input('Enter base of triangle: '))
height_of_triangle=float(input('Enter height of triangle: '))
area_of_triangle=0.5*base_of_triangle*height_of_triangle
print('The area of the triangle is:', area_of_triangle)

side_a=float(input('Enter side A: '))
side_b=float(input('Enter side B: '))
side_c=float(input('Enter side C: '))
perimeter=side_a+side_b+side_c
print('The perimeter of the triangle is',perimeter)
length=float(input('Enter length of rectangle: '))
width=float(input('Enter width of rectangle: '))
area_of_rectangle=length*width
perimeter_of_rectangle=(2*(length+width))
print('The area of the rectangle is', area_of_rectangle)
print('The perimeter of the rectangle is', perimeter_of_rectangle)

print(len('python') != len('dragon'))
print('on' in 'python'and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print(type(str(float(len('python')))))

#checking if a number is even or not (even numbers are divisible by 2 and remainder is 0)
print(2%2==0, 4%2==0, 6%2==0, 9%2==0)
number=int(input('enter a number'))
if number%2==0:
    print("the number is even")
else:
    print('the number is odd')

print(7//3==int(2.7))

print(type('10')==type(10))

print(int(float('9.8'))==10)

#Write a script that prompts the user to enter hours and rate per hour.
hours=float(input('Enter hours:'))
rate_per_hour=(float(input('Enter rate per hour:')))
wage=hours*rate_per_hour
print('Your wage for hours worked is:',wage)

#Calculate the number of seconds a person can live.
years_lived=int(input('Enter number of years lived:'))
seconds_in_year=365*24*60*60
seconds_lived=years_lived*seconds_in_year
print('you have lived for', seconds_lived,'seconds!')

print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)