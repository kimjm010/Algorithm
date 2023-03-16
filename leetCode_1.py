# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(0, len(nums)):
            sum = 0
            for j in range(0, i + 1):
                sum += nums[j]
            output.append(sum)
            
        return output