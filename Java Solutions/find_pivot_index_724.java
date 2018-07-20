class Solution {
    public int pivotIndex(int[] nums) {
        int[] sumSoFar = new int[nums.length];
        int total=0;
        for(int i=0;i<sumSoFar.length;i++){
            total=total+nums[i];
            sumSoFar[i]=total;
        }
        for(int i=0;i<sumSoFar.length;i++){
            if(sumSoFar[i]-nums[i]==total-sumSoFar[i]){
                return i;
            }
        }
        return -1;
    }
}