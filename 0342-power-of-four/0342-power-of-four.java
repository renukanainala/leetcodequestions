class Solution {
    public boolean isPowerOfFour(int n) {
        if (n<=0){
            return false;
        }
        double l1=Math.log(n)/Math.log(4);
        return l1==(int)l1;

    }
}