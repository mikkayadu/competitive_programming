class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i< len(nums):
            if nums[i]  <= len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i+=1
        
        ans = []

        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
        