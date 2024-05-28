class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = 0
        max_len = 0
        left = 0

        for right in range(n):
            cost += abs(ord(s[right]) - ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


def run_tests():
    tests = [
        {"s": "abcd", "t": "bcdf", "maxCost": 3, "expected": 3},
        {"s": "abcd", "t": "cdef", "maxCost": 3, "expected": 1},
        {"s": "abcd", "t": "acde", "maxCost": 0, "expected": 1},
    ]

    for i, test in enumerate(tests):
        result = Solution().equalSubstring(
            test["s"], test["t"], test["maxCost"])
        if result != test["expected"]:
            print(f"Test {i + 1} failed:")
            print(
                f"  Input: s={test['s']}, t={test['t']}, maxCost={test['maxCost']}")
            print(f"  Expected: {test['expected']}, but got: {result}")

    print('all tests passed!')


run_tests()
