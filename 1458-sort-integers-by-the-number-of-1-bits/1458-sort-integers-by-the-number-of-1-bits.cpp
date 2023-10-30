class Solution {
public: 
    static int countBit(int n)
    {
        int cnt = 0 ;
        while(n)
        {
            n = n & (n - 1);
            cnt++;
        }
        return cnt ;
    }

    static bool comp(int x, int y)
    {   
        int bitCountX = countBit(x);
        int bitCountY = countBit(y);
        
        if (bitCountX == bitCountY) 
            return x < y;

        return bitCountX < bitCountY;
    }
    
    vector<int> sortByBits(vector<int>& arr) 
    {
        sort(arr.begin(),arr.end(),comp) ;

        return arr ;
    }
};