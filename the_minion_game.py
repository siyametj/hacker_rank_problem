# the_minion_game.py

def minion_game(string):
    kevin = 0 # Player of vowel
    stuart = 0 # Player of consonent
    length = len(string) # Total length of input string

    for i in range(length):
        if string[i] in "AEIOU":
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
