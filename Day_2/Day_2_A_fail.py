# REASON FOR FAILURE IS PYTHON'S EXPRESSION OF NUMBERS AS TWO'S COMPLEMENT EVEN WHEN UNDESIRED
# SO, F0 AND F1 CAN HAVE ~0 & ~1 = -2 :( IF ONLY THERE WERE BOOLS

# # Part A
score = 0
with open('Day_2_mock_data.txt', 'r') as data:
    for line in data:
        their_pick, my_pick = line.split()
        # Get unicode value of each pick
        uc_their_pick, uc_my_pick = map(ord, (their_pick, my_pick))
        uc_their_pick -= 65; uc_my_pick -= 88
        # Compute difference - 23, win if diff = -2 or 1, draw if diff = 0, lose otherwise
        # unicode_diff = uc_my_pick - uc_their_pick - 23

        x0, x1, x2, x3 = (uc_my_pick >> 1) & 1, uc_my_pick & 1, (uc_their_pick >> 1) & 1, uc_their_pick & 1

        # print(f"{x0=}, {x1=}, {x2=}, {x3=}")

        f0 = (x0 & x3) | (~x0 & ~x1 & x2) | (x1 & ~x2 & ~x3) ### LINES CAUSING ISSUE
        f1 = (x1 & x3) | (x0 & x2) | (~x0 & ~x1 & ~x2 & ~x3) ### LINES CAUSING ISSUE

        score += 3*((f0 << 1) + f1)

        print(their_pick, my_pick, uc_my_pick, uc_their_pick, end='\n\n')

print(score)



# me = ['X', 'Y', 'Z']
# them = ['A', 'B', 'C']
#
# print('  X Y Z')
# for them_let in them:
#     print(them_let, end=' ')
#     for me_let in me:
#         print(ord(me_let) - ord(them_let) - 23, end=' ')
#     print()

# outputs = [-2, -1, 0, 1, 2]
# first = 2
# diff = 2
#
# for output in outputs:
#     print(f'{first} & ({output} + {diff}) = {first & (output + diff)}')

# print('Part A answer:', max_total, sep='\n')