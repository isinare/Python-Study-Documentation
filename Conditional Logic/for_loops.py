#for Loops

for item in {1,2,3,4,5,6,7,8}:
    print(item + 1)
    print(item - 1)
    print(item*2)
#for loops can seperately print lists, sets dictionaries etc


#range
#print(range(10,100))

#for number in range(3,21,4):
#    print('MUAHAHAHHAHAHHA')

#RANGE is very useful and important since u can then easily repeat certain operations over and over

#enumerate
#enumaterate gives u index of all the values in it
for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')

item = [1,2,3,4,5,6,7]
for item in [1,2,3,4,5,6,7]:
    print(item[4])