# https://ru.hexlet.io/challenges/python_basics_tuple_rotation_exercise

def rotate_left(triple_arg):
    a, b, c = triple_arg
    return b, c, a


def rotate_right(triple_arg):
    a, b, c = triple_arg
    return c, a, b


triple = ('A', 'B', 'C')
print(triple)
print(f"rotate_left = {rotate_left(triple)}")
print(f"rotate_right = {rotate_right(triple)}")
