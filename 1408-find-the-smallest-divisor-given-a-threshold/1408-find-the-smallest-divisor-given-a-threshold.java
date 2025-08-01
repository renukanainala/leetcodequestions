class Solution {
    private static int find(int[] nums,int v){
        int s=0;
        for(int i:nums){
            s+=(i+v-1)/v;
        }
        return s;
    }
    public int smallestDivisor(int[] nums, int threshold) {
      int v=Integer.MIN_VALUE;
      for(int i=0;i<nums.length;i++){
        v=Math.max(nums[i],v);
      }  
      int l=1;
        int h=v;
        int     ans=v; 
        while(l<=h){
          int m=(l+h)/2;
          int k=find(nums,m);
          if (k >threshold) l=m+1; 
          else if (k <=threshold) {
                ans=m;
                h=m-1;
          }
        }
        return  ans;
      
    }
}