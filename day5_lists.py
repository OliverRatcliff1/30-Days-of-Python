# Day 5 - Lists

lst=list()
empty_list=list() # this is an empty list 
print(len(empty_list))
lst=[]
empty_list=[]
print(len(empty_list))

fruits=['banana','orange','mango','lemon']
print('Fruits:',fruits)
print('Number of Fruits:',len(fruits))

lst=['Oliver',24, True, {'country:england','city: london'}] 
# lists can have multiple data types 

# Indexing
fruits=['banana','orange','mango','lemon']
first_fruit=fruits[0]
print(first_fruit)
second_fruit=fruits[1]
print(second_fruit)
# Negative indexing
fruits=['banana','orange','mango','lemon']
first_fruit=fruits[-4]
print(first_fruit)
second_fruit=fruits[-3]
print(second_fruit)

# Unpacking lists
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# Slicing from list 
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

# Modifying a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
 # Checking items in a list 
fruits=['banana','orange','mango','lemon']
does_exist='banana' in fruits
print(does_exist)
does_exist='lime' in fruits 
print(does_exist)

# Adding to list (adds to the end)
fruits.append('blueberry')
print(fruits)
fruits.append('blackcurrents')
print(fruits)
# Inserting items into a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') 
print(fruits)          
fruits.insert(3, 'lime') 
print(fruits)
# Removing from list 
fruits.remove('banana')
print(fruits)

fruits.pop() # removes last item 
print(fruits)
fruits.pop(0) # removes the index selected
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits) 
del fruits[1]
print(fruits)
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)
del fruits # this would delte list and result in error msg 

# Clearing List Items 
fruits=['banana','oragne','mango','lemon']
fruits.clear()
print(fruits)

# Copying a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists (+ method / extend() method)
positive_numbers = [1, 2, 3, 4, 5] 
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) 
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

# Counting numbers in a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))       

# Finding an index of an item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) # will show the first occuracne 

# Reversing a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

# Sorting list items 
# sort() reorders the list items in ascending order IF an argument of sort() method 
#reverse is equal to true it will arrnage in decending order 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print('GAP')
# sorted() returns ordered list without modifying the original list 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)

# Exercises 
empty_list=list()
players=['Messi','Ronaldo','Neymar','Mbappe','Noble']
print(len(players))
first_player=players[0]
print(first_player)
middle_player=players[len(players)//2] # how to get middle player
print(middle_player)
last_player=players[-1]
print(last_player)

mixed_data_types=['Ollie',24,181,True,'London']

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))

it_companies[0]='Rocket Labs'
print(it_companies)

it_companies.append('Intuative I')
print(it_companies)

it_companies.insert(2,'Nike')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

it_companies_string='#: '.join(it_companies)
print(it_companies_string)

does_exist='Nike' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

first_three_companies=it_companies[:3]
print(first_three_companies)


