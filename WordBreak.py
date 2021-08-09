from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        >>> m = Solution()
        >>> s = "leetcode"
        >>> wordDict = ["leet","code"]
        >>> m.wordBreak(s, wordDict)
        True
        >>> s = "applepenapple"
        >>> wordDict = ["apple","pen"]
        >>> m.wordBreak(s, wordDict)
        True
        >>> s = "catsandog"
        >>> wordDict = ["cats","dog","sand","and","cat"]
        >>> m.wordBreak(s, wordDict)
        False

        :param s:
        :param wordDict:
        :return:
        """

        res = self.helper_wb_bu(s, frozenset(wordDict), 0, {})

        return res

    def helper_wb_bu(self, s: str, wordDict: frozenset, start: int, memo: dict) -> bool:

        # Base case: empty string returns True
        if start == len(s):
            return True

        # Return the value of wb at at start (which include either the whole word case and the char + wb case
        if start in memo.keys():
            return memo[start]

        # for loop
        for i in range(start + 1, len(s) + 1):
            tmp = s[start:i]
            if tmp in wordDict and self.helper_wb_bu(s, wordDict, i, memo):
                memo[start] = True
                return memo[start]

        return False

    def dp(self, s: str, wordDict):
        """
        >>> sol = Solution()
        >>> msg = "leet"
        >>> d = ["le", "et"]
        >>> sol.dp(msg, d)
        True

        :param s:
        :param wordDict:
        :return:
        """
        wordDict_set = set(wordDict)

        # the extra space for 0-length
        dp = [False]* (len(s)+1)
        dp[0] = True

        # the dp problem requires 1D array only; 1. We can repeat words in dict 2. Not required to return items
        # iterate over the length
        for length in range(1, len(s)+1):
            for start in range(length):
                if s[start:length] in wordDict_set and dp[start]:
                    print(s[start:length])
                    dp[length] = True
                    break

        return dp[-1]

if __name__ == '__main__':
    import doctest

    doctest.testmod()
