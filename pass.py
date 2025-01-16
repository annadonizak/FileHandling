###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password
username_pattern = '^[a-z]{6,}$'    #poczatek i koniec ciagu, male litery, min 6 z
password_pattern = '^[a-zA-Z0-9_]{8,}$' #male/d

# check if username and password are ok
username_match = re.match(username_pattern, username) #czy pasi do wzoru
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
    print("Username and password are valid.")
else:
    if not username_match:
        print("Invalid username")
    if not password_match:
        print("Invalid password")