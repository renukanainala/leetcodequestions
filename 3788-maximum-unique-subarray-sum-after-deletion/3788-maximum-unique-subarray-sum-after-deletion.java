class Solution {
    public int maxSum(int[] nums) {
        HashSet<Integer> s=new HashSet<>();
        int r=0;
        for(int i:nums){
            if (!s.contains(i) && i>=0){
                r+=i;
            }
            s.add(i);
        }
        if (r==0)  r=Arrays.stream(nums).max().getAsInt();
        return r;
    }
}