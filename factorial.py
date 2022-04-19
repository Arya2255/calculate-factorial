# clean code solution
def factorial_using_for_loop(number):
    factorial = 1
    for i in range(1, number+1):
        factorial = factorial * i
    print("The factorial of {} is: {}".format(number, factorial))

# solution using library
def factorial_using_math_library(number):
    import math
    result = math.factorial(number)
    print("The factorial of {} is: {}".format(number, result))

# my solution
def factorial_using_my_algorithm(number):
    result = 1
    while number != 1:
        result *= number
        number-=1
    result *= number
    print("The factorial of {} is: {}".format(number, result))

number = int(input("please Enter integer number: "))
factorial_using_my_algorithm(number)
# factorial_using_math_library(number)
# factorial_using_for_loop(number)