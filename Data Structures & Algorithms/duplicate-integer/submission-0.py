class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        original_len = len(nums)

        if len(set(nums)) < original_len:
            return True

        return False
        