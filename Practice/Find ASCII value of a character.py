sum = 0
print ("Please enter the String: ", end = "")  
string = input()  
string_length = len(string)  
for K in string:  
    ASCII = ord(K) 
    sum = sum + ASCII
    print (K, "\t", ASCII)  
print("\nThe Sum of each character ASCII code ", string, "is: ", sum)
