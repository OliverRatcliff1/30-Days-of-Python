# Day 6 - Tuples

# A tuple is a collection of differnet data types which are ordered and unchangable

empty_tuple=()
empty_tuple=tuple()

# tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

# Accessing tuple items - uses positive indexing
first_item=fruits[0]
second_item=fruits[1]
last_item=fruits[-1]
print(first_item,second_item,last_item)

# Slicing Tuples - pick where to start and end, the retunr will be a new tuple
all_fruits=fruits[0:4]
all_fruits=fruits[0:]
orange_mango=fruits[1:3]
orange_and_after=fruits[1:]
allfruits=fruits[-4]
middle_two=fruits[-3:-1]

#Tuples cant be editied, so what we do is change it to a list
fruits=list(fruits)
print(fruits)
fruits=tuple(fruits)
print(fruits)

# Checking items in a tuple 
print('orange' in fruits)
print('apple' in fruits)

vegetables=('tomato','potato','cabbage','onion','carrot')
fruits_and_veg=fruits+vegetables
print(fruits_and_veg)

del fruits
del vegetables

# Exercises 
tuple=()
brothers=('Oscar','Tom')
sisters=('Niamh','Rosie')
siblings=brothers+sisters 
print(siblings)
print(len(siblings))

parents=('Adrian','Sarah','Michelle','Chris')
family_members=parents+siblings
print(family_members)

print(family_members[0:4])
print(family_members[4:])

fruits=('bananna','kiwi','pear')
vegetables=('cucumber','pepper','courgette')
animal_products=('milk','steak','butter')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
food_stuff_list=list(food_stuff_tp)
middle_item_number=len(food_stuff_list)//2
print(food_stuff_list[middle_item_number])
print(food_stuff_list[4])
print(food_stuff_list[0:3])
print(food_stuff_list[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)