class Solution: 
    def largestAltitude(self, gain: List[int]) -> int:
        x = 0
        max = x
        for i in gain:
            x+=i
            if x > max:
                max=x
        return max