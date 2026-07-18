# iterable_and_iterators.py

from itertools import combinations

n = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

all_combos = list(combinations(letters, k))

contain_a = sum(1 for combo in all_combos if 'a' in combo)

print(f"{contain_a / len(all_combos):.4f}")
