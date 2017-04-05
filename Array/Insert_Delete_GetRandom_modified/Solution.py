import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valtoindex = {}
        self.indextoval = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.valtoindex:
            return False
        else:
            self.indextoval.append(val)
            self.valtoindex[val] = len(self.indextoval) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.valtoindex:
            return False
        else:
            index = self.valtoindex.pop(val)
            self.indextoval[index] = self.indextoval[-1]
            out = self.indextoval[-1]
            if out in self.valtoindex:
                self.valtoindex[out] = index
            self.indextoval.pop()
            return True
 
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.indextoval)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()