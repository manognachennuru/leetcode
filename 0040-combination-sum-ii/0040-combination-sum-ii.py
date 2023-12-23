class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        candidates.sort()
        
        def helper(i, curSum, curComb):
            #print(i, curSum, curComb)
            if target == curSum:
                combs.append(curComb.copy())
                #print("yay found one",curComb, combs)
                return
            
            elif i >= len(candidates) or curSum > target:
                return 
            
            #continue to check
            #choose current number
            helper(i + 1, curSum + candidates[i], curComb + [candidates[i]])
            
            #don't choose current number
            curNum = candidates[i]
            while candidates[i] == curNum: 
                i += 1
                if i == len(candidates):
                    return
            
            helper(i, curSum, curComb)
            
        helper(0, 0, [])
        return combs