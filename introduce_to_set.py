# introduce_to_set.py

def average(array):
    my_set = set(array)

    set_sum = sum(my_set)

    length = len(my_set)

    average = set_sum / length
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
