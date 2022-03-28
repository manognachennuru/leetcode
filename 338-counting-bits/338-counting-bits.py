class Solution:
    def countBits(self, n: int) -> List[int]:
        '''0 - 0
        1 - 1
        2 - 10
        3 - 11
        4 - 100
        5 - 101
        6 - 110
        7 - 111
        8 - 1000
        9 - 10001 '''
    
        return [bin(i).count('1') for i in range(0,n+1)]

        