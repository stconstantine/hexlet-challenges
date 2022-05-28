# https://ru.hexlet.io/challenges/python_basics_angle_difference_exercise

def reduct_angle(angle):
    return angle % 360


def diff(a1: int, a2: int):
    a1 = reduct_angle(a1)
    a2 = reduct_angle(a2)

    straight_angle = max(a1, a2) - min(a1, a2)

    return min(straight_angle, 360 - straight_angle)


print(diff(315, 45))
