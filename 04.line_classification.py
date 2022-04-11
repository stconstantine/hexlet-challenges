# https://ru.hexlet.io/challenges/python_basics_line_classification_exercise
# A bunch of bool function with lines


def is_degenerated(line):
    p1, p2 = line
    return p1 == p2


def is_vertical(line):
    (x1, y1), (x2, y2) = line
    return not is_degenerated(line) and x1 == x2


def is_horizontal(line):
    (x1, y1), (x2, y2) = line
    return not is_degenerated(line) and y1 == y2


def is_inclined(line):
    return not (is_vertical(line) or is_horizontal(line) or is_degenerated(line))


line1 = (0, 10), (100, 130)
line2 = (42, 1), (42, 2)
line3 = (100, 50), (200, 50)
line4 = (0, 0), (0, 0)

print(is_vertical(line2))
