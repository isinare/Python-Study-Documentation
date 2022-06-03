#sets are lists where u cant have duplicates, with other functions to add subtract and do various other operations on multiple sets
my_set = {1,2,3,4,5,6,7,8}
my_set.add('POG')
my_set.discard(2)
print('POG' in my_set)

# add()	| Adds an element to the set
# clear() |	Removes all the elements from the set
# copy() |	Returns a copy of the set
# difference() |	Returns a set containing the difference between two or more sets
# difference_update() | 	Removes the items in this set that are also included in another, specified set
# discard()	| Remove the specified item
# intersection() |	Returns a set, that is the intersection of two or more sets
# intersection_update() | 	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() | 	Returns whether two sets have a intersection or not
# issubset() |	Returns whether another set contains this set or not
# issuperset() |	Returns whether this set contains another set or not
# pop() |	Removes an(the last) element from the set
# remove()	| Removes the specified element
# symmetric_difference() |	Returns a set with the symmetric differences of two sets
# symmetric_difference_update() |	inserts the symmetric differences from this set and another
# union() | 	Return a set containing the union of sets
# update() |	Update the set with another set, or any other iterable
