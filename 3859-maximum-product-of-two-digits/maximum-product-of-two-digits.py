class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(d) for d in str(n)]
        max_product = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                max_product = max(max_product, digits[i] * digits[j])

        return max_product