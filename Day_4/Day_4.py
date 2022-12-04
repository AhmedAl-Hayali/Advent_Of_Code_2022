# # Part A
# import re
# result = 0
#
# with open('Day_4_data.txt', 'r') as data:
#     for line in data:
#         # Input is in the following form: 'a-b,c-d\n'
#         # Strip newline character then split on both dashes and comma, giving the list [a, b, c, d]
#         # a, b are endpoints of first elf's sections, and c, d are those of the second elf
#         elf_sections_endpoints = re.split(r'[,\-]', line.strip())
#         elf_1_l, elf_1_r, elf_2_l, elf_2_r = list(map(int, elf_sections_endpoints))
#
#         # If 1st elf's left endpoint is to the left of 2nd elf's, they will overlap only if 1st right endpoint
#         # meets, or surpasses, right endpoint of 2nd elf
#         if elf_1_l < elf_2_l:
#             result += elf_1_r >= elf_2_r
#             # print(str(elf_sections_endpoints) + '\n' if elf_sections_endpoints[1] >= elf_sections_endpoints[3] else '',
#             #       end='')
#
#         # If left (or right, really, but that's incorporated in others) endpoints coincide, they will overlap regardless
#         elif elf_1_l == elf_2_l:
#             result += 1
#             # print(str(elf_sections_endpoints) + '\n' if elf_sections_endpoints[0] == elf_sections_endpoints[2] else '',
#             #       end='')
#
#         # If 1st elf's left endpoint is to the right of 2nd elf's, they will overlap only if 1st right endpoint
#         # meets, or does not surpass, right endpoint of 2nd elf
#         else:
#             result += elf_1_r <= elf_2_r
#             # print(str(elf_sections_endpoints) + '\n' if elf_sections_endpoints[1] <= elf_sections_endpoints[3] else '',
#             #       end='')
#
# print(result)


# Part B
import re

result = 0

with open('Day_4_data.txt', 'r') as data:
    for line in data:
        # Loading data as I did in Part A
        elf_sections_endpoints = re.split(r'[,\-]', line.strip())
        elf_1_l, elf_1_r, elf_2_l, elf_2_r = list(map(int, elf_sections_endpoints))

        # If any of the endpoints of either elf lie within the limits bounded by the endpoints of the other elf, there
        # is an overlap
        result += elf_2_l <= elf_1_l <= elf_2_r or \
                  elf_2_l <= elf_1_r <= elf_2_r or \
                  elf_1_l <= elf_2_l <= elf_1_r or \
                  elf_1_l <= elf_2_l <= elf_1_r

print(result)
