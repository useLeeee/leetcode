import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indextovalue = {}
        self.valuetoindex = {}
        self.insertindex = [0]

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False
        self.indextovalue[self.insertindex[-1]] = val
        if len(self.insertindex) > 1:
            insert = self.insertindex.pop()
        else:
            insert = self.insertindex[0]
            self.insertindex[0] += 1
        if val in self.valuetoindex:
            self.valuetoindex[val].append(insert)
            ret = False
        else:
            self.valuetoindex[val] = [insert]
            ret = True
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.valuetoindex:
            return False
        elif len(self.valuetoindex[val]) == 1:
            deleteindex = self.valuetoindex.pop(val)[0]
        else:
            deleteindex = self.valuetoindex[val].pop()
        self.indextovalue.pop(deleteindex)
        self.insertindex.append(deleteindex)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randint(0, len(self.indextovalue)-1)
        self.insertindex[1:] = sorted(self.insertindex[1:])
        for i in range(1, len(self.insertindex)):
            if index >= self.insertindex[i]:
                index += 1
        return self.indextovalue[index]

# Your RandomizedCollection object will be instantiated and called as such:

