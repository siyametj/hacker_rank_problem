# find_the_runner_up_score.py

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, set(input().split())))

    first_max_val = max(arr)
    arr.remove(first_max_val)

    print(max(arr))


