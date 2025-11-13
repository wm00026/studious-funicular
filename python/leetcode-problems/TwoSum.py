"""
Two Sum - LeetCode Problem #1 (easy)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
    
"""
Explanation:
We want to find the target sum by adding two numbers from the list.
We created a dictionary to store the numbers we have and their indices.
Using the enumerate function, we can then determine the complement of each number (target - num).
If the complement exists in our dictionary, we return the indices of the complement and the current number as a list.
"""