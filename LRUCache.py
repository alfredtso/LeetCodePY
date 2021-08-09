from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keys():
            return -1

        # get op cause it to move to the top of cache
        self.move_to_end(key=key)
        return self[key]

    def put(self, key: int, value: int) -> None:

        # put op cause it to move to top
        # case 1: key not inside already
        if key not in self.keys():
            self.move_to_end(key=key)

        # put value
        self[key]= value

        # if capacity reached
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)