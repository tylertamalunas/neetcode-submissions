class Solution {
    public boolean hasDuplicate(int[] nums) {
        // input = int array 
        // output = true if multiple values
        //         false if all values are unique
        // how to get there = make a hash map, set the values in num array to be the key with 0 as the value
        // check if hash map already contains the key, if so return true
        // if i hit no duplicate "key" i set the value to 0
        // add key/value to hash map as i go with getOrDefault((array[val], 0)+1)
        

        HashMap<Integer, Integer> map = new HashMap<>();

        // loop through array and check or add value to hashmap
        for (int i : nums) {
            if (map.containsKey(i)) return true;
            else {

                map.put(i, 0);
            }
        }
        return false;
    }
}
