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
