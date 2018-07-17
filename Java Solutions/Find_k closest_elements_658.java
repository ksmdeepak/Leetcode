class Solution {
    int binarySearch(int arr[], int l, int r, int x)
    {
        // System.out.println(l);
        if (r>=l)
        {
            int mid = l + (r - l)/2;
 
            if (arr[mid] == x)
               return mid;
 
            if (arr[mid] > x)
               return binarySearch(arr, l, mid-1, x);
 
            return binarySearch(arr, mid+1, r, x);
        }
 
        if(l>=0 && l<arr.length)
            return l;
        else
            return r;
    }
    
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int location = binarySearch(arr,0,arr.length-1,x);
        System.out.println(location);
         
        
        int leftDiff = 0;
        int rightDiff=0;
        int right = 0;
        int left=0;
        
        if(arr[location]==x){
            
            if(location==0){
                int output[] = Arrays.copyOfRange(arr,0,k);
                // for (int i : output)
                //     System.out.print(i + "  ");
                return IntStream.of(output).boxed().collect(Collectors.toList());
            }
            else if(location==arr.length-1){
                 int output[] = Arrays.copyOfRange(arr,arr.length-k,arr.length);
                 return IntStream.of(output).boxed().collect(Collectors.toList());
            }
            else{
                right=location+1;
                left=location-1;      
            }  
            k=k-1;
        }
        else{
            right=location;
            left=location-1;
            
        }
        
        while(k>0  && left>-1 && right<arr.length){
            
            if(x-arr[left]<=arr[right]-x){
                left--;
            }
            else{
                right++;
            }
            k=k-1;
        }
        if(k!=0){
            if(left==-1)
                right=right+k;
            else
                left=left-k;
        }
        
        
          
        int output[] = Arrays.copyOfRange(arr,left+1,right);
         return IntStream.of(output).boxed().collect(Collectors.toList());
    }
}