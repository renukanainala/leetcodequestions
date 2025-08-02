class Solution {
    private static long find(int [] p,int v){
        long s=0;
        for(int i:p){
            s+=(long)(i+v-1)/v;
        }
        return s;
    }
    public int minEatingSpeed(int[] piles, int h1) {
        int v=Integer.MIN_VALUE;
        for(int i:piles){
            v=Math.max(v,i);
        }
        int l=1;
        int h=v;
        int     ans=v;
        while (l<=h){
            int m=l+(h-l)/2;
            long r=find(piles,m);
            if (r>h1){
                l=m+1;
            }
            else{
                    ans=m;
                    h=m-1;
            }
        }
        return  l;
    }
}

