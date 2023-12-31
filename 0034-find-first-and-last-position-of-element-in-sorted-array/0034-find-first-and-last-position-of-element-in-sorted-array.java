class Solution {
    
    public int[] searchRange(int[] nums, int target) 
    {
        int[] ans={-1,-1};
        int n=nums.length;

        int index=find(nums,0,n-1,target); 
        //Checking element is present or not in array.


        if(index!=-1)
        {
            ans[0]=index;
            ans[1]=index;

            while(index-1>=0 && nums[index-1]==target)//move back till first index
                ans[0]=--index;

            while(index+1<n && nums[index+1]==target)//move forward till last index
                ans[1]=++index;
            
        }

        return ans;
    }

    public int find(int[] nums,int s,int e,int target) //binary search function
    {
        if(s<=e)
        {
            int mid=(s+e)/2;
            if(nums[mid]==target)
                return mid;
            else if(target>nums[mid])
                return find(nums,mid+1,e,target);
            else
                return find(nums,s,mid-1,target);            
        }
        return -1;
    }
}