class Solution {
    public int missingNumber(int[] nums) {

        int[] c = new int[nums.length + 1] ;
        for( int i = 0; i < c.length;i++){
            c[i] = -1;
        }
        for( int i = 0; i < nums.length;i++){
            c[nums[i]] = i;
        }

        for(int i = 0; i < c.length;i++){
            if( c[i] == -1){
                return i;
            }
        }

        return 0;

    }
}