class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        curr_num = last_num = res = 0
        operation = '+'
        for i in range(n):
            char = s[i]
            if char.isdigit():
                curr_num = curr_num * 10 + ord(char) - ord('0')

            if (not char.isdigit() and not char.isspace()) or i == n-1:
                if operation == '+':
                    res += last_num
                    last_num = curr_num
                elif operation == '-':
                    res += last_num
                    last_num = (-1) * curr_num
                elif operation == '*':
                    last_num *= curr_num
                elif operation =='/':
                    last_num = int(last_num/curr_num)

                operation = char
                curr_num = 0
        res += last_num
        return res