class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for j in range(n - 1):
            for i in range(n - j - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
        return nums