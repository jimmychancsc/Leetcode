class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        prev = None
        for c in preorder:
            if c == ",":
                slots -= 1

                if slots < 0:
                    return False

                if prev != "#":
                    slots += 2
            prev = c

        slots = slots + 1 if c != "#" else slots - 1
        return slots == 0