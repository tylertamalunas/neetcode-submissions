class Solution {
    public int[] twoSum(int[] nums, int target) {
        // hash map, itterate one pass
        // if target-value is not in map, add current in, otherwise return current and target

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
