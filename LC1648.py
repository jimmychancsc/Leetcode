class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        arr = sorted(Counter(inventory).items(), reverse=True) + [(0, 0)]
        ans, ind, width = 0, 0, 0

        while orders > 0:
            width += arr[ind][1]
            sell = min(orders, width * (arr[ind][0] - arr[ind + 1][0]))
            whole, remainder = divmod(sell, width)
            ans += width * (whole * (arr[ind][0] + arr[ind][0] - (whole - 1))) // 2 + remainder * (arr[ind][0] - whole)
            orders -= sell
            ind += 1
        return ans % 1_000_000_007