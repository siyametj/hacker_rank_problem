# compress_the_string.py

from itertools import groupby

s = input().strip()

print(*(f"({len(list(group))}, {int(key)})" for key, group in groupby(s)))
