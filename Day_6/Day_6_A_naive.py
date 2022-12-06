# Part A, Naive implementation
marker_length = 4

with open('Day_6_data.txt', 'r') as data:
    for line in data:
        char_pos = marker_length - 1

        seen_chars = {char for char in line[char_pos - marker_length + 1:char_pos + 1]}

        while len(seen_chars) != marker_length:
            seen_chars = {char for char in line[char_pos - marker_length + 1:char_pos + 1]}
            char_pos += 1

        print(char_pos, line.rstrip('\n'))

# Part B, Naive implementation
marker_length = 14

with open('Day_6_data.txt', 'r') as data:
    for line in data:
        char_pos = marker_length - 1

        seen_chars = {char for char in line[char_pos - marker_length + 1:char_pos + 1]}

        while len(seen_chars) != marker_length:
            seen_chars = {char for char in line[char_pos - marker_length + 1:char_pos + 1]}
            char_pos += 1

        print(char_pos, line.rstrip('\n'))
