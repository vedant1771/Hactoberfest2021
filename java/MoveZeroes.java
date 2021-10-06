import java.util.Arrays;

public class MoveZeroes {
    public static void main(String[] args) throws Exception {
        int[] ret = new int[]{0,1,0,3,12};
        moveZeroes(ret);
        System.out.println(Arrays.toString(ret));
    }
    public static void moveZeroes(int[] nums) {
        if(nums == null || nums.length == 0){
            return;
        }
        int cur = 0;
        for(int i = 0 ; i < nums.length; i++) {
           if(nums[i] != 0){
                int tmp = nums[cur];
                nums[cur] = nums[i];
                nums[i] = tmp;
                cur++;
            }
        }
    }
}
