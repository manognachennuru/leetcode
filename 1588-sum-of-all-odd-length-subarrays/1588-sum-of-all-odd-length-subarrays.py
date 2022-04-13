class Solution:
    #brute force
    def sumNLengthSubarrays(self,arr,n):
        sm = 0
        for i in range(0,len(arr)-n+1):
            sm += sum(arr[i:i+n])
        return sm
        
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for n in range(1,len(arr)+1,2):
            result += self.sumNLengthSubarrays(arr,n)
        return result