"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

"""
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        >>> s = Solution()
        >>> strs = ["eat","tea","tan","ate","nat","bat"]
        >>> s.groupAnagrams(strs)
        [["bat"],["nat","tan"],["ate","eat","tea"]]
        >>> strs = ["ddddddddddg","dgggggggggg"]
        >>> s.groupAnagrams(strs)
        [["dgggggggggg"],["ddddddddddg"]]

        :param strs: list of strings
        :return: list of lists of strings
        """

        res = []
        d = collections.defaultdict(list, {})

        # map hash with index
        for i, x in enumerate(strs):

            # no need to hash
            tmp = hash(tuple(sorted(x)))

            # insert the index to mapping
            d[tmp].append(i)


        # build the list with the dictionary
        for k, v in d.items():
            res.append([strs[ans] for ans in v])

        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()