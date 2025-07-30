class Solution {
    public int longestSubarray(int[] nums) {
        int maxi=Integer.MIN_VALUE;
        for(int i:nums){
            maxi=Math.max(maxi,i);
        }
        int c=0;
        int c1=0;
        for(int i:nums){
            if (i==maxi){
                c+=1;
                c1=Math.max(c1,c);
            }
            else{
                c=0;
            }
        }
        return c1;
    }
}