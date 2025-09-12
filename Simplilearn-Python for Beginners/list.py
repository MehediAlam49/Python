# number list
num = [1,3,5,6,0]
print(num)

# letter list
letter = ['m','e','h','e','d','i']
print(letter)

# string list
str = ['mehedi','alam','md','saiful','alam']
print(str)

# Mixing list
mix = ['mehedi',49, True, 'simplilearn','course']
print(mix)

# matrix list
mat = [[1,2],[3,4],[8,9]]
print(mat)



# -----Access of Elements------

# length of list
print(len(mix))

# Access element using index
print(mix[:3])
# Access element using reverse index
print(mix[3:])
# Access element using rang of index

print(mix[2:4])
# Access element every 2nd index
print(mix[::2])
# Access element using reverse index
print(mix[::-1])



# -----Operations in list------
# print specific number of content in list
print([0]*100)

# concatinate 2 string
conc = letter + str
print(conc)

# extract the letter of a string
text = list("This is Mehedi")
print(text)

# seperate the value of a string
one, *other = str
print(one)
print(other)



# -------Methods in list

# append method
print(num)
num.append(9)
print(num)

# extend method
num.extend(str)
print(num)

# insert method
num.insert(6,'Aowlad')
print(num)

# remove method
num.remove('md')
print(num)

# sort method
str1 = ['e','o', 'q','j','a', 'z']
str1.sort()
print(str1)





# --------------Python built-in functions---------

x = [4,8,889,365,56,4,5,2,85]
# Length of the number of this list
print(len(x))
# Minimum number of this list
print(min(x))
# Maximum number of this list
print(max(x))
# Sum of the number of this list
print(sum(x))
# Average of the number of this list
print(sum(x)/len(x))