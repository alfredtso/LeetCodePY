import copy

def anagram(s):
    # IMPOSSIBLE case: any one character have number more than half ?
    length = len(s)
    char_set = set(s)
    for c in char_set:
        if s.count(c) > length / 2:
            print("IMPOSSIBLE")
            return

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
        print("".join(resultpath))
    else:
        print("IMPOSSIBLE")


def construct_candidates(ava_set, k, s):
    candidates = []
    for c in ava_set:
        if s[k] != c:
            candidates.append(c)

    return candidates

if __name__ == '__main__':

    with open('anagram_test.txt') as f:
        k = int(f.readline())
        print(f'Number of lines: {k}')
        i = 0
        line = f.readline().rstrip('\n')
        while line:
            anagram(line)
            line = f.readline().rstrip('\n')
            i += 1


