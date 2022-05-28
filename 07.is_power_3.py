# https://ru.hexlet.io/challenges/python_basics_power3_exercise

from time import time


def is_power_of_three(number):
    for i in range(0, int(pow(number, 1/3)+1)):
        if 3 ** i == number:
            return True
    return False


def is_power_of_three_h(number):
    counter = 1  # 3 ** 0
    while counter < number:
        counter *= 3
    return counter == number


N = 1
while N < 1000000000000:
    start_time = time()
    is_power_of_three(N)
    stop_time = time()
    f1 = stop_time - start_time

    start_time = time()
    is_power_of_three_h(N)
    stop_time = time()
    f2 = stop_time - start_time

    print(f"N = {N}, вычисление pow(.., 1/3) – {f1 * 1000000}, полный проход - {f2 * 1000000}")

    N *= 1000
