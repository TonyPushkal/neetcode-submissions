class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        def check(left,right):
            while left < right:
                if s[right] != s[left]:
                    return False
                left += 1
                right -=1
            return True
        
        while left < right:
            if s[right] != s[left]:
                return check(left,right-1) or check(left+1,right)
            left += 1
            right -= 1

        return True 