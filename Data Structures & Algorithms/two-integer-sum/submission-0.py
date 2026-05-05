class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], index]
            mapping[num] = index

