class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if (r*c!=mat.length*mat[0].length) return mat;
        int r1=0;
        int c1=0;
        int m=mat.length;
        int n=mat[0].length;
        int[][] ans= new int[r][c];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                    ans[r1][c1]=mat[i][j];
                    c1+=1;
                    if(c1==c){
                        r1+=1;
                        c1=0;
                    } 

        }
        
    }
    return ans;
    }
}