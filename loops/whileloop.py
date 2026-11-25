# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# ans = ""
# while ans != "yes":
#     ans = input("Do you love me? yes/no ")
# print("Thank you")

# ================== while with if and break statment ================
# while True:
#     reply = input("Do you agree? (yes/no) ")
#     if reply == "yes":
#         break
# print("Thank You")

# ============== Task ==============
# allow upto 3 attempts
# if the user type yes print glad we are on the same page 
# otherwise print 3 strikes you are out
strike = 0

while strike < 3:
    reply = input("Do you agree? (yes/no) ").strip().lower()
    
    if reply == "yes":
        print("Glad we are on the same page")
        break
    else:
        strike += 1
        if strike == 3:
            print("3 strikes, You are out")


