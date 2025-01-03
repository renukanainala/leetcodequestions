class Solution {
    public int waysToSplitArray(int[] nums) {
        int n=nums.length;
        long p[]=new long[nums.length];
        p[0]=nums[0];
        for(int i=1;i<n;i++){
            p[i]=p[i-1]+nums[i];
        }
        long tsum=p[n-1];
        long c=0;
        for(int i=0;i<n-1;i++){
            if (p[i]>=tsum-p[i]){
                c+=1;
            }
        }
        return (int)c;
    }
}