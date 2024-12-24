class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        HashMap<Integer,Integer>h=new HashMap<>();
        HashSet<Integer> s1=new HashSet<>();
        HashSet<Integer> s2=new HashSet<>();
        HashSet<Integer> s3=new HashSet<>();
        for(int i:nums1){
            s1.add(i);
        }
        for(int i:nums2){
            s2.add(i);
        }
        for(int i:nums3){
            s3.add(i);
        }
        for(int i:s1){
            h.put(i,h.getOrDefault(i,0)+1);
        }
        for(int i:s2){
            h.put(i,h.getOrDefault(i,0)+1);
        }
        for(int i:s3){
            h.put(i,h.getOrDefault(i,0)+1);
        }
        List<Integer> a=new ArrayList<>();
        for(Map.Entry<Integer,Integer> e:h.entrySet()){
            if (e.getValue()>=2){
                a.add(e.getKey());
            }
        }
        return a;
    }
}