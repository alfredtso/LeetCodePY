"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

>>> r = RandomizedSet()
>>> r.insert(1)
True
>>> r.remove(2)
False
>>> r.insert(2)
True
>>> r.getRandom()
1 or 2
>>> r.remove(1)
True
>>> r.insert(2)
False

"""
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._index = []
        self._map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val not in self._index:
            self._index.append(val)
            self._map[val] = len(self._index) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val in self._map:
            # all constant time ops
            last_elm, idx = self._index[-1], self._map[val]

            # swap the last to index of val and update the index of last elm
            self._index[idx], self._map[last_elm] = last_elm, idx

            # delete the duplicated last element
            self._index.pop()
            del self._map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._index)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
