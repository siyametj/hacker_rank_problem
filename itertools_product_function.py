# itertools_product_function.py

from itertools import product

def itertools_product_function():
    list1 = map(int, input().strip().split())
    list2 = map(int, input().strip().split())

    result = list(product(list1, list2))

    print(*result)

if __name__ == "__main__":
    itertools_product_function()
