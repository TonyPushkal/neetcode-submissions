class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count ={}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        n = len(nums)
        output =[]

        for num in count:
            if count[num] > n/3:
                output.append(num)

        return output