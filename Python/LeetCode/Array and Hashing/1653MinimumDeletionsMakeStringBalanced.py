class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        min_deletions = a_count
        b_count = 0

        for char in s:
            if char == 'b':
                b_count += 1
            else:
                a_count -= 1

            min_deletions = min(min_deletions, a_count + b_count)

        return min_deletions
