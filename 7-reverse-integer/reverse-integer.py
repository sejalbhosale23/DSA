class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow before adding digit
            if rev > INT_MAX // 10:
                return 0

            if rev == INT_MAX // 10 and digit > 7:
                return 0

            rev = rev * 10 + digit

        rev *= sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev