class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        sequence = [2, 3]
        i = 1
        while i + 2 < n:
            sequence.append(sequence[i - 1] + sequence[i])
            i += 1

        return sequence[-1]
