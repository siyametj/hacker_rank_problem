# word_order.py

from collections import Counter

n = int(input())
word = [input().strip() for _ in range(n)]

word_counts = Counter(word)

print(len(word_counts))
print(*(word_counts.values()))

