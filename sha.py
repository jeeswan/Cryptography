# Python 3 code to demonstrate 
# SHA hash algorithms. 

import hashlib 

# initializing string 
str = "Jeeswan"

# encoding GeeksforGeeks using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "Jeeswan"

# encoding GeeksforGeeks using encode() 
# then sending to SHA384() 
result = hashlib.sha384(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA384 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "Jeeswan"

# encoding GeeksforGeeks using encode() 
# then sending to SHA224() 
result = hashlib.sha224(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA224 is : ") 
print(result.hexdigest()) 

print ("\r") 

