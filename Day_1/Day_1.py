# Part A
with open('Day_1/Day_1_data.txt', 'r') as data:
    current_total, max_total = 0, 0
    for line in data:
        # Update max total & reset current total after reading an individual elf's input
        if line == '\n':
            max_total = max(max_total, current_total)
            current_total = 0
        else:
            current_total += int(line.strip('\n'))

print('Part A answer:', max_total, sep='\n')

# Part B
import heapq

with open('Day_1/Day_1_data.txt', 'r') as data:
    calories_heap = []; current_total = 0
    for line in data:
        if line != '\n':
            current_total += int(line.strip('\n'))
        # Update calories heap & reset current total after reading an individual elf's input
        else:
            heapq.heappush(calories_heap, current_total)
            # print(calories_heap)
            current_total = 0

    # Updating calories heap with final elf's calories
    heapq.heappush(calories_heap, current_total)
    # print(calories_heap)

print('Part B answer:', sum(heapq.nlargest(3, calories_heap)), sep='\n')