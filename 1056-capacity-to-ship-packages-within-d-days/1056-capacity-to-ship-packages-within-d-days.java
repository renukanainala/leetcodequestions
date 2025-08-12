class Solution {
    private static boolean isposible(int m,int[] w, int d){
        int l=0;
        int c=1;
        for(int i:w){
            //l+=i;
            if (l+i>m){
                l=0;
                c+=1;;

            }
            l+=i;
        }
        
        
        return c<=d;
    }
    public int shipWithinDays(int[] weights, int days) {
        int maxi=Integer.MIN_VALUE;
        int h=0;
        for(int i:weights){
            maxi=Math.max(maxi,i);
            h+=i;
        }
        int l=maxi;
        int ans=-1;
        while (l<=h){
            int m=(l+h)/2;
            if (isposible(m,weights,days)){
                ans=m;
                h=m-1;
            }
            else{
                l=m+1;
            }
        }
        return ans;
    }
}