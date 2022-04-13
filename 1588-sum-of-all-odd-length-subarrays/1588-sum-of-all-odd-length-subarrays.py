class Solution:
    #brute force - using prefix sum to find sumNLengthSubarrays
    def sumNLengthSubarrays(self,arr,n):
        total = sm = sum(arr[0:n])
        for i in range(1,len(arr)-n+1):
            sm -= arr[i-1]
            sm += arr[i+n-1]
            total += sm
        return total
        
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for n in range(1,len(arr)+1,2):
            result += self.sumNLengthSubarrays(arr,n)
        return result