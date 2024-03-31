public class FirstAndLast34 {
    public static void main(String[] args) {
        int [] arr = {5,7,7,8,8,10};
        int target = 8;
        int [] ans = searchRange(arr, target);
        System.out.println(ans[0] + " " + ans[1]);
    }
    public static int[] searchRange(int[] nums, int target) {
        int [] ans = {-1, -1};
        int start = 0;
        int end = nums.length - 1;
        while (start <= end){
            int mid = start + (end - start) / 2;
            if (target < nums[mid]){
                end = mid - 1;
            } else if (target > nums[mid]){
                start = mid + 1;
            } else{
                ans[0] = mid;
                end = mid - 1;
            }

        }


        start = 0;
        end = nums.length - 1;
        while (start <= end){
            int mid = start + (end - start) / 2;
            if (target < nums[mid]){
                end = mid - 1;
            } else if (target > nums[mid]){
                start = mid + 1;
            } else {
                ans[1] = mid;
                start = mid + 1;
            }

        }
        return ans;
    }
}
