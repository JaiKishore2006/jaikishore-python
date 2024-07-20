# fibonacci(recursiom)

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = 119283
# print("the number is fibonacci")

#task2

# def factorial(n):
#     if n < 0:
#         return "Invalid input: Negative number"
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# try:
#     number = int(input("Enter a number : "))
#     result = factorial(number)
#     print(result)
# except ValueError:
#     print("Invalid input")

# task3


# class Counter:

#     __count = 0
    
#     @classmethod
#     def get_count(cls):
#         return cls.__count
    
#     @classmethod
#     def increment(cls):
#         cls.__count += 1
    
#     @classmethod
#     def decrement(cls):
#         if cls.__count > 0:
#             cls.__count -= 1
    
#     @classmethod
#     def reset(cls):
#         cls.__count = 0


# print("Initial count:", Counter.get_count())  

# Counter.increment()
# Counter.increment()
# print("After 2 increments:", Counter.get_count())  

# Counter.decrement()
# print("After 1 decrement:", Counter.get_count())  

# Counter.reset()
# print("After reset:", Counter.get_count())  


# print("Access __count using name mangling:", Counter._Counter__count)  

#task4

# from functools import reduce

# def factorial(n):
    
#     if n == 0:
#         return 1
    
#     num_list = list(range(1, n + 1))
    
#     result = reduce(lambda x, y: x * y, num_list)

#     return result
# number = 5
# print(number)

#TASK5

# def is_armstrong(number):
#     num_digits = len(str(number))
 
#     sum_of_powers = sum(int(digit) ** num_digits for digit in str(number))
    

#     if sum_of_powers == number:
#         return True
#     else:
#         return False

# num = 153
# if is_armstrong(num):
#     print("armstrong number")
# else:
#     print("not an armstrong number")

#leap year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = 2024
if is_leap_year(year):
    print("leap year")
else:
    print("not a leap year.")

#task6

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_str = "Madam"
if is_palindrome(input_str):
    print(is_palindrome)
else:
    print(" is not a palindrome")




