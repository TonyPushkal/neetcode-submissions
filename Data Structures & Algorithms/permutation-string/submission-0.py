class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1) 
        b = len(s2) 

        for i in range(b-a+1):
            substring = s2[i:i+a]

            if sorted(substring) == sorted(s1):
                return True
        return False