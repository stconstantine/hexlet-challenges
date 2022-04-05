def binary_sum(a, b):
    if a > b:
        longest = a[::-1]
        shortest = b[::-1] + "0"
    else:
        longest = b[::-1] + "0"
        shortest = a[::-1] + "0"

    result = ""
    add_to_next = 0
    i = 0
    print(f"shortest = {shortest}")
    print(f"len(shortest) = {len(shortest)}")

    while i < len(shortest):
        print(f"i = {i}")
        print(f"shortest[{i}] = {shortest[i]}")
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

    result = result + longest[i:]

    return result[::-1]


print(binary_sum("11", "1"))
