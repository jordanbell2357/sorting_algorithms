import bisect
import timeit
import random
import csv

NAME_FILE_PATH = 'names.txt'
SORTED_NAME_FILE_PATH = 'sorted_names.txt'

with open(NAME_FILE_PATH, 'r') as f:
    name_list_newlines = f.readlines()
    name_list = [n.removesuffix('\n') for n in name_list_newlines]
    sorted_name_list = sorted(name_list)
    sorted_name_list_newlines = [n + '\n' for n in sorted_name_list]
    with open(SORTED_NAME_FILE_PATH, 'w') as sorted_file:
        sorted_file.writelines(sorted_name_list_newlines)

# target_name = random.choice(sorted_names)

# ITERATIONS = 100

# print(timeit.timeit(lambda: target_name in sorted_names, number=ITERATIONS))

# print(timeit.timeit(lambda: bisect.bisect_left(sorted_names, target_name), number=ITERATIONS))