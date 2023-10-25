class Solution {
    public int kthGrammar(int n, int k) {
        if(n < 3)
            return k - 1;
        int half = (int)Math.pow(2, n - 2);
        if(k <= half)
            return kthGrammar(n - 1, k);
        return kthGrammar(n - 1, k - half) == 0? 1 : 0; 
    }
}