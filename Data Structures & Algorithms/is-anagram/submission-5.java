class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> Scount = new HashMap<>();
        HashMap<Character, Integer> Tcount = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Scount.put(s.charAt(i), Scount.getOrDefault(s.charAt(i), 0) + 1);
            Tcount.put(t.charAt(i), Tcount.getOrDefault(t.charAt(i), 0) + 1);
        }
        if (Scount.equals(Tcount)) return true;
        return false;
    }
}
