# import modules
import random

chars = "abcdefghijklomnpqrstuvwyxzABCDEFGHIJKLOMNPQRSTUVWYXZ1234567890!@#$%^&*()"

while 1:
    password_length = int(input("What length will your password to be : "))
    password_count = int(input("how many passwords will you like : "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_length):
            password_char = random.choice(chars)
            password = password + password_char
        print("here is your new password", password)
