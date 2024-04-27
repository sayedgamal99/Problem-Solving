from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        best_steps = {}

        def countSteps(curr, next):
            stepsBetween = abs(curr-next)
            stepsAround = abs(len(ring)-stepsBetween)
            return min(stepsAround, stepsBetween)

        def tryLock(ring_index, key_index):
            if (ring_index, key_index) in best_steps:
                return best_steps[(ring_index, key_index)]

            if key_index == len(key):
                best_steps[(ring_index, key_index)] = 0
                return 0

            minSteps = float('inf')
            for i in range(len(ring)):
                if ring[i] == key[key_index]:
                    total_steps = countSteps(ring_index, i)+1 +\
                        tryLock(i, key_index+1)
                    minSteps = min(minSteps, total_steps)
            best_steps[(ring_index, key_index)] = minSteps
            return minSteps
        return tryLock(0, 0)


# Greedy Solution (not accepted)
class Solution1:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R, n = defaultdict(list), len(ring)
        for i in range(n):
            R[ring[i]].append(i)

        answer = 0
        current_idx = 0
        min_index = 0
        for idx, k in enumerate(key):
            answer += 1
            path = 300
            for v in R[k]:
                m = min(abs(v-current_idx), abs(n-(v-current_idx)))
                if m <= path:
                    path = m
                    min_index = v
            current_idx = min_index

            answer += path
            # print(path)
        return answer


# print(Solution().findRotateSteps(ring="godding", key="gd"))
# print(Solution().findRotateSteps(ring="godding", key="godding"))

# print(Solution().findRotateSteps("abcde", 'ade'))
