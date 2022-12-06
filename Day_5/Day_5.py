# # Part A
# import re
# stacks = []
#
# with open('Day_5_data.txt', 'r') as data:
#     for line in data:
#         # Halt reading when finished reading stack/container layout
#         if line[0] == '\n':
#             break
#         if line[1] == '1':
#             continue
#
#         # Useful information is only available every 4th character (starting at 2nd character)
#         for i in range(1, len(line), 4):
#             # If no container in position, skip to next position
#             if line[i] == ' ':
#                 continue
#
#             # Invariant: All container positions to the "left" of current position have allocated stacks, empty or not
#
#             # Adjusted i, from character position in `line` to container position in `line` and correspondingly `stacks`
#             container_position = (i - 1) // 4
#
#             # If we have yet to allocate a stack to the container position or ones preceding it
#             if container_position > len(stacks):
#                 # Allocate as many stacks as necessary for preceding container positions
#                 stacks += [[] for _ in range(container_position - len(stacks))]
#                 # Then create stack with current container item
#                 stacks.append([line[i]])
#
#             # If we have stacks for preceding positions but not the current one
#             elif container_position == len(stacks):
#                 # Create current stack with current container item
#                 stacks.append([line[i]])
#
#             # If we have a stack for current position
#             else:
#                 # Directly index and add container to stack
#                 stacks[container_position].append(line[i])
#
#     # By now, we have read in stack, and discarded 2 lines (enumeration of containers and newline character on `line`)
#
#     # Reading & executing container moves
#     for line in data:
#         # Read all (3) numbers in 'move `n_containers` from `from_stack` to `to_stack`'
#         n_containers, from_stack, to_stack = map(int, re.findall(r'\d+', line))
#
#         # Repeated stack pop & insert reverses order, so we insert `n_containers` into `to_stack` in reverse order
#         # from `from_stack`, adjusting indices by 1 because our stacks are 0-indexed whereas containers are 1-indexed
#         # first_n_from_stack = [stacks[from_stack - 1][i] for i in range(n_containers)]
#         first_n_from_stack = stacks[from_stack - 1][:n_containers]
#         stacks[to_stack - 1] = first_n_from_stack[::-1] + stacks[to_stack - 1]
#
#         # Remove `n_containers` from `from_stack` to reflect movement to `to_stack`
#         stacks[from_stack - 1] = stacks[from_stack - 1][n_containers:]
#
# print(''.join([stack[0] for stack in stacks]))

# Part B - only one line altered lol
import re
stacks = []

with open('Day_5_data.txt', 'r') as data:
    for line in data:

        if line[0] == '\n':
            break
        if line[1] == '1':
            continue

        for i in range(1, len(line), 4):
            if line[i] == ' ':
                continue

            container_position = (i - 1) // 4

            if container_position > len(stacks):
                stacks += [[] for _ in range(container_position - len(stacks))]
                stacks.append([line[i]])
            elif container_position == len(stacks):
                stacks.append([line[i]])
            else:
                stacks[container_position].append(line[i])

    for line in data:
        n_containers, from_stack, to_stack = map(int, re.findall(r'\d+', line))

        first_n_from_stack = stacks[from_stack - 1][:n_containers]
        # Only changed line of code, instead of a LIFO pop of containers, it's FIFO dequeue behaviour, so no reversal
        # stacks[to_stack - 1] = first_n_from_stack[::-1] + stacks[to_stack - 1]
        stacks[to_stack - 1] = first_n_from_stack + stacks[to_stack - 1]

        stacks[from_stack - 1] = stacks[from_stack - 1][n_containers:]

print(''.join([stack[0] for stack in stacks]))
