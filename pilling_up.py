# pilling_up.py

from collections import deque

for _ in range(int(input().strip())):
    n = int(input())

    blocks = deque(map(int, input().split()))
    last_picked = float('inf')
    possible = "Yes"

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > last_picked:
            possible = "No"
            break

        last_picked = current

    print(possible)
