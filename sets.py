# Creating and printing a list
list1=[1,1,2,2,3,3]

# Creating and printing a set
set1=set(list1)


#   print(set1[1]) - set not indexable

# Checking if 4 is in the set
if 4 in set1:
    print("Element present")
else:
    print("Element not present")

# Checking if 2 is in the set
if 2 in set1:
    print("Element present")
else:
    print("Element not present")

# Adding elements to the set
myset=set([])
myset.add(3)
myset.add(4)
myset.add(2)
myset.add(3)
myset.add(1)
myset.add(5)
myset.add(6)


# Removing an element from the set
myset.remove(5)


# Removing an element (Option 2)
myset.discard(1)
print(myset)

"""
set operations
1. Union - additon of sets
2. Intersection - common elements between two sets
3. Difference - elements present in the first set
4. Symetric Difference - union - intersection
"""
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}

print(a.union(b))
# print(a | b) - Option 2

print(a.intersection(b))
# print(a&b) - Option 2

print(a.difference(b))
print(b - a)


print(a.symmetric_difference(b))
# print(a^b) - Option 2