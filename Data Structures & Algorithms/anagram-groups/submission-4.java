class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // hashmap to gather 'like' words. key is array counter, key is list of words Map<int[], ArrayList<> or List?>
        HashMap<String, List<String>> map = new HashMap<>();
        ArrayList<String> words = new ArrayList<>();

        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
