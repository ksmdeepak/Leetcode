class Solution {
    public boolean findSum(int sum,int[] nums,int n){
        boolean subset[][] = new boolean[sum+1][n+1];
        for(int i=0;i<=n;i++)
            subset[0][i]=true;
        for(int i=1;i<=sum;i++)
            subset[i][0]=false;
        for(int i=1;i<=sum;i++){
            for(int j=1;j<=n;j++){
                subset[i][j] = subset[i][j-1];
                if(i>=nums[j-1] && !subset[i][j]){
                    subset[i][j] = subset[i-nums[j-1]][j-1];
                }
            }
        }
        return subset[sum][n];
    }
    
    public boolean canPartition(int[] nums) {
        int sum=0;
        for(int i=0;i<nums.length;i++)
            sum=sum+nums[i];
        if (sum%2!=0)
            return false;
        else
            return findSum(sum/2,nums,nums.length);
    }
}