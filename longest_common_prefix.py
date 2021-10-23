import random
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = []
        length = len(strs)
        strs.sort()

        if length == 1:
            return strs[0]

        first_word = strs[0]
        last_word = strs[-1]

        if first_word == "":
            return ""

        for i in range(len(first_word)):
            if first_word[i] == last_word[i]:
                result.append(first_word[i])
            else:
                break

        return ''.join(result)
