# Day 2 - Variables & Functions

# Functions 
print(min(20,30,40,50)) # give min value 
print(max(20,30,40,50)) # give max value
print(min([5,3,6,2,8])) # give min value from list
print(max([5,3,6,2,8])) # give max value from list
print(sum([5,3,6,2,8])) # give sum of values in list

print(len('Hello,  World!')) # it counts the number of characteristics including space !
print(type('Hello, World!')) # it checks the data type 
print(str(10)) # it converts a number into a string 
print(float(10)) # it converts a number into a decimal 
print(int(10)) # it converts to a number 

# Variables
print('Hello, World!') # the text Hello, World! is an argument
print('Hello,',',','World!') # it can take multiple arguments
print(len('Hello, World!')) # it takes only one argument

# Variables in Python
first_name = 'Oliver'
last_name = 'Ratcliff'
country = 'England'
city = 'London'
age = 23
is_married = False
skills = ['Trading','Football','Running','Python']
person_info = {
   'firstname':'Oliver',
   'lastname':'Ratcliff',
   'country':'England',
   'city':'London'
   }

print('First name:',first_name)
print('First name length:',len(first_name))
print('Last name:',last_name)
print('Last name length:',len(last_name))
print('Country:',country)
print('City:',city)
print('Age:',age)
print('Married:',is_married)
print('Skills:',skills)
print('Person Info:',person_info)

# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Oliver', 'Ratcliff', 'England', 23, False
print(first_name, last_name, country, age, is_married)
print('Frst name:',first_name)
print('Last name:',last_name)
print('Country:',country)
print('Age:',age)
print('Married:',is_married)

first_name = input('What is your first name? ')
age = input('How old are you? ')
print(first_name)
print(age)

# Checking Data Types
first_name = 'Oliver' # str
last_name = 'Ratcliff' # str
Country = 'England' # str
city = 'London' # str
age = 23 # int

print(type('Oliver')) # str
print(type(first_name)) # str
print(type(10)) # int
print(type(3.14)) # float
print(type(1 + 1j)) # complex
print(type(True)) # bool
print(type([1, 2, 3, 4])) # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2))) # tuple
print(type(zip([1,2],[3,4]))) # zip

#Casting
#int to float
num_int = 10 
print('num_int:',num_int) # 10 
num_float = float(num_int)
print('num_float:',num_float) # 10.0
#float to int
gravity = 9.81
print(int(gravity)) # 9
#int to str
num_int = 10
print('num_int:',num_int) #10
num_str = str(num_int) # '10'
print(num_str) # '10'
#str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float:', float(num_str)) # 10.6
num_int = int(num_float)
print('num_int',int(num_int)) # 10
#Str to list 
first_name = 'Oliver'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list) # ['O','l','i','v','e','r

# Exercise 1
name_one='Saffron'
name_two='Francis'
name_all= 'Saffron Francis'
country='England'
City='London'
Age=23
DOB_year=2002
is_married=False
has_a_car= True
is_light_on=False
has_a_car, is_light_on = True, False

#Exercise 2
print(type(name_one))
print(type(name_two))
print(type(name_all))
print(type(country))
print(type(City))
print(type(Age))
print(type(DOB_year))

print(len(name_one))
print(len(name_two))
print(len(name_all))
print(len(country))
print(len(City))

num_one=5
num_two=4
variable_total=num_one+num_two
variable_diff=num_two-num_one
variable_product=num_one*num_two
variable_divison=num_one/num_two
variable_remainder=num_two%num_one
variable_exp=num_one**num_two
variable_floor_div=num_one//num_two

print(variable_total)
print(variable_diff)
print(variable_product)
print(variable_divison)
print(variable_remainder)
print(variable_exp)
print(variable_floor_div)

#The radius of a circle is 30 meters
#1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
#2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#3. Take radius as user input and calculate the area.

#1
radius_of_circle=30
pie=3.14
radius_of_circle_squared=radius_of_circle**2
area_of_circle=radius_of_circle_squared*pie
print(area_of_circle)
#2
two_times_pie=2*pie
circum_of_circle=two_times_pie*radius_of_circle
print(circum_of_circle)

#3
radius = float(input('What is the radius?'))
radius_squared=radius**2
area_of_circle=radius_squared*pie
print(area_of_circle)

firstname = input("First name: ")
lastname = input("Last name: ")
country = input("Country: ")
age = input("Age: ")
help('keywords')