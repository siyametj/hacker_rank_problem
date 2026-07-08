# set_add_function.py

def solve():
    total_input = int(input().strip())
    unique_set = set()

    for i in range(total_input):
        new = input()
        unique_set.add(new)

    print(len(unique_set))

if __name__ == "__main__":
    solve()
