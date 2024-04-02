public class SearchInROtatedArray33 {
    public static void main(String[] args) {
        int [] arr = {4,5,6,7,0,1,2};
        int target = 0;
        System.out.println(search(arr, target));
//        int [] arr2 = {3, 1};
//        int target2 = 1;
//        System.out.println(search(arr2, target2));
    }
    public static int search(int[] nums, int target) {
        return peakIndexInMountainArray(nums, target);
    }
    public static int peakIndexInMountainArray(int[] arr, int target) {
        int start = 0;
        for (int i = 0;i < arr.length - 1; i++){
            if (arr[i] > arr[i + 1]) {
                start = i;
                break;
            }
        }
        int end1 = arr.length - 1;
        int ans = binarySearch(arr,target,0,start);
        if (ans != -1){
            return ans;
        }
        ans = binarySearch(arr, target, start + 1, end1);
        return ans;


    }
    public static int binarySearch(int [] arr, int target, int start, int end){
        while(start <= end){
            int mid = start + (end - start) / 2;
            if(arr[mid] == target){
                return mid;
            }
            if(arr[mid] < target){
                start = mid + 1;
            }if(arr[mid] > target){
                end = mid - 1;
            }
        }
        return -1;
    }
}
