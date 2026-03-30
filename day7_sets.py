# Day 7 - Sets
st=set()
fruits={'bannana','orange','mango','lemon'}
print(len(fruits))

# Accessing Items in a Set 
    # We use loops to access items in a set

# Checking an item 
fruits={'bannana','orange','mango','lemon'}
print("Does fruits contain mango?",'mango' in fruits)

# Adding to a set 
fruits={'bannana','orange','mango','lemon'}
fruits.add('pear')

#Add multiple items using update
fruits={'bannana','orange','mango','lemon'}
new_fruits=('strawberry','kiwi','melon')
fruits.update(new_fruits)
print(fruits)

# Removing from a set 
fruits.remove('orange')
print(fruits)

# Removing a random item from the list and returns removed item
fruitsnew={'bannana','orange','mango','lemon'}
fruitsnew.pop()
print(fruitsnew)
removed_item=fruitsnew.pop()
print(removed_item)

# Clearing / Deleting Items in a Set 
fruits.clear()
del fruits

# Converting List to Set ( list to set will remove duplicates)
teamlist=['manu','westham','spurs','arsenal','westham']
teamset=set(teamlist)
print(teamset)

# Joining Sets 
food={'crisps','chocolate','pizza'}
drink={'coke','beer','lemonade'}
meal=food.union(drink)
print(meal)
# or 
food.update(drink)
print(food)

# Finding Intersection Items (items in both)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))

# Subset and Superset - a set can be a subset(contains only that) or susperset of other sets (contains everything)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# Checking difference between sets (returns the difference using - symbol)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}

# Finding symetric  difference between 2 sets (A\B = stuff in a but not B) ∪ (B\A = stuff in B but not A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# Joining Sets - if 2 sets do not have a common item/s we call them disjoint sets
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


# Exercises
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update({'Rocket Labs','ASTS','BlackSky'})
print(it_companies)
it_companies.remove('Google')
# remove removes item from set ONLY if its there ERROR if not and discard does same but no ERROR if not there

A.update(B)
A.intersection(B)
print(A.issubset(B))
print(A.isdisjoint(B))
A.union(B)
B.union(A)
A.symmetric_difference(B)
del A,B

print(len(age)) # List is bigger
ageset=set(age) 
print(len(ageset))
# A string is a collection of characters (text)
# A list is an ordered, changeable collection of items (can have duplicates)
# A tuple is an ordered, unchangeable collection of items
# A set is an unordered collection of unique items (no duplicates)

quote=('I am a teacher and I love to inspire and teach people')

len(set(quote.split()))

