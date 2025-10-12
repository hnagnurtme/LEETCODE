class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length ;
        int [][] arr = new int[len][2];

        for( int i = 0 ; i < len ; i++){
            arr[i][0] = nums[i];
            arr[i][1] = i;
        }

        Arrays.sort( arr , (a , b) -> ( a[0] - b[0]));

        int left = 0;
        int right = len - 1;

        while( left < right){
            if( arr[left][0] + arr[right][0]  < target){
                left += 1 ;
                continue;
            }
            
            if( arr[left][0] + arr[right][0]  > target){
                right -= 1 ;
                continue;
            }

            if(arr[left][0] + arr[right][0]  == target){
                return new int[] { arr[left][1] , arr[right][1]};
            }
        }
        return new int [] {} ;
    }
}