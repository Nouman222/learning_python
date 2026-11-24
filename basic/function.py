# Here i learn the function what is function and why we use it.
# we have 3 type of function builtin function which is standalone function
# usertype function the fuction that created by user
# Methods it also a function but but having role
# The function is differnt for every datatype it depend on datatype to which function use here

text = "hi"
number = 10

print(text)
print(number) # this both are builtin function

print(type(text))
print(type(number)) # this both is also a builtin function but it is nested function one funtion inside another function

print(len(text)) # len function is also bultin function

utext = text.upper() # this is the method 
print(utext)

rtext = text.replace("hi","Hello") # this is also method
print(rtext)

