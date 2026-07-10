class NumArray:

    def __init__(self, nums: List[int]):
        self.prifix =[0]
        sum = 0
        for i in nums:
            sum+= i
            self.prifix.append(sum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prifix[right+1]-self.prifix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)