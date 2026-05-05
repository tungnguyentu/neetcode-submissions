class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set()
        for i in nums:
            if i in dedup:
                return True
            dedup.add(i)
        return False