#Tuples are immutable lists

my_tuple = (1,2,3,4,5)

b = my_tuple[1]
a = my_tuple[2]
print(b)
print(a)

#OR

x,y, *other = (1,2,3,4,5)
print(other)

pokemon = ['pikachu',
'squirtle',
'charmander',
'Jynx',
'Mr.Mime'
]

pogemon = tuple(pokemon)
print(type(pogemon))