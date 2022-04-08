class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        from collections import deque
        stk = deque()
        res = [0]*len(t)
        
        for curr_day, curr_temp in enumerate(t):
            while len(stk) and t[stk[-1]] < curr_temp:
                prev_day = stk.pop()
                res[prev_day] = curr_day - prev_day
            stk.append(curr_day)
            
        return res
            