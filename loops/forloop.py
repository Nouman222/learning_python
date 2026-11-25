# ======== for loop ========
for i in (1, 2, 3, 4, 5):
    print(f"Round: {i}")

rounds = (1, 2, 3, 4, 5)

for round in rounds:
    print(f"Round: {round}")

for i in range(5):  # same like the above but it start from zero
    print(f"Round: {i}")

for i in range(2,10):  # same like the above but here the start and end we declear
    print(f"Round: {i}") 

for i in range(0,10,2):  # here it will start from 0 and take 2 step and end on 10 but it will not include and here the 9 will also not print because it take 2 step after 8 is 10 and 10 is not include
    print(f"Round: {i}") 


name = "Nouman"
for chr in name:
    print(chr)

heros_name = ["nomi","khan","khalil","afridi","Pakistani"]
for name in heros_name:
    print(name)

# =============================================================
scores = [85,90,75,80,99,100]
total = 0

for score in scores:
    # total = total + score
    total += score
    print(f"current total score: {total}")

print(f"final total score: {total}")

# =============================================================

files = ["  Reporting.csv ", "DATA.csv "," final.TXT"]

for file in files:
    file = file.strip().lower().replace(".txt","csv")
    print(f"File: {file}")

# =============================================================

# print the 7 times table from 1 to 10
for i in range(7,71,7):
    print(i)

# ======================= loop control =========================

# ========= Break statment ========
# it stop the loop immediatly it jump out and end the loop right away

heros_name = ["nomi","khan","khalil","afridi","Pakistani"]
for name in heros_name:
    if name == "khalil" or name == "afridi":
        print("Unknown names detected")
        break
    print(name)

# ========== continue statment ======
# it skip one loop cycle without stoping the loop 
names = ["nomi","khan","","Pakistani"]
for name in names:
    if name == "":
        print("Empty value detective")
        continue
print(name)

# ======== pass statment ========
# it just pass not skipping or ending the loop it is just like place holder
names = ["nomi","khan","","Pakistani"]
for name in names:
    if name == "":
        pass
print(name)
# =====================================
# ============= Task ==================

# print doublicate found if exists other wise print all files are unique
file_list = ["report.csv", "data.xlsx", "summary.docx", "report.csv", "data.csv"]

seen = []
duplicate_found = False

for file in file_list:
    if file in seen:
        duplicate_found = True
        break
    seen.append(file)

if duplicate_found:
    print("Duplicate found")
else:
    print("All files are unique")


# file_list = ["report.csv", "data.xlsx", "summary.docx", "report.csv", "data.csv"]

# duplicate_found = False

# for file in file_list:
#     if file_list.count(file) > 1:
#         duplicate_found = True
#         break

# if duplicate_found:
#     print("Duplicate found")
# else:
#     print("All files are unique")

# ============================= Nested for loop ============================

# one loop inside the loop 
for x in range(3): # This is the outer loop
    for y in range(2): # This is the inner loop
        print(f"({x},{y})")

years = ["2026","2027"]
months = ["Jan","Feb"]

for y in years:
    for m in months:
        for d in range(1,28):
            print(f"File_{y}_{m}_{d}.csv")

