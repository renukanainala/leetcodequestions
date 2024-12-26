class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums3=new int[nums1.length+nums2.length];
        int i=0,j=0,k=0;
        while(i<nums1.length && j<nums2.length){
            if(nums1[i]<nums2[j]){
                nums3[k]=nums1[i];
                k++;
                i++;
            }
            else{
                nums3[k]=nums2[j];
                k++;
                j++;
            }
        }
        while(i<nums1.length){
            nums3[k]=nums1[i];
            k++;
            i++;
        }
        while(j<nums2.length){
            nums3[k]=nums2[j];
            k++;
            j++;
        }
        
        int n=nums3.length;
        if(n%2==1){
            return (double)(nums3[n/2]);
        }
        else{
            return ((nums3[n/2]+(nums3[n/2-1]))/2.0);
        }
    }
} 