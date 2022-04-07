class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            #pick heaviest two stones
            if stones[-1] == stones[-2]:
                #destroy both
                stones.pop(-1)
                stones.pop(-1)
            else:
                #destroy both and 
                #insert another element with y-x weight at right position
                el = stones.pop(-1) - stones.pop(-1)
                l = len(stones)
                if l == 0:
                    return el
                #if el is less or equal to smallest
                
                if el > stones[-1]:
                    stones.append(el)
                    continue
                for i in range(0,l):
                    if el <= stones[i]:
                        stones.insert(i,el)
                        break
                
                            
        return 0 if len(stones) == 0 else stones[0]
        