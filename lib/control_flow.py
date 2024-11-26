#!/usr/bin/env python3

def admin_login(username, password):
   
    if (username.lower() == "admin") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

pass 


def hows_the_weather(temperature):
    # your code here

    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 75:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

    pass

def fizzbuzz(num):
    # your code here
    
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

    pass
def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Division by zero is not allowed.")
            return None
    else:
        print("Invalid operation!")
        return None

    pass
