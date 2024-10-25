from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums[:] = sorted(nums)
        return nums