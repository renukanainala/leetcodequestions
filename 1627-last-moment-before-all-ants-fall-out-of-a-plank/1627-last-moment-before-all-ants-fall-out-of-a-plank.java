class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int mini=Integer.MIN_VALUE;
        for(int i:left){
            mini=Math.max(mini,i);
        }
        for(int i:right){
            mini=Math.max(mini,n-i);
        }
        return mini;
    }
}