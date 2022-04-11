def reverse_and_add_zeroes_for_binary_sum(a: str, b: str) -> (str, str):
    if a > b:
        longest = a[::-1]
        shortest = b[::-1] + "0" * (len(a)-len(b))
    elif b > a:
        longest = b[::-1]
        shortest = a[::-1] + "0" * (len(b)-len(a))
    else:
        longest = a[::-1] + "0"
        shortest = b[::-1] + "0"
    return longest, shortest


def binary_sum(a: str, b: str) -> str:
    longest, shortest = reverse_and_add_zeroes_for_binary_sum(a, b)
    result = ""
    add_to_next = 0
    i = 0

    while i < len(shortest):
        current_rank_sum = int(longest[i]) + int(shortest[i]) + add_to_next
        if current_rank_sum <= 1:
            result += str(current_rank_sum)
            add_to_next = 0
        elif current_rank_sum == 2:
            result += "0"
            add_to_next = 1
        else:
            result += "1"
            add_to_next = 1
        i += 1
    if add_to_next > 0:
        result = result + str(add_to_next)
    return result[::-1]


print(binary_sum('1101', '101'))
