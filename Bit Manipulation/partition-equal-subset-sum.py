class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i, target):
            if target == 0:
                return True

            if target < 0 or i  >=len(nums):
                return False
            
            state = (i, target)

            if state not in memo:
                memo[state] = dp(i+1, target-nums[i]) or dp(i+1, target)
            
            return memo[state]
        
        return sum(nums) % 2 == 0 and dp(0, sum(nums)//2)

            
            

        