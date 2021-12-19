# Bullshit exercises from practicepython.org

# 1. input from user (age and name)
# 2. Make sure its a dictionary string:age
# 3. Calculate age until 100 years old.
# 4. Print age, adressed to user.
from datetime import datetime

year = datetime.today().year
name = input("Whats your name?\n")
age = int(input("How old do you turn this year?\n"))
birthday = input("What month where you born in?\n")
age_calculation = year - age + 100

relay_information = "Your name is {} and you will turn 100 years old in year: {}".format(name, age_calculation)

print(relay_information)