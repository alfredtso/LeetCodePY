"""
First approach: Brute force; exceeded limit in LC

>>> sol = Solution()

>>> s = "babad"
>>> sol.longestPalindrome(s)
'bab'
>>> s = "cbbd"
>>> sol.longestPalindrome(s)
'bb'
>>> s = "a"
>>> sol.longestPalindrome(s)
'a'
>>> s = "ac"
>>> sol.longestPalindrome(s)
'a'
>>> ar = array.array("B", [5, 4, 5])
>>> sol.helper(ar)
True
>>> sol.helper_center("aba",1, 1)
3

"""
import array
from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = self.expandAtCenter(s)
        #result = self.bruteforce(s)

        return result

    def expandAtCenter(self, s: str) -> str:

        start = 0
        end = 0

        # find the len of the longeststring
        for i in range(len(s)):
            l1 = self.helper_center(s, i, i)
            l2 = self.helper_center(s, i, i+1)
            length = max(l1, l2)

            # update the start and end ?
            if length > end - start + 1 :
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end+1]



    def helper_center(self, s: str, start: int, end: int) -> int:
        """
        Expand around the centre denoted by the start and end

        :param s: string to be processed
        :param start:
        :param end:
        :return: length of palindromic substring

        >>> my = Solution()
        >>> my.helper_center("aba",1,1)
        3
        >>> my.helper_center("abba",1,2)
        4
        """

        # check boundary and the equal of the first and last char
        # end > or >= 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        # return the length
        # start == end then end - start + 1
        # end == start + 1 then end - start + 1; same
        # end - start + 1 - 2 as the last increment is wrong
        return end - start - 1

    def bruteforce(self, s: str) -> str:

        ls = array.array("B", map(ord, s))
        length = 0
        start = 0

        # base case
        builder = list(s[0])

        # brute force from the back
        for i in range(len(s), -1, -1):
            for j in range(len(s)-i+1):
                # helper to check palindrome substring
                if self.helper(ls[j:j+i]):
                    length= i
                    start = j
                    break

            if length != 0:
                builder = list(s)[start:start+length]
                break

        return ''.join(builder)

    def helper(self, ar: array) -> bool:

        dq = deque(ar)

        for _ in range(len(dq)//2):
            if dq.popleft() != dq.pop():
                return False

        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()