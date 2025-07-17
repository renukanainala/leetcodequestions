class Solution {
    public int minStartValue(int[] nums) {
        int minipos=0;
        int maxi=Integer.MAX_VALUE;
        for(int i:nums){
            minipos+=i;
            maxi=Math.min(maxi,minipos);
        }
        return  (maxi<1) ?(-1*maxi+1): 1;

    }
}