class Solution {
    public int strStr(String haystack, String needle) {
        String res = haystack.replaceFirst(needle, "*");
        if(res.equals(haystack))
        return -1;
        for(int i=0;i<haystack.length();i++)
            if(res.charAt(i) == '*')
                return i;
        
        return 0;
    }
}