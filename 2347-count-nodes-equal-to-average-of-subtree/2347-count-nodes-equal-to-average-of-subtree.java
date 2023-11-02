/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int averageOfSubtree(TreeNode root) {
        int ans[] = new int[1];
        solve(root, ans);
        return ans[0];
    }

    int[] solve(TreeNode root, int []ans) {
        if(root == null) return new int[]{0, 0};

        int[] left = solve(root.left, ans); // 0 position has sum 1 position has total nodes
        int[] right = solve(root.right, ans); // 0 position has sum 1 position has total nodes

        int total = 1 + left[1] + right[1];

        int avg = (root.val + left[0] + right[0]) / total;
        if(avg == root.val) ans[0]++;

        return new int[] {root.val + left[0] + right[0], total};
        
    }
}