# maximize_it.py

from itertools import product

if __name__ == "__main__":
    K, M = map(int, input().strip().split())

    lists = []

    for _ in range(K):
        row = list(map(int, input().strip().split()))[1:]
        lists.append(row)

    max_value = 0

    for combination in product(*lists):
        current_sum = sum(x ** 2 for x in combination) % M

        if current_sum > max_value:
            max_value = current_sum

    print(max_value)
