class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        ori = 0
        i = 1
        while i < len(prices):
            if prices[i] < prices[i+1]:
                ori = ori
                i = i + 1
            else:
                profit = profit + prices[i+1]-prices[i]
                ori = i + 2
                i = i + 3
        return profit


s1 = Solution()
print(s1.maxProfit([1,5]))
