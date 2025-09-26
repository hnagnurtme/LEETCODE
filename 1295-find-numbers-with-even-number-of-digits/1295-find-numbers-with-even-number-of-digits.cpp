class Solution {
public:
    int extractNum(int num){
        int count = 0;
        while(num != 0){
            num /= 10;
            count ++;
        }
        return count;
    }
    int findNumbers(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i <nums.size();i++){
            if( extractNum(nums[i]) %2 == 0) result++;
        }
        return result;
    }
};