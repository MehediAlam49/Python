fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

# add operation
fruits.add('guava')
print(fruits)

#remove operation
fruits.remove('banana') #Removes an element (error if missing)
print(fruits)

#discard operation
fruits.discard('banana') # Removes an element (no error)
print(fruits)

# pop operations
fruits.pop() #Removes and returns a random item
print(fruits)

# clear operation
fruits.clear()
print(fruits)


# union operation
s1 = {1, 2, 3,8,7}
s2 = {2,5,8,0,9}
print(s1.union(s2)) #Combines sets

# intersection operation
print(s1.intersection(s2)) #Common elements

# difference operation
print(s1.difference(s2)) # Elements in set1 not in set2
