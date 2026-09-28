class Solution {
    public int myAtoi(String s) {

        int i = 0;
        int n = s.length();

        // 1. Remove leading spaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        // If only spaces
        if (i == n) {
            return 0;
        }

        // 2. Check sign
        int sign = 1;

        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        } 
        else if (s.charAt(i) == '+') {
            i++;
        }

        // 3. Convert digits
        int result = 0;

        while (i < n && s.charAt(i) >= '0' && s.charAt(i) <= '9') {

            int digit = s.charAt(i) - '0';

            // 4. Check overflow
            if (result > Integer.MAX_VALUE / 10 ||
                (result == Integer.MAX_VALUE / 10 && digit > 7)) {

                if (sign == 1) {
                    return Integer.MAX_VALUE;
                } else {
                    return Integer.MIN_VALUE;
                }
            }

            result = result * 10 + digit;

            i++;
        }

        return result * sign;
    }
}