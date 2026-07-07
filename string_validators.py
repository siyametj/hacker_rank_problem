# string_validators.py

def string_validators(string):

    # if alphanumeric characters
    print(any(char.isalnum() for char in string))

    # if alphabetical characters
    print(any(char.isalpha() for char in string))

    # if digits
    print(any(char.isdigit() for char in string))

    # if lowercase characters
    print(any(char.islower() for char in string))

    # if uppercase characters
    print(any(char.isupper() for char in string))


if __name__ == '__main__':
    s = input()
    string_validators(s)

