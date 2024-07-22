class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        all = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        sorted_names, sorted_heights = zip(*all)
        return list(sorted_names)
