class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums); 
        int i = 1;
        int count = 0; 
        while(i<nums.length){
            while(i<nums.length && nums[i] == nums[i-1]){
                count++;
                if(count == nums.length/2)
                    return nums[i];
               i++;
         
            }
            i++;
            count = 0;
        }
        return 1;
    }
}