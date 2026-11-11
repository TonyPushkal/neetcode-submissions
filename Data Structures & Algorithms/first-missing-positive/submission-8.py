class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        answer = 1

        for num in nums:
            if num == answer:
                answer += 1

        return answer