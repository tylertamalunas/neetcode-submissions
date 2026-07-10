/*
    simple binary search algo
    pivot is middle point
    target lower, check left half + repeat
    target higher, check right half + repeat

*/
class Solution {
    public int search(int[] nums, int target) {
        int s = 0;
        int e = nums.length - 1;

        while (s <= e) {
            int p = s + ((e - s) / 2);
            if (target < nums[p]) {
                e = p - 1;
            } else if (target > nums[p]) {
                s = p + 1;
            } else {
                return p;
            }
        }
        return - 1;
    }
}
