//https://leetcode.com/problems/two-sum/description/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int b=nums.size();
        for(int i=0;i<b;i++){
            for(int j=i+1;j<b;j++){
                if(nums[i]+nums[j]==target){
                    return {i,j};
                }

            }
        }
        return {};
}
};
