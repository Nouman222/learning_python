# ====== if standalone statement==========
score = 100
if score >= 90:
    print("A")

# identation 
# like the above print show us this statment is belong to if statment if there is no tab space 
# this print will not belong to that if statement 

# another example of indentation is 
mark = 65
if mark >= 60:
    print("Pass")
print("hello")
# here the pass print is the if statemtn print it belong to if statment and the hello print is independent it is not 
# so if statment is True then the pass print will print if not only the hello print will print because that is not depend on if statment

# ========== if and else statment =========
score = 70
if score >= 90:
    print("A")
else:
    print("F")

# ====== multiple condition elif ==========
score = 70
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("F")

age = 20
if age >= 18:
    print("You are eligible")
elif age >= 14 and age < 18:
    print("you are young and not eligible")
elif age >= 5:
    print("you are too young not eligible")
else: 
    print("You are a child")

# ======= nested if ===========
score = 95
project_submited = True
if score >= 90:
    if project_submited:
        print("A+")
    else:
        print("A")
elif score >= 75:
    print("B")
else:
    print("F")

# ======== connection conditon statments ========
age = 22
medical_Tast = True
if age >= 18 and medical_Tast:
    print("You are eligiable")
elif age == 17 or age > 14:
    print("You are young not eligiable")
else:
    print("Not eligiable")

# ======= Ternary or short form =========
# the long form of if else statment 
score = 70

if score >= 90:
    print("A")
else:
    print("F")     

# the ternary the short form but can use of for if else statment not nested not not complex logic
print("A" if score >= 90 else "F")

grade = "A" if score >= 90 else "F"
print(grade)

# ========= match case ============
# convert full name into short form 

# The long form
country = "United State"
if country == "United State":
    print("US")
elif country == "India":
    print("Ind")
elif country == "Pakistan":
    print("PK")
elif country == "Afghanistan":
    print("AFG")
else:
    print("unknown country")

# short form is
match country:
    case "United State":
        print("US")
    case "India":
        print("Ind")
    case "Pakistan":
        print("PK")
    case "Afghanistan":
        print("AFG")
    case _:
        print("Unknown country")

        