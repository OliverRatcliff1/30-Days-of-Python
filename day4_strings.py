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
