class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit, price_buy, price_sell = 0, prices[0], prices[0]

        for i, price_today in enumerate(prices[1:]):

            today = i + 1

            if price_today >= price_sell:
                price_sell = price_today
                profit = max(profit, price_sell - price_buy)
            
            elif price_today < price_buy:
                # 找到买价最低一天
                price_buy = price_today
                # 买入要在卖出之前
                price_sell = price_buy
                print(today, price_buy, price_sell)

        return profit
        

if __name__ == "__main__":

    prices = [7,1,5,3,6,4]
    # prices = [2,2] # 
    # prices = [7,1] # 不能为-6
    prices = [3,7,1,2]

    soulution = Solution()
    result = soulution.maxProfit(prices)
    print(result)