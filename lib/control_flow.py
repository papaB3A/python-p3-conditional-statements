#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username== "ADMIN" or username== "admin") and password== "12345":
        print("Access granted")
    else:
        print("Access denied")
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature< 40:
        print("It's brisk out there!")
    elif temperature>= 40 and temperature<= 65: 
        print("It's a little chilly out there!")
    elif temperature> 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")
    pass

def fizzbuzz(num):
    # your code here
    if (num%3== 0) and (num%5== 0):
        print("FizzBuzz")
    elif num%3== 0:
        print("Fizz")
    elif num%5== 0:
        print("Buzz")
    else:
        print(num)
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation== "+":
        print(num1 + num2)
    elif operation== "-":
        print(num1 - num2)
    elif operation== "*":
        print(num1 * num2)
    elif operation== "/":
        print(num1 / num2)
    else:
        print("Invalid operation!")
        return None
    pass

# admin_login("sudo", "12345")
# admin_login("admin", "12345")
# admin_login("ADMIN", "12345")

# hows_the_weather(33)
# hows_the_weather(99)
# hows_the_weather(75)

# fizzbuzz(1)
# fizzbuzz(2)
# fizzbuzz(3)
# fizzbuzz(4)
# fizzbuzz(5)
# fizzbuzz(15)

# calculator("+", 1, 1)
# calculator("-", 3, 1)
# calculator("*", 3, 2)
# calculator("/", 4, 2)
# calculator("nope", 4, 2)