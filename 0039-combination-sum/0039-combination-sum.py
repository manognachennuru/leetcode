class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        i = 0
        combs = []
        curSum = 0
        
        def helper(curComb, curSum, i):
            #print(curComb, curSum, i)
            
            if i == len(candidates):
                return
            
            if curSum == target:
                combs.append(curComb)
                return
            
            if curSum > target:
                return
            
            #choose 2
            helper(curComb + [candidates[i]], curSum + candidates[i], i)
            
            #not choose 2
            helper(curComb, curSum, i + 1)
            
            return
                
        helper([], curSum, i)
        return combs
                
            