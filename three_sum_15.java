import java.util.*;

public class three_sum_15 {

    HashSet<List<Integer>> output = new HashSet<List<Integer>>();


    public void find_triplets(int[] nums){

        for(int i=0;i<nums.length-2;i++){


            int l = i+1;
            int r = nums.length-1;
            int sum = 0-nums[i];

            while(l<r){

                if(nums[l]+nums[r]==sum){
                    ArrayList<Integer> temp = new ArrayList<Integer>(Arrays.asList(nums[i],nums[l],nums[r]));

                    output.add(temp);
                    l++;
                    r--;
                }
                else if(nums[l]+nums[r]>sum){
                    r--;
                }
                else{
                    l++;
                }
            }

        }

    }

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        find_triplets(nums);
        return new ArrayList<List<Integer>>(output);
    }


    public static void main(String args[]){
        int[] nums = {-1,0,1,2,-1,-4};
        three_sum_15 obj = new three_sum_15();
        System.out.println(obj.threeSum(nums));



    }
}
