# merge_the_tools.py

def merge_the_tools(string, k):
    # Total size of string
    length = len(string)

    for i in range(0, length, k):
        sub_string = string[i: i + k]

        unique_characters = []

        for char in sub_string:
            if char not in unique_characters:
                unique_characters.append(char)

        print("".join(unique_characters))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
