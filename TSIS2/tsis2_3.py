class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    x+=1
        return x
        