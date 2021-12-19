user_input = int(input("Please give me a number and ill tell you if its even or odd: "))
calculation = user_input % 2

if(calculation == 0):
    print("The number you entered is even.")

else:
    print("The number you entered is odd.")