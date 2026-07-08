# alphabet_rangoli.py

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    width = 4 * size - 3

    lines = []

    for i in range(size):
        s = alphabet[i:size]
        row_char = s[::-1] + s[1:]

        row_string = "-".join(row_char).center(width, "-")
        lines.append(row_string)

    rangoli = lines[::-1] + lines[1:]
    print("\n".join(rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
