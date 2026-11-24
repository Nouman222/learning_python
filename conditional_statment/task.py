# validate the quality and correctness of email values
# Must not be empty
# must contain "." and "@"
# must contain exactly one "@" symbol
# must end with ".com",".net",".org"
# must not be longer than 254 character
# must start and end with a letter or digit

email = "$nomi@gmail.com"
# cleaning the string
email = email.strip()
# Must not be empty
if email == "":
    print("Email must not be empty")
# must contain "." and "@"
elif not ("." in email and "@" in email):
    print("Email must contain '.' and '@'")
# must contain exactly one "@" symbol  
elif email.count("@") !=1:
    print("Email must contain only one @")
# must end with ".com",".net",".org"
# elif email.endswith(".com") or email.endswith(".net") or email.endswith(".org"):
elif not (email.endswith((".com",".net",".org"))):
    print('Email must end with ".com",".net",".org"')
# must not be longer than 254 character
elif len(email) > 254:
    print("Email must not be longer than 254 character")
# must start and end with a letter or digit
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")  


# validate the quality and correctness of Passwords 
# Password must not be empty
# Password must be at least 8 characters
# Password must include 1 upper case and 1 lower case
# Password must not be same as the email
# Password must not contain spaces
# Password must start and end with a letter or digit

