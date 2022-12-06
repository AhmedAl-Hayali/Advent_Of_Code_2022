# Part A
marker_length = 4

with open('Day_6_test_data.txt', 'r') as data:
    for line in data:
        seen_chars = {char for char in line[:marker_length]}

        # If first `marker_length` chars are distinct, we have the solution immediately
        if len(seen_chars) == marker_length:
            result = marker_length

        char_pos = marker_length - 1

        while char_pos < len(line) and len(seen_chars) != marker_length:
            char = line[char_pos]

            if char in seen_chars:
                print("foo")
                for i in range(1, marker_length):
                    print(line[char_pos - i], line[char_pos - marker_length + 1: char_pos + 1])
                    if line[char_pos - i] == char:
                        char_pos += marker_length - i + 1
                        break
                seen_chars = {char for char in line[char_pos - marker_length + 1: char_pos + 1]}
                print(seen_chars)
            else:
                # seen_chars.add(char)
                # seen_chars.remove(line[char_pos - marker_length])
                seen_chars = {char for char in line[char_pos - marker_length + 1: char_pos + 1]}
                char_pos += 1
        print(line, ' '*(char_pos - marker_length - 1) + '^'*(marker_length), seen_chars, char_pos)

# Part B