class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        high, low = len(people)-1, 0
        boats = 0
        while high >= low:
            if (people[high]+people[low]) <= limit:
                low += 1
            high -= 1
            boats += 1
        return boats
