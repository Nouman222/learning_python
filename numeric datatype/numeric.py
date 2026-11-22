import math
import random

x = 50
y = 3.14
z = 2 + 3j 
print(type(x))
print(type(y))
print(type(z))

p = "1947"
print(type(p))
p = int(p)
print(type(p))

# ============= maths oprators ===========

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 4)

x = 2
# x = x + 8 
print(x) 
x += 8 # this is the shorcut of above
print(x) 

x -= 5
print(x)

x *= 5
print(x)

# ============ rounding methods ===========

price = 49.995484488448
print("rounded price:", round(price))
print("rounded with 2 decimal price:", round(price,2))
print("rounded with 1 decimal price:", round(price,1))
print("floor price:", math.floor(price))
print("ceil price:", math.ceil(price))

print("trunc price", math.trunc(price)) # this mathod is strikly show only the first int number not like rounding floor or ceil


# ============ random methods =======

print(random.random())

print(random.randint(1,6))


# ======== validation methods ============
x = 7.0
print(x.is_integer())

y = 7.1
print(y.is_integer())

z = 20
print(isinstance(x, int))
print(isinstance(x, float))

y = random.randint(1,100)

z = y % 2 == 0

print("z:", z)






