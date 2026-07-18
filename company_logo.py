# company_logo.py

from collections import Counter

s = sorted(input().strip())

word_counts = Counter(s).most_common(3)

for char, count in word_counts:
    print(char, count)
