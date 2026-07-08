# symmetric_diffrence.py

def solve():
    _ = input()
    m_set = set(map(int, input().split()))

    _ = input()
    n_set = set(map(int, input().split()))

    diffrence = m_set.symmetric_difference(n_set)

    for number in sorted(diffrence):
        print(number)

if __name__ == "__main__":
    solve()
