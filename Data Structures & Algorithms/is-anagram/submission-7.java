class Solution {
    public boolean isAnagram(String s, String t) {
        // can sort and see if they are equal, nlogn & 1

        char[] sortS = s.toCharArray();
        char[] sortT = t.toCharArray();
        Arrays.sort(sortS);
        Arrays.sort(sortT);

        return Arrays.equals(sortS, sortT);

        // use array to count letters and see if arrays are equal n & 1
    }
}
