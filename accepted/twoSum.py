# https://leetcode.com/problems/two-sum/
# 19/19 test cases passed
# runtime: 72ms
# language: python 3

class Solution:
    def twoSum(self, nums, target):
        lut_num_to_idx = {}
        for i, v in enumerate(nums):
            desired = target - v
            if desired in lut_num_to_idx:
                return [lut_num_to_idx[desired], i]

            lut_num_to_idx[v] = i

c = Solution()
assert c.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert c.twoSum([3, 2, 4], 6) == [1, 2]

print("Everything passed!")