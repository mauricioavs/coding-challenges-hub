class Solution:
    def twoSum(self, nums: List[float], target: int) -> List[float]:
        d={}
        for i in range(len(nums)):
            key=target-nums[i]
            if key in d:
                return (d[key],i)
            else:
                d[nums[i]]=i 