# weired_or_not.py

def weired_or_not(n):
    # If n is ODD it mean weired
    if n % 2 != 0:
        print("Weird")

    # If n is even and stay between 2 to 5 print Not Weird
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")

    # If n is even and stay between 6 to 20 Weird
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")

    # If n is even and greater than 20
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

if __name__ == "__main__":
    n = int(input().strip())
    weired_or_not(n=n)
