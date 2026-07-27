class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        first = nums[-1]
        second = nums[-2]

        ans = (first - 1) * (second - 1)

        return ans