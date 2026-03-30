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

# Find() - returns the index of the first occurance of a substring (-1 if not found)
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# rfind() - returns the index of the last occurance of a substring(-1 if not found)
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# index() - Returns the lowest index of a substring
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7

# rindex() - returns the highest index of a substring (reverse index)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex('on', 8)) # 19, the 8 means it ignores everything before it 
text = "abc da xyz da"
print(text.index("da"))   # 4
print(text.rindex("da"))  # 11

# Isalnum() - Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True
challenge = '30DaysPython'
print(challenge.isalnum()) # True
challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character
challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isaplha() - checks if stroings elements are alphabet characters
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal() - Checks if all characters in a string are decimal
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed 

# isdigit() - Checks if all characters in a string are numbers
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

# isnumeric() - Checks if all characters in a string are numbers or number related
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

# isidentifier() - Checks for a valid identifier - it checks if a string is a valid varible name 
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower() - Checks if all alphabet characters in the string are lowercase 
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper() - Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join() - Returns a concatenated string 
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

# strip - Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# replace - Replaces substring with a given string 
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split() - Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title() - Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase - Converts upper to lower and lower to upper case 
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith() - Checks if String Starts with the Specific String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False


# Exercises 

name='Thirty', 'Days', 'Of', 'Python.'
result2=' '.join(name)
print(result2)
name='Coding', 'For', 'All.'
result3=' '.join(name)
print(result3)

company="Coding For All"
print(company)
print(len(company))
print(company.lower())
print(company.upper())
print(company.capitalize())
print(company.title())
print(company.swapcase)

split=company[7:]
print(split)

print(company.find('Coding'))
print('Coding' in 'Coding for all')
sub_string_two = 'Coding'
print(company.index(sub_string_two))
print(company.replace('Coding','Python'))
company_two='Python For Everyone'
print(company_two.replace('Everyone','All'))
print(company.split(' '))
companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))
print(company[0])
print(company[13])
print(company[10])

print(company_two.split(' '))
print(company.split(' '))
first_letter_everyone=company_two[0]
second_letter_everyone=company_two[7]
third_letter_everyone=company_two[11]
first_letter_coding=company[0]
second_letter_coding=company[7]
third_letter_coding=company[11]

company_abr=first_letter_everyone+second_letter_everyone+third_letter_everyone
company_two_abr=first_letter_coding+second_letter_coding+third_letter_coding
print(company_abr)
print(company_two_abr)

sub_string='F'
print(company.index(sub_string))
sub_string_three='l'
print(company.rindex(sub_string_three))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))

start=sentence.index('because')
end=start+len('because because because')
print(sentence[start:end])

print(company.startswith('Coding'))
print(company.endswith('Coding'))
newcompany=' Coding For All '
print(newcompany)
print(newcompany.strip())

list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result='# '.join(list)
print(result)

multistring='''I am enjoying this challenge.
I just wonder what is next.'''
print(multistring)

print('Name\tAge\tCountry\tCity')
print('Oliver\t24\tEngland\tLondon')


radius=10
area=3.14*radius**2
print("The area of the circle with a radius {} is {:.0f} meters square".format(radius,area))

a=8
b=6
print('{}+{}={}'.format(a,b,a+b))
print('{}-{}={}'.format(a,b,a-b))
print('{}*{}={}'.format(a,b,a*b))
print('{}/{}={}'.format(a,b,a/b))
print('{}%{}={}'.format(a,b,a%b))
print('{}//{}={}'.format(a,b,a//b))
print('{}**{}={}'.format(a,b,a**b))