# In this problem, the programmer is supposed to solve the problem using permutations function of the itertools library
# The difficulty of the problem is Medium
# Link to the problem: https://leetcode.com/problems/permutations
# Problem has been accepted

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        us = permutations(nums)
        return list(us)
