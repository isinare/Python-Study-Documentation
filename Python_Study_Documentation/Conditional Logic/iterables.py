#an iterable is a collection of items(lists,sets,dictionaries,tuples)
#iterate -> one by one check each item in the collection

user = {
    'name':'Zlade',
    'age' : 14,
    'occupation' : 'student',
    'minor' : False
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key,value in user.items():
    print(key,value)