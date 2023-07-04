class Solution {
    public int jump(int[] nums) {
        int end = 0, reachable = 0, count = 0;
        for (int i = 0; i < nums.length-1; i++) {
            reachable = Math.max(reachable, i + nums[i]);
            if (i == end) {
                count += 1;
                end = reachable;
            }
        }
        return count;
    }
}