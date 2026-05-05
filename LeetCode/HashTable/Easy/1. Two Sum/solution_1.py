from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = defaultdict(lambda: None)
        for idx, num1 in enumerate(nums):
            old_idx = dict_nums[num1]
            if dict_nums[num1] == None:
                dict_nums[num1] = idx
            else:
                dict_nums[num1] += idx
            num2 = target - num1
            if num1 == num2 and old_idx != None:
                return [old_idx, idx]
            if num1 != num2 and dict_nums[num2] != None:
                other_idx = dict_nums[num2]
                return [other_idx, idx]