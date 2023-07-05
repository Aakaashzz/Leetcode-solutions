class Solution {
    public int longestSubarray(int[] nums) {
        List<Integer> l = new ArrayList<>();
        int n = nums.length, i=0;
        int s = 1;
        for(i=1;i<n;i++){
            int nu = nums[i];
            if(nu>0){
                if(nums[i-1]>0){
                    s++;   
                }else{
                    l.add(-s);
                    s=1;
                }
            }else{
                if(nums[i-1]>0){
                    l.add(s);
                    s=1;
                }else{
                    s++;
                }
            }
        }
        
        if(nums[n-1]>0) l.add(s);
        else l.add(-s);
        
        int ans = 0;
        for(i=0;i<l.size();i++){
            int nu = l.get(i);
            if(nu>0){
                ans = Math.max(ans,nu);
            }else if(nu==-1){
                int ad =0;
                if(i-1>=0)
                    ad+=l.get(i-1);
                if(i+1<l.size())
                    ad+=l.get(i+1);
                ans = Math.max(ans,ad);
            }
        }
        if(ans==n)
            ans--;
        
        return ans;
    }
}
