/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
	public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
		List<Integer> ret = new ArrayList<>();
		if (k == 0) {
			ret.add(target.val);
			return ret;
		}
		Map<Integer, List<Integer>> graph = new HashMap<>();
		treeToGraph(root, graph);
		Queue<Integer> q = new LinkedList<>();
		q.add(target.val);
		List<Integer> visited = new ArrayList<>();
		int level = 1;
		while (!q.isEmpty()) {
			int size = q.size();
			while (size-- > 0) {
				int s = q.poll();
				visited.add(s);
				for (int i : graph.getOrDefault(s, new ArrayList<>())) {
					if (!visited.contains(i)) {
						q.add(i);
						if (level == k) {
							ret.add(i);
						}
					}
				}
			}
			if (level == k)
				return ret;
			level++;
		}
		return ret;
	}



	private void treeToGraph(TreeNode root, Map<Integer, List<Integer>> graph) {
		if (root == null)
			return;
		if (root.left != null) {
			graph.computeIfAbsent(root.val, k -> new ArrayList<>()).add(root.left.val);
			graph.computeIfAbsent(root.left.val, k -> new ArrayList<>()).add(root.val);
		}
		if (root.right != null) {
			graph.computeIfAbsent(root.val, k -> new ArrayList<>()).add(root.right.val);
			graph.computeIfAbsent(root.right.val, k -> new ArrayList<>()).add(root.val);
		}
		treeToGraph(root.left, graph);
		treeToGraph(root.right, graph);
	}
}