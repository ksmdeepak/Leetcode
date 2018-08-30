class Solution {
    public int[] twoSum(int[] nums, int target) {  
        Map<Integer,Integer> hm = new HashMap<Integer,Integer>();
        for (int i=0;i<nums.length;i++){
            if(hm.get(target-nums[i])!=null){
                return new int[] {hm.get(target-nums[i]),i};
            }
            else{
                    hm.put(nums[i],i);    
            }
            
        }
        return new int[] {0,0};
    }
}