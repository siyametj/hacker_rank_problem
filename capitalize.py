# capitalize.py

# Complete the solve function below.
def solve(s):
    word_list = s.split(" ")
    new_list = []

    for w in word_list:
        if w == "":
            new_list.append(w)
        else:
            new_list.append(w.capitalize())

    return " ".join(new_list)

if __name__ == '__main__':
    print(solve("chris alan"))
