# ============= search methods ==============

phone = "+49-15484515-3"
print(phone.startswith("+49"))
print(phone.endswith("15"))

email = "nomi@gmail.com"
print("@" in email)
print("$" in email)

phone2 = "+95-8484591518-1"
phone3 = "+95-9448491518-1"
phone4 = "+95-1484997518-1"

print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
print(phone4[phone4.find("-")+1:])


