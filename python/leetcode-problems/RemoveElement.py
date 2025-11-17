"""
LeetCode Problem: Remove Element (easy)
"""

from typing import List

"""
First, a pointer is created.
Then, we iterate through the list. For each val in nums in place, we remove nums not equal to val.
Pointer is incremented each time a non-val is found.
Finally, we return the pointer as the new length of the modified list.
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

# Example test cases
print(Solution().removeElement([3,2,2,3], 3))  # 2
