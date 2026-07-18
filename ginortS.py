# ginortS.py

s = input().strip()

print("".join(sorted(s, key=lambda c: (c.isdigit() and int(c) % 2 == 0, c.isdigit(), c.isupper(), c))))
