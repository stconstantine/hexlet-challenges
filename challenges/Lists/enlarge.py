def show(image):
    for line in image:
        print(line)

def enlarge_line(line):
    result = []
    for element in line:
        result.append(element * 2)
    return ''.join(result)


def enlarge(frame):
    result_frame = []
    for line in frame:
        result_frame.append(enlarge_line(line))
        result_frame.append(enlarge_line(line))
    return result_frame


frame = [
    '1234',
    '*  *',
    '*  *',
    '****'
]

print(enlarge(frame))
