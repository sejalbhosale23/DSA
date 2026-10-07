import java.util.*;

class Solution {

    public List<String> removeInvalidParentheses(String s) {

        List<String> result = new ArrayList<>();

        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(s);
        visited.add(s);

        boolean found = false;

        while (!queue.isEmpty()) {

            String current = queue.poll();

            // Check if current string is valid
            if (isValid(current)) {
                result.add(current);
                found = true;
            }

            // If valid strings are found,
            // don't remove more characters
            if (found) {
                continue;
            }

            // Remove one character at a time
            for (int i = 0; i < current.length(); i++) {

                // Only remove parentheses
                if (current.charAt(i) != '(' &&
                    current.charAt(i) != ')') {
                    continue;
                }

                String newString =
                    current.substring(0, i) +
                    current.substring(i + 1);

                // Avoid duplicates
                if (!visited.contains(newString)) {
                    visited.add(newString);
                    queue.add(newString);
                }
            }
        }

        return result;
    }

    // Check whether parentheses are valid
    private boolean isValid(String s) {

        int count = 0;

        for (char ch : s.toCharArray()) {

            if (ch == '(') {
                count++;
            }
            else if (ch == ')') {
                count--;

                // More closing brackets than opening
                if (count < 0) {
                    return false;
                }
            }
        }

        return count == 0;
    }
}