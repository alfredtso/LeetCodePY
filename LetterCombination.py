from typing import List


class Solution:
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        """
        >>> sol = Solution()
        >>> digits = "252"
        >>> sol.letterCombinations(digits)
        ["a", "b", "c"]
        >>> digits = "23"
        >>> sol.letterCombinations(digits)
        ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        >>> digits = ""
        >>> sol.letterCombinations(digits)
        []
        >>> digits = "2"
        >>> sol.letterCombinations(digits)
        ["a", "b", "c"]

        :param digits:
        :return:
        """
        if digits == "":
            return []

        global combination
        combination = []
        self.backtrack([], 0, digits)
        return combination

    def backtrack(self, path, steps, input):

        if steps == len(input):
            combination.append("".join(path))
            return

        possible_letters = self.construct_candidates(steps, input)
        for letter in possible_letters:
            path.append(letter)
            self.backtrack(path, steps + 1, input)
            path.pop()

    def construct_candidates(self, steps, input):
        return [x for x in self.letters[input[steps]]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
