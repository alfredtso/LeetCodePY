def miniumBribes(q):
    # maintain a
    return 0

if __name__ == '__main__':
    with open("bribe.txt") as f:
        t = int(f.readline().strip())
        print(t)

        for _ in range(t):
            n = int(f.readline().strip())
            print(n)

            q = list(map(int, f.readline().rstrip().split()))
            print(q)
