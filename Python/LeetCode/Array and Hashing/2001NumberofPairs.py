class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        themap = {}
        for rectangle in rectangles:
            ratio = rectangle[0]/rectangle[1]
            themap[ratio]= themap.get(ratio,0)+1
        result = 0
        for key,value in zip(themap.keys(),themap.values()):
            result+=((value)*(value-1)//2)
        return result
    

rectangles = [[4,8],[3,6],[10,20],[15,30],[1,7]]
print(Solution().interchangeableRectangles(rectangles=rectangles))