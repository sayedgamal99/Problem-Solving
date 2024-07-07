class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles

        while numBottles // numExchange:
            totalBottles += numBottles // numExchange
            numBottles = (numBottles // numExchange) + \
                (numBottles % numExchange)

        return totalBottles
