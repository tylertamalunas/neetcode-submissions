/*
    simple binary search algo
    pivot is middle point
    target lower, check left half + repeat
    target higher, check right half + repeat

*/
class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int pivot = (end - start) / 2;
        
        while (nums[pivot] != target) {
            if (target == nums[start]) {
                return start;
            } else if (target == nums[end]) {
                return end;
            } else if (target > nums[pivot] && target <= nums[end]) {
                start = pivot + 1;
                pivot = (end - start) * 2;
            } else if (target < nums[pivot] && target >= nums[start]) {
                end = pivot - 1;
                pivot = (end - start) / 2;
            } else {
                return -1;
            }
        }
        return pivot;
    }
}
