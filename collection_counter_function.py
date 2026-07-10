# collection_counter_function.py

from collections import Counter

if __name__ == "__main__":
    number_of_shoes = int(input().strip())
    shoes_size = map(int, input().strip().split())
    shoe_inventory = Counter(shoes_size)

    number_of_customer = int(input().strip())

    total_earn = 0

    for _ in range(number_of_customer):
        size, price = map(int, input().strip().split())

        if shoe_inventory[size] > 0:
            total_earn += price
            shoe_inventory[size] -= 1

    print(total_earn)
