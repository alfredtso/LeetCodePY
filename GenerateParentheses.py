from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        """
        >>> sol = Solution()
        >>> n = 1
        >>> sol.generateParenthesis(n)
        ["()"]
        >>> n = 3
        >>> sol.generateParenthesis(n)
        ["((()))","(()())","(())()","()(())","()()()"]


        :param n:
        :return:
        """
        if n == 0:
            return []

        global combination
        combination = []
        self.backtrack([], 0, n)
        return combination

    def backtrack(self, path, index, input):
        if index == input * 2:
            combination.append("".join(path))
            return

        candidates = self.construct_candidates(path, index, input)
        for can in candidates:
            path.append(can)
            self.backtrack(path, index+1, input)
            path.pop()

    def construct_candidates(self, path, index, input):

        can = []
        stack = []

        for x in path:
            if x == "(":
                stack.append(x)
            elif x == ")":
                stack.pop() if stack else ...

        if stack:
            can.append(")")

        if path.count("(") < input:
            can.append("(")

        return can

if __name__ == "__main__":
    import doctest

    doctest.testmod()



