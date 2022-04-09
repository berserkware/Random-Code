import re

email = input("Enter your email -> ")

if(re.match("[^@]+@[^@]+\.[^@]+", email)):
    print("that is a valid email")
else:
    print("that is not a valid email")
