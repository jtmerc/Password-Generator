# Import modules
from random import randint

# All uppercase
password = ""
for i in range(13):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# Random Generator - Upper and Lowercase password
password = ""
for i in range(6):
    i = chr(randint(65, 90))
    for j in range(6):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)
