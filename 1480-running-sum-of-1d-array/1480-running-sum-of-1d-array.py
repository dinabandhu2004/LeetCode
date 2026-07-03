class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr =[]
        p_sum = 0

        for i in range(len(nums)):
            p_sum += nums[i]
            sum_arr.append(p_sum)
        return sum_arr