class Solution {
    public boolean isPalindrome(String s) {
        // 2 pointer start at both ends
        // strip and lower string
        // isLetterOrDigit() method

        s.strip();
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) {
                l++;
            }
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) {
                r--;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            else {
                l++;
                r--;
            }
        }
        return true;
    }
}
