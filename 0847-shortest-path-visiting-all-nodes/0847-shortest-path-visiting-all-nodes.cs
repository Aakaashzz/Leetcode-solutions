public class Solution {
    public int ShortestPathLength(int[][] graph) {
        int n = graph.Length;
        int targetMask = (1 << n) - 1;
        int[][] visited = new int[n][];
        for (int i = 0; i < n; i++) {
            visited[i] = new int[1 << n];
        }

        Queue<(int, int, int)> queue = new Queue<(int, int, int)>();
        for (int i = 0; i < n; i++) {
            queue.Enqueue((i, 1 << i, 0));
            visited[i][1 << i] = 1;
        }

        while (queue.Count > 0) {
            var (node, mask, dist) = queue.Dequeue();

            if (mask == targetMask)
                return dist;

            foreach (var neighbor in graph[node]) {
                int newMask = mask | (1 << neighbor);
                if (visited[neighbor][newMask] == 0) {
                    visited[neighbor][newMask] = 1;
                    queue.Enqueue((neighbor, newMask, dist + 1));
                }
            }
        }

        return -1; // If no valid path is found
    }
}