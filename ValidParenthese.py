from typing import List


class Solution:
    def isValid(self, s: str) -> bool:

        map = {")": "(", "}": "{", "]": "["}
        stack = list()

        for x in s:

            if x in map:

                # pop if stack is not empty
                tmp = stack.pop() if stack else ...

                # check if matching
                if map[x] != tmp:
                    return False

            else:

                stack.append(x)

        # if stack if not empty return False
        return not bool(stack)

    def test(self):
        assert self.isValid("()") == True
        assert self.isValid("()]") == False
        assert self.isValid("((") == False
        assert self.isValid("{[]}") == True
        assert self.isValid("{([)]}") == False

if __name__ == '__main__':
    my = Solution()
    my.test()
