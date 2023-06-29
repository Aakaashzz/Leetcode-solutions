class Solution {
    class State {
        int i;
        int j;
        int key;
        State(int i, int j, int key) {
            this.i = i;
            this.j = j;
            this.key = key;
        }
    }

    int[][] moves = new int[][]{ {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

    int[][][] dp = new int[31][31][64];

    boolean isLower(char c) {
        return 'a' <= c && 'z' >= c;
    }

    boolean isUpper(char c) {
        return 'A' <= c && 'Z' >= c;
    }

    public int shortestPathAllKeys(String[] grid) {

        int n = grid.length;
        int m = grid[0].length();

        Queue<State> q = new LinkedList<>();
        int start_i = 0, start_j = 0;
        int key = 0;
        for(int i = 0; i < n; i ++) {
            for(int j = 0; j < m; j ++) {
                if(grid[i].charAt(j) == '@') {
                    start_i = i;
                    start_j = j;
                }
                else if(isLower(grid[i].charAt(j)) == true) {
                    key |= 1 << (grid[i].charAt(j) - 'a');
                }
            }
        }
        
        dp[start_i][start_j][key] = 1;

        q.add(new State(start_i, start_j, key));
        
        return solve(grid, q);
    }


    int solve(String[] grid, Queue<State> q) {
        int n = grid.length;
        int m = grid[0].length();

        int ans = 0;

        while(q.size() > 0) {

            int sz = q.size();

            for(int i = 0; i < sz; i ++) {

                State state = q.remove();

                if(state.key == 0) { // if we have taken all keys
                    return ans;
                }

                for(int[] move : moves) { // move in four directions

                    int x = move[0] + state.i;
                    int y = move[1] + state.j;

                    // check if index is valid or not
                    if(x == -1 || x == n || y == -1 || y == m) {
                        continue;
                    }

                    char ch = grid[x].charAt(y);

                    if(ch == '#') { // if its a wall, continue
                        continue;
                    }

                    int key = state.key;

                    if(isLower(ch) == true) { // if its a key
                        int mask = 0b111111 ^ (1 << (ch - 'a'));
                        key &= mask; // mark it as taken
                    }

                    else if(isUpper(ch) == true) { // if its a lock
                        int mask = 1 << (ch - 'A');
                        if((mask & key) != 0) { // if we don't have the key
                            continue;
                        }
                    }
                    /*
                        If we have not been to grid[x][y] with 
                        current key configuration, we will add a new state
                        to queue
                     */
                    if(dp[x][y][key] != 1) {
                        q.add(new State(x, y, key));
                        dp[x][y][key] = 1;
                    }
                }
            }

            ans ++;
        }
        return -1;
    }
}