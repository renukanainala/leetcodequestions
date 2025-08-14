class Solution {
    public String largestGoodInteger(String num) {
        char[] A1=num.toCharArray();
        char g=A1[0];
        int c=1;
        int maxi=-1;
        for(int i=1;i<num.length();i++ ){
            if(A1[i]==g){
                c+=1;

            }
            else{
                g=A1[i];
                c=1;
            }
            if (c>=3){
                maxi=Math.max(maxi,g-'0');
            }
        }
        if (maxi==-1){return "";}
        char m=(char) (maxi+'0');
        return ""+m+m+m;
    }
}