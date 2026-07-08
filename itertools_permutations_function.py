# itertools_permutations_function.py

from itertools import permutations

def itertools_permutations_function():
    user_input = input().strip().split()
    size = int(user_input[1])

    input_permutations = list(sorted(permutations(user_input[0], size)))

    for p in input_permutations:
        print(*p, sep="")


if __name__ == "__main__":
    itertools_permutations_function()
