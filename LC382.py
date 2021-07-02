class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        pick = int(random.random() * len(self.range))
        return self.range[pick]