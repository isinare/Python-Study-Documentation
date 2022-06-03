def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)        


print(highest_even([10,8,6,5,3,4,11,55]))
