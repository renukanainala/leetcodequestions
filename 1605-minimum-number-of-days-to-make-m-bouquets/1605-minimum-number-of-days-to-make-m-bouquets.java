class Solution {
    private static boolean checkwillbloom(int[] bloomDay, int v,int m, int k){
        int c=0;
        //int c1=0;
        for (int i: bloomDay){
            if (i<=v){
                c+=1;
                if (c==k){
                m-=1;
                c=0;
            }
            }
            else{
                c=0;
            }
           
        }
        return m<=0;
    }
    public int minDays(int[] bloomDay, int m, int k) {
        int n=bloomDay.length;
        if (n<m*k) return -1;
        int mini=Integer.MAX_VALUE;
        int maxi=Integer.MIN_VALUE;
        for(int i:bloomDay){
            mini=Math.min(mini,i);
            maxi=Math.max(maxi,i);
        }
        int l=1;
        int h=maxi;
        int ans=-1;
        while (l<=h){
            int m1=(l+(h-l)/2);
            if (checkwillbloom(bloomDay,m1,m,k)){
                ans=m1;
                h=m1-1;
            }
            else{
                l=m1+1;
            } 

        }
        return ans;
    }
    
}