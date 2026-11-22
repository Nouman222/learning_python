# ============ cleaning spaces =============

# ======== lstrip method ========
# now i want to remove the unwanted space from left side
text = "  Engineering".lstrip()
print(text)

# ======== rstrip =========
# now i want to remove the unwanted space from right side
text = "Engineering  ".rstrip()
print(text)

# =========== strip =============
# now i want to remove unwanted spaces from both side left and right
text = "   Engineering   ".strip()
print(text)

# this will remove special character which we want to remove
text = "##nomi##".strip("#")
print(text)

# =============== clean cases ===============

text = "python PROGRAMMING"
# so if i want to convert this into lower case all i will use lower() method

print(text.lower())

# now i want to uppar case

print(text.upper())

# raw = "968-Maria, ( d@t@ Engineer ) ;; 27y  "
# clean_data = raw.lower().strip().replace("@", "a").replace("968", "").replace(";",
#                                                                               "").replace(",", " ").replace("y", "").replace("-", "").replace(")", "").replace("(", "")
# clean_data = clean_data[0:-1].replace("  ", ",").replace(" ","")
# clean_data = clean_data.split(",")
# print(clean_data)
# name = clean_data[0]
# role = clean_data[1]
# age = clean_data[2]
# print(f"name: {name} | role: {role} | age: {age}")


raw = "968-Maria, ( d@t@ Engineer ) ;; 27y "
clean = raw.lower().replace("@", "a")

name = clean.split(",")[0].split("-")[1].strip()
role = clean.split("(")[1].split(")")[0].strip()
age = clean.split(";;")[1].replace("y", "").strip()

print(f"name: {name} | role: {role} | age: {age}")
# Output: name: maria | role: data engineer | age: 27

