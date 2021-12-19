# Bullshit exercises from practicepython.org

# 1. input from user (age and name)
# 2. Make sure its a dictionary string:age
# 3. Calculate age until 100 years old.
# 4. Print age, adressed to user.

user_birth = input("What year, month and date were you born? Answer in this format: yyyy mm dd\n")
user_birth_2 = user_birth.split()
list_object = list(user_birth_2)
making_int = int(list_object[0])

calculation = making_int[0] + 100

print("You will turn 100 years old in year: {}".format(calculation))