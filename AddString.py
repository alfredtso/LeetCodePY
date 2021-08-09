import itertools


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        >>> sol = Solution()
        >>> s1 = "2465756"
        >>> s2 = "876554"
        >>> s = str(int(s1) + int(s2))
        >>> sol.addStrings(s1, s2) == s
        True
        >>> s1 = "9"
        >>> s2 = "99"
        >>> s = str(int(s1) + int(s2))
        >>> sol.addStrings(s1, s2) == s
        True
        """
        builder = []
        c = 0

        for i, j in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            i_int = int(i)
            j_int = int(j)
            c, v = divmod(i_int + j_int + c, 10)
            builder.append(v)

        # handle last carry
        if c:
            builder.append(c)

        return "".join(map(str, builder[::-1]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
