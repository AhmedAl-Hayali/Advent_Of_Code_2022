# # Part A
# score = 0
#
# # win if diff = -2 or 1, draw if diff = 0, lose otherwise; win -> +6, draw -> +3, loss -> +0
# result_scoring_dict = {
#     -2: 6,
#     -1: 0,
#     0: 3,
#     1: 6,
#     2: 0,
# }
#
# with open('Day_2_data.txt', 'r') as data:
#     for line in data:
#         their_pick, my_pick = line.split()
#         # Get unicode value of each pick
#         uc_their_pick, uc_my_pick = map(ord, (their_pick, my_pick))
#
#         # Map picks to numbers in set {0, 1, 2}, corresponds to {rock, paper, scissors} (essentially enum)
#         uc_their_pick -= 65
#         uc_my_pick -= 88
#         # Compute difference, win if diff = -2 or 1, draw if diff = 0, lose otherwise
#         unicode_diff = uc_my_pick - uc_their_pick
#
#         # uc_my_pick + 1 is the score per item chosen (rock: 1, paper: 2, scissors: 3)
#         score += result_scoring_dict[unicode_diff] + uc_my_pick + 1
#
# print(score)

# Part B
score = 0

# win if diff = -2 or 1, draw if diff = 0, lose otherwise; win -> +6, draw -> +3, loss -> +0

# My picks for input tuple (round_result, their_pick)
my_pick = {
    # My picks to lose (their_pick -make me lose-> my_pick)
    (0, 0): 2,  # rock -> scissors
    (0, 1): 0,  # paper -> rock
    (0, 2): 1,  # scissors -> paper
    # My picks to draw (just mirror what they pick)
    (1, 0): 0,
    (1, 1): 1,
    (1, 2): 2,
    # My picks to win (reverse mapping of "my picks to lose")
    (2, 0): 1,
    (2, 1): 2,
    (2, 2): 0,
}

with open('Day_2_data.txt', 'r') as data:
    for line in data:
        their_pick, round_result = line.split()
        # Get unicode value of each pick
        uc_their_pick, uc_round_result = map(ord, (their_pick, round_result))

        # Map picks to numbers in set {0, 1, 2}, corresponds to {rock, paper, scissors} (essentially an ENUM)
        uc_their_pick -= 65
        uc_round_result -= 88

        # Add 3*result (L: 0, D: 3, W: 6), then my pick (R: 0, P: 1, S: 2) + 1 (R, P, S add 1, 2, 3 not 0, 1, 2)
        score += 3 * uc_round_result + my_pick[(uc_round_result, uc_their_pick)] + 1

print(score)
