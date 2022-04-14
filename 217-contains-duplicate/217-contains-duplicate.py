class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #multiple ways to solve
        #using a dic
        #using  set
        #if the array only has values from 1 to n \
        #then you can edit vallue at that index without using extra space"
        
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
            
        return False