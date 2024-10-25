from typing import List
from collections import Counter

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        output = freq.most_common()[-1]
        return output[0]