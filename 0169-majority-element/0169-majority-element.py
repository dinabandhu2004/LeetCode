class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for i in nums:
            if i in seen:
                seen[i] +=1
            else:
                seen[i] =1
        
        
        for key in seen:
            if seen[key] > (len(nums)//2):
                return key
            