public class EvenNumberofDigits1295 {
    public static void main(String[] args) {

        int [] arr = {12,345,2,6,7896};
        System.out.println(findNumbers(arr));
    }
    public static int findNumbers(int[] nums) {
        int count = 0;
        for(int num: nums){
            String s = String.valueOf(num);
            if (s.length() % 2 == 0)
                count++;
        }
        return count;
    }

}
