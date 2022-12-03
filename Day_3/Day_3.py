# Part A
# import string
#
# lowercase_letters_set = set(string.ascii_lowercase)
# priority = 0
#
# with open('Day_3_data.txt', 'r') as data:
#     for line in data:
#         # Count of items in rucksack
#         item_count = len(line.strip('\n'))
#
#         items_in_compartment_1 = set(line[:item_count // 2])
#         items_in_compartment_2 = set(line[item_count // 2:])
#
#         item_in_both = items_in_compartment_1.intersection(items_in_compartment_2).pop()
#         # Unicode of item (letter) in both compartments
#         uc_item_in_both = ord(item_in_both)
#
#         priority += uc_item_in_both - 96 if item_in_both in lowercase_letters_set else uc_item_in_both - 38
#
# print(priority)

# import string
# Generate look-up table for letter -> priority, but can be simpler as done above
# print('{',
#       *[f'\t{letter}: {ord(letter) - 96}' for letter in string.ascii_lowercase],
#       *[f'\t{letter}: {ord(letter) - 38}' for letter in string.ascii_uppercase],
#       '}',
#       sep='\n')


# Part B
import itertools
import string

lowercase_letters_set = set(string.ascii_lowercase)
priority = 0

with open('Day_3_data.txt', 'r') as data:
    # Indefinitely read next 3 lines until EOF (reads <= 3 lines on final read)
    while True:
        # current_group of elves (usually 3 elves, but either of {1, 2, 3} for semi-final, & 0 for final read)
        # Credit: https://stackoverflow.com/a/6335876
        current_group = list(itertools.islice(data, 3))

        # Break out of indefinite loop when at EOF (empty list of elves)
        if not current_group:
            break
        # Otherwise, non-empty list of elves

        # Set of items in backpack; last char (`\n`) erased
        current_group_sets = [set(elf_backpack[:-1]) for elf_backpack in current_group]

        # Invariant: 1 <= # elves <= 3, so indexing list only causes an IndexError at indices 1 & 2
        try:
            # Separated to
            shared_item = current_group_sets[0].intersection(current_group_sets[1])
        except IndexError:
            print("Failed first intersection, group size is 1 elf:",
                  current_group_sets[0],
                  sep='\n')
            pass

        try:
            shared_item = shared_item.intersection(current_group_sets[2])
        except IndexError:
            print('Failed second intersection, group size is 2 elves:',
                  current_group_sets[0],
                  current_group_sets[1],
                  sep='\n')
            pass

        shared_item = shared_item.pop()

        # Unicode of item (letter) shared by elves
        uc_shared_item = ord(shared_item)

        priority += uc_shared_item - 96 if shared_item in lowercase_letters_set else uc_shared_item - 38

print(priority)
