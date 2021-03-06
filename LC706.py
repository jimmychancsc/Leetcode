class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic[key] = value
        else:
            self.dic[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            return self.dic[key]
        else:
            return -1
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.dic:
            del self.dic[key]