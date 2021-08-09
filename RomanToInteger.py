class Solution:
    def romanToInt(selfself, s: str) -> int:
        translation = {"I": 1, "V": 5, "X": 10, "L": 50,
                       "C": 100, "D": 500, "M": 1000}
        # case 1: if the symbol to the left is greater, the result is left - right, then skip the left
        # case 2: if the symbol to the left is less than or equal, the result is adding the current
        val = 0

        # skip for taking the left on in case 1
        skip = 0
        for i, x in enumerate(s):
            if skip:
                skip = 0
                continue
            # Condition: end of string, check case 1 and check skip
            elif i+1 < len(s) and translation[x] < translation[s[i+1]] and ~skip:
                val += translation[s[i+1]] - translation[x]
                skip = 1
            # Case 2
            else:
                val += translation[x]
        return val



    def test(self):
        assert self.romanToInt("III") == 3
        assert self.romanToInt("IV") == 4
        assert self.romanToInt("IX") == 9
        assert self.romanToInt("LVIII") == 58
        assert self.romanToInt("MCMXCIV") == 1994


if __name__ == '__main__':
    my = Solution()
    my.test()
