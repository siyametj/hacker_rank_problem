# mutate_string.py

def mutate_string(string, position, character):
    first = string[:position]
    last = string[position + 1:]
    return first + character + last

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
