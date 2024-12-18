from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            price = prices[i]
            while stack and price <= prices[stack[-1]]:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices
