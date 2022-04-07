class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #from solutions
        stones.sort()
        while len(stones) > 1:
            s1 = stones.pop(-1)
            s2 = stones.pop(-1)
            
            if s1 > s2:
                #insert s1-s2 at right pos
                for i in range(0,len(stones)+1):
                    if i == len(stones) or s1-s2 <= stones[i]:
                        stones.insert(i,s1-s2)
                        break
            #else
            #destroy both
            
        return 0 if len(stones) == 0 else stones[0]
        