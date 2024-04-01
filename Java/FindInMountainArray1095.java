/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        return peakIndexInMountainArray(mountainArr, target);
    }
    public int peakIndexInMountainArray(MountainArray arr, int target){
        int start = 0;
        int end = arr.length() - 1;
        while (start < end){
            int mid = start + (end - start) / 2;
            if (arr.get(mid) > arr.get(mid + 1)){
                end = mid;
            } else{
                start = mid + 1;
            }
        }
        int ans = binarySearchAsc(arr,target,0,start);
        if (ans != -1){
            return ans;
        }
        ans = binarySearchDsc(arr, target, start, arr.length() - 1);
        return ans;
    }
    public int binarySearchAsc(MountainArray arr, int target, int start, int end){
        while(start <= end){
            int mid = start + (end - start) / 2;
            int num = arr.get(mid);
            if(num == target){
                return mid;
            }
            if(num < target){
                start = mid + 1;
            }             
            if(num > target){
                end = mid - 1;
            }               
        }
        return -1;
    }
    public int binarySearchDsc(MountainArray arr, int target, int start, int end){
        while(start <= end){
            int mid = start + (end - start) / 2;
            int num = arr.get(mid);
            if(num == target){
                return mid;
            }
            if(num > target){
                start = mid + 1;
            }             
            if(num < target){
                end = mid - 1;
            }               
        }
        return -1;
    }
}