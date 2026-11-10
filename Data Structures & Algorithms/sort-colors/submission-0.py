class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for j in range(len(nums)-1):
            for i in range(len(nums)-j-1):
                temp = 0
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
        return nums
        