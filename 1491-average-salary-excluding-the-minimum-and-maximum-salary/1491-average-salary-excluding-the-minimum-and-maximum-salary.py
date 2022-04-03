class Solution:
    def average(self, salary: List[int]) -> float:
        minval = min(salary)
        maxval = max(salary)
        s = sum(salary)
        l = len(salary)
        return (s - minval - maxval) / (l - 2)