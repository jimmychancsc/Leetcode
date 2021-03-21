class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles:
            return False
        x1 = y1 = 2 ** 31 - 1
        x2 = y2 = -2 ** 31

        bag = set()
        area = 0

        for rectangle in rectangles:
            x1 = min(x1, rectangle[0])
            y1 = min(y1, rectangle[1])
            x2 = max(x2, rectangle[2])
            y2 = max(y2, rectangle[3])

            area += (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])

            s1 = f"{rectangle[0]} {rectangle[1]}"
            s2 = f"{rectangle[0]} {rectangle[3]}"
            s3 = f"{rectangle[2]} {rectangle[3]}"
            s4 = f"{rectangle[2]} {rectangle[1]}"

            bag.remove(s1) if s1 in bag else bag.add(s1)
            bag.remove(s2) if s2 in bag else bag.add(s2)
            bag.remove(s3) if s3 in bag else bag.add(s3)
            bag.remove(s4) if s4 in bag else bag.add(s4)

        if f"{x1} {y1}" not in bag or f"{x1} {y2}" not in bag or f"{x2} {y1}" not in bag or f"{x2} {y2}" not in bag or len(
                bag) != 4:
            return False

        return area == (x2 - x1) * (y2 - y1)