class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        count = Counter(s)

        first_half = ""
        middle = ""

        # Process characters in sorted order
        for ch in sorted(count.keys()):
            first_half += ch * (count[ch] // 2)

            # If a character has an odd count, it goes in the middle
            if count[ch] % 2 == 1:
                middle = ch

        # Second half is the reverse of the first half
        second_half = first_half[::-1]

        return first_half + middle + second_half