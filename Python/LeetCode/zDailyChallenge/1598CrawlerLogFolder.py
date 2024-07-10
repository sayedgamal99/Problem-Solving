class Solution:
    def minOperations(self, logs: list[str]) -> int:
        operations = 0
        for l in logs:
            if l == '../':
                operations = (operations-1) if operations > 0 else 0
            elif l == './':
                continue
            else:
                operations += 1
        return operations


print(Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))
