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