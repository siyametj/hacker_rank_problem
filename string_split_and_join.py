# string_split_and_join.py

def split_and_join(line):
    spliting = line.split()
    return "-".join(spliting)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
