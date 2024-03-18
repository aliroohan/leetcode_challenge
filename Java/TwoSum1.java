class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        int [] arr= new int[2];
        for (int i = 0; i < nums.length; i++){
            for(int j = 0;j < nums.length; j++){
                if (i == j)
                    continue;
                if (nums[i] + nums[j] == target){
                    arr[0] = i;
                    arr[1] = j;
                }
            }
        }
        return arr;
    }
}
public class TwoSum1 {
    public static void main(String[] args) {
        Solution1 sol = new Solution1();
        int [] arr = {2,7,11,15};
        int target = 9;
        int [] result = sol.twoSum(arr, target);
        for (int i = 0; i < result.length; i++){
            System.out.println(result[i]);
        }
    }
}
