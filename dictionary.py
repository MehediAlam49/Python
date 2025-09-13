dict = {1:'how',2:'are', 3:'you'}
d = {1:'Welcome', 2:'here', 'name':{'fname':'Mehedi', 'lname':'Alam'}}

# dictionary
print(dict)

# nested dictionary
print(d)

# add element
d['age']=24
print(d)

# update element
d.update({'age':25})
print(d)

# access element
print(d['age'])

# access element using get method
print(d.get('city')) # get used for if you not sure key is exits or not and avoid error
print(d.get(1))

# accessing nested dict
print(d['name']['fname'])


# -----delete element

#used pop method
d.pop('age') #delete specific item
print(d)

# used popitem
d.popitem() # popitem delete the last item
print(d)


# ----In-build function
#values method
print(d.values())

# clear method
d.clear()
print(d)