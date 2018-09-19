class HashSet(object):

    def __init__(self):
        self.set= set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.set:
            self.set.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.set


if __name__ == "__main__":
    hashset = HashSet()  # void
    hashset.add(3)  # void
    print(hashset.contains(3))  # True
    hashset.remove(3)  # void
    print(hashset.contains(3))  # False
