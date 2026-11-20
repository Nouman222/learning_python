name = "Nouman"
print(type(name))

age = 23
print(type(age))

# print("Your age is" + age) this give us error because we can't oprate string with interger so will will convert int to str

print("Your age is " + str(age))

password = "123a"

print(len(password)) # this will show us the length of character in a string the space is also count 

text = """
python is easy to learn.
python is powerful.
Many people love python.
"""
print(text.count("python")) # the count() method show how many times the specific string come.

# ==========================================
# The transformation methods start here we have two methods and four oprators
# ==========================================
# ======= replace method ==========
price = "1234,56"
print(price)

# here i want to replace , with . so i will use the replace method which take two argument
price.replace(",", ".")
print(price)

phone = "92/31254848/48"
print(phone.replace("/", "-"))

# now if i want to don't replace just remove same method but work different
print(phone.replace("/","")) # here / will remove nothing will replace 

# the second method is join two string using + oprator
# ======= oprator method to join str ==========
first_name = "Nouman"
last_name = "Ahmad"
full_name = first_name + last_name
print(full_name)
# if we want space b/w first and last name we have to join empty " "
full_name = first_name + " " + last_name
print(full_name)


# Now i will learn f string method
# ============ f string method ==========
name1 = "Nomi"
age2 = 25
country = "Pakistan"

print(f"User name is {name1} age is {age2} and from {country}") # so with the help of f string we can join variables with string without + oprator

print(f"20 - 10 = {20-10}")

# ======== split method ===========
stamp = "20-11-2026 12:58"
print(stamp.split(" "))

stamp2 = "20-11-2026"
print(stamp2.split("-"))

stampsplit = stamp2.split("-")
print(type(stampsplit))

# ======= string repetation ==========
print("ha" * 4)

print("=" * 20)

print("your are great")

# ========= indexing and slicing of string ===========

p = "python"

print(p[1]) # here i am extracting y which is on index 1 
print(p[-5]) # this is also extraction y but from - 

# now i want to extract py 
print(p[0:3]) # here 0 is the start index and 3 is the end index and 3 is not include in the ouput 

# if i want to print from y so i can
print(p[2:]) # we don't need to write the end this will start from index 2 with the last 

# now if i want to skip every second charcter 
print(p[0:6:2]) # this will print pto because every second index skip it print p then skip y then print t then skip h and then print o then skip n and finsh







