# Day 4 - Strings

# Multiline strings are created using triple single ''' or """"
multiline_string = '''I am learning Python.
This is day four.
Strings are cool.'''
print(multiline_string)

# We can connect strings together this is called 'Concantenation' 
first_name = 'Ollie'
last_name = 'Ratcliff'
full_name = first_name + ' ' + last_name
print(full_name)


# Escape Sequences
#\n: new line
#Tab means(8 spaces)
#Back slash
#Single quote (')
#Double quote (")

print('I hope everyone is enjoying the Python.\nAre you?')
print('Days\tTopics\tExercises')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('this is a backslash symbol (\\)')
print('in every programing language it starts with \"Hello, World!\"')

# String Formatting

# OLD STYLE
# % is used to format a set of variables enclosed in a tuple, together with 
# a format string, which contains normal text together with argument specifiers (below)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision
radius=10
pi=3.14
area=pi*radius**2
formatted_string='The area of the Circle with a radius %d is %.2f.'%(radius,area)
print(formatted_string)
# 2 refers to the 2 significant figures after the point

# New Style 
first_name='Ollie'
last_name='Ratcliff'
language='Python'
formatted_string='I am {} {}. I teach {}'.format(first_name,last_name,language)
print(formatted_string)

a=4
b=3
print('{}+{}={}'.format(a,b,a+b))
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings and Numbers 
radius=10
pi=3.14
area=pi*radius**2
formatted_string='The area of a circle with a radius of {} is {:.2f}'.format(radius, area)
print(formatted_string)

# String Interpolation / f-strings 
c=4
d=3
print(f'{a} + {b} = {a+b}')
print(f'{a} / {b} = {a / b:.2f}')

# Python strings as sequences of characters (numbers start from 0)
language='Python'
first_letter=language[0]
print(first_letter)
second_letter=language[1]
print(second_letter)
last_index=len(language)-1
last_letter=language[last_index]
print(last_letter)

# Slicing Strings 
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[:3]
print(last_three)   # hon
# :3 = everything beofre index 3 / 3: everything after index 3 

# Reversing String 
greeting='Hello, World!'
print(greeting[::-1])

# Skipping Characters ( the 6 means stop before index 6 / the 2 takes every 2nd character
language = 'Python'
pto = language[0:6:2] #
print(pto) # pto

# String Methods 

# Capitalize - first letter a capital
challenge='thirty days of python'
print(challenge.capitalize())

# Count() - returns occurances 
hallenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2

# Endswith() - checks if string ends with a specific ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# Expandtabs() - replaces tab character spaces
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(15)) # 'thirty    days      of        python'