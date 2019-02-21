class Solution:
    def maxProfit(self, prices):

        n = len(prices)

        if n < 2:
            return 0

        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]

        minval = prices[0]
        maxval = prices[-1]

        #前向   
        for i in range(1,n):
            dp1[i] = max(dp1[i-1], prices[i] - minval)
            minval = min(minval, prices[i])

        #后向    
        for i in range(n-2,-1,-1):
            dp2[i] = max(dp2[i+1], maxval - prices[i])
            maxval = max(maxval, prices[i])
        
        dp = [dp1[i] + dp2[i] for i in range(n)]

        return max(dp)

if __name__ == "__main__":

    prices = [3,3,5,0,0,3,1,4]

    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)