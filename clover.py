resources_map = {"3": [4], "4": [5, 6, 7], "6": [-1, 410]}

def fetch(id):

    result = []
    not_ava_ls = []
    result.append(id)

    def helper(id):
        try:
            tmp = resources_map[str(id)]
        except KeyError:
            return

        for i, x in enumerate(tmp):
            if x == -1:
                not_ava_ls.append(tmp[i+1])
                break
            else:
                result.append(x)
                helper(x)

    helper(id)
    print(result)
    print(not_ava_ls)
    return 0


if __name__ == '__main__':
    fetch(3)