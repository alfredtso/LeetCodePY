import copy
import sys


def anagram(s, i):
    # output either one anagram or IMPOSSIBLE
    ava_set = list(s)
    finished = False
    resultpath = []

    def backtracking(path, ava_set, k, s):

        nonlocal finished
        nonlocal resultpath

        # solution: one of the anagram
        if len(path) == len(s):
            finished = True
            resultpath = copy.deepcopy(path)
            return

        else:
            candidates = construct_candidates(ava_set, k, s)

            for can in candidates:
                ava_set.remove(can)
                path.append(can)
                backtracking(path, ava_set, k + 1, s)
                path.pop()
                ava_set.append(can)
                if finished:
                    return

    backtracking([], ava_set, 0, s)
    if finished:
        print(f'Case #{i+1}: {"".join(resultpath)}')
    else:
        print(f'Case #{i+1}: IMPOSSIBLE')


def construct_candidates(ava_set, k, s):
    candidates = []
    for c in ava_set:
        if s[k] != c:
            candidates.append(c)

    return candidates

if __name__ == '__main__':
    k = int(sys.stdin.readline())
    for _ in range(k):
        line = sys.stdin.readline().rstrip('\n')
        anagram(line, _)