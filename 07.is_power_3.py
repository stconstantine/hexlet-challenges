# https://ru.hexlet.io/challenges/python_basics_power3_exercise

def is_power_of_three(number):
    for i in range(0, int(pow(number, 1/3)+1)):
        if 3 ** i == number:
            return True
    return False

print (is_power_of_three(26))