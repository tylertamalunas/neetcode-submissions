class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // words with same letters grouped together
        // likely hashmap. Key=letter count array int[]     Value=List<strings>
        // return values of the map
        
        // create map
        HashMap<String, ArrayList<String>> map = new HashMap<>();

        // loop through input array
        for (String word : strs) {
            int[] count = new int[26];
        // loop through string letters
            for (int i=0; i < word.length(); i++) {
                // calculate charAt[i] - 'a' ++
                count[word.charAt(i) - 'a']++;
            }
            // convert array to string
            String key = Arrays.toString(count);
            // check if key exists, if so get AL and add word to it
            if (map.containsKey(key)) {
                ArrayList<String> AL = map.get(key);
                map.get(key).add(word);
            // if not, add key and initialize an AL
            } else {
                ArrayList<String> AL = new ArrayList<>();
                    AL.add(word);
                map.put(key, AL);
            }
        }
        return new ArrayList<>(map.values());
    }
}
