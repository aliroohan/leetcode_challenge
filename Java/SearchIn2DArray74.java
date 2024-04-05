public class SearchIn2DArray74 {
    public static void main(String[] args) {
        int[][] matrix = {{-8,-7,-5,-3,-3,-1,1},{2,2,2,3,3,5,7},{8,9,11,11,13,15,17},{18,18,18,20,20,20,21},{23,24,26,26,26,27,27},{28,29,29,30,32,32,34}};
        int target = -5;
        System.out.println(searchMatrix(matrix, target));
    }
    public static boolean searchMatrix(int[][] matrix, int target) {
        int start = 0;
        int end = matrix.length - 1;
        int i = 0;
        while (start <= end){
            int mid = start + (end - start) / 2;
            if (target >= matrix[mid][0] && target <= matrix[mid][matrix[mid].length - 1]){
                i = mid;
                break;
            }
            if (target >= matrix[mid][0]){
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        start = 0;
        end = matrix[i].length - 1;
        while(start <= end){
            int mid = start + (end - start) / 2;
            if (matrix[i][mid] == target){
                return true;
            }
            if (matrix[i][mid] < target){
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return false;
    }
}