class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        complement = {}

        for i in range(n):
            if numbers[i] in complement:
                return [complement[numbers[i]] + 1, i + 1]
            else:
                complement[target - numbers[i]] = i