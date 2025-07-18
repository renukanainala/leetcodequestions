class Solution {
    private static int check(int i,int j,String s,String t,int [][] dp){
        if (i<0|| j<0){
            return 0;
        }
        if (dp[i][j]!=-1){
            return dp[i][j];
        }
        if(s.charAt(i)==t.charAt(j)){
           dp[i][j]= 1+check(i-1,j-1,s,t,dp);
        }
        else{
        dp[i][j]= Math.max(check(i-1,j,s,t,dp),check(i,j-1,s,t,dp));}
        return dp[i][j];
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int [][] dp=new int[text1.length()][text2.length()];
        for(int i=0;i<text1.length();i++){
            for(int j=0;j<text2.length();j++)
{
    dp[i][j]=-1;
}        }
        return check(text1.length()-1,text2.length()-1,text1,text2,dp);
    }
}