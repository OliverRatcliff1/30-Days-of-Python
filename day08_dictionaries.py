# Day 8 - Dictionaries

empty_dict={}
dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':25,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

# We access information from dictionaries by referinng to its key name
print(person['first_name'])
print(person['address']['street'])

# We use get to check is there is that key availible - if there is that key it shows
# if no key then it'll say none
print(person.get('first_name'))
print(person.get('Football_team'))

# Adding to dictionary
person['job_title']='Instructor'
person['skills'].append('HTML')
print(person)

# Modifying a dictionary
person['age']='21'
person['first_name']='Ollie'
print(person)

# Checking keys in dictionary
print('last_name'in person)

# Removing key and value pairs from a dictionary 
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name
person.pop('first_name')
person.popitem()  #removes address as thats the last key entered 
del person['is_married']
print(person)

# Changing dictioanry to a list is done by using items()
print(dct.items())

# clear() removes items in a dictioary / del X deletes it
print(dct.clear())   #will show none

# Copying a dictionary is done by using copy()
dct_copy=dct.copy()

# Getting keys and values as a list 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)   

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values) 

# Exercises 
dog={}

dog['name']='Albie'
dog['colour']='Beige'
dog['breed']='Bullmastif'
dog['legs']=4
dog['age']=6
print(dog)

student={'first_name':'Ollie',
          'last_name':'Ratcliff',
          'gender':'Male',
          'age':24,
          'marital_status':'No',
          'skills':['Python','Fitness'],
          'country':'UK',
          'city':'Shenfield',
          'address':'53 Ardeligh Court'}
print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('Football')
student['skills'].append('Running')
print(student)

keys = student.keys()
print(keys)   

values = student.values()
print(values) 
