# FizzBuzz task:
# Function returns a string with numbers (separated by spaces) in the range from "begin" to "end", inclusive.
# Wherein:
# – If the number is divisible by 3 without a remainder, then the word Fizz is displayed instead
# – If the number is divisible by 5 without a remainder, then the word Buzz is displayed instead
# – If the number is divisible by both 3 and 5 without a remainder, then the word FizzBuzz is displayed instead
# – In other cases, the number itself is added to the string
# The function takes two parameters (begin and end) that define the beginning and end of the range (inclusive).
# If the range is empty (when begin > end), then the function returns an empty string.

def fizz_buzz(begin, end):
    if begin > end:
        return ""

    first_number = 3
    second_number = 5
    result = ""

    for i in range(begin, end+1):
        if i % (first_number * second_number) == 0:
            add = "FizzBuzz"
        elif i % first_number == 0:
            add = "Fizz"
        elif i % second_number == 0:
            add = "Buzz"
        else:
            add = i
        result = f"{result} {add}"

    return result.strip()


print(fizz_buzz(11, 20))
