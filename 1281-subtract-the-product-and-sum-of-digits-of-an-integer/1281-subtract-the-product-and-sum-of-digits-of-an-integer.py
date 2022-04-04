class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #trying one-liner 
        A = list(map(int,str(n)))
        return reduce(operator.mul, A) - reduce(operator.add, A)