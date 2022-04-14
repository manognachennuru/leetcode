class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum_of_n = [0]*len(nums)
        sm = 0
        for i,num in enumerate(nums):
            sm += num
            self.sum_of_n[i] = sm
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_of_n[right]
        return self.sum_of_n[right] - self.sum_of_n[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)