import time
# Returns current time as seconds since Unix epoch (1970-01-01)
epc = time.time()
print(epc)

# Returns current local time as a struct_time object
localtime = time.localtime(epc)
print(localtime)

# Returns current local time as a struct_time object only year
print(localtime.tm_year)

# Returns current time as a readable string
print(time.ctime(epc))