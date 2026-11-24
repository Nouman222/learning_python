# =========== boolean logic ===========
print(True)
print(False)
print(type(True))
print(type(False))

print(bool(1234))
print(bool("HI"))

print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

email = "nouman@gmail.com"
phone = "45-48845845848-6"
name = ""
print(any([email,phone,name]))
print(all([email,phone,name]))

email = "nouman@gmail.com"
phone = "45-48845845848-6"
name = "nomi"
print(all([email,phone,name]))
print(any([email,phone,name]))


print(isinstance(1234,int))
print(isinstance(True, str))

print("hello".endswith("o"))
print("hello".startswith("o"))


# ======== operators logic ============
print(10 == 10)
print(10 != 10)

print(7 > 3)
print(7 >= 7)

print(3 < 7)
print(3 <= 7)

print("a" < "b")
print("a" > "b")
print("a" == "b")
print("a" == "A")
print("a" == "a")

print(1 < 4 < 6)

print(1 < 4 > 6)

print(1 > 4 < 6)

age = 20

print(age >= 18)

# ========== logical operators ===========
print(3 > 1 and 1 > 5)
print(3 > 1 and 1 < 5)

print(4 > 5 or 4 < 6)
print(5 == 5 or 10 < 8)
print(5 != 5 or 4 > 5)

cpu_usage = 70
memory_usage = 95

print(cpu_usage > 90 or memory_usage > 90)

email = True
password = False

print(email and password)

# Now going to learn NOT operator it change if True it say false and if false it say true
print(not 3 > 1)
print(not 3 < 1)

print(not True)
print(not False)

name = ""
print(not name)

# ========= control operators ===========
is_login = True
is_guest = False
is_banned = False

print(is_login or is_guest and not is_banned)

is_login = True
is_guest = False
is_banned = True

print((is_login or is_guest) and not is_banned)

# ========= membership in operator ==========
print("o" in "python")
print("o" in "data")
print("o" not in "data")

domain = "gmail.com"
block_domain = ["fake.com","spam.org","bot.com"]

print(domain in block_domain)

domain = "fake.com"
print(domain in block_domain)
print(domain not in block_domain)

# ========= is operator ==========
x = ["a","b","c"]
y = ["a","b","c"]

print(x == y) # here python check the values so there for it is true
print(x is y) # here python check the memory id so it is false

x = ["a","b","c"]
y = x 
print(x == y)
print(x is y)

