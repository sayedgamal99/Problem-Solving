class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        answer = 1
        endpoint = points[0][1]
        for ball in points[1:]:
            if ball[0] > endpoint:
                answer += 1
                endpoint = ball[1]
            else:
                endpoint = min(endpoint, ball[1])
        return answer
