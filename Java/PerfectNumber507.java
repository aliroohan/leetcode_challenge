class Solution {
    public boolean checkPerfectNumber(int num) {
        int sum = 0;
        for(int i = 1;i <= num / 2; i++){
            if (num % i == 0){
                sum += i;
            }
        }
        if (sum == num)
            return true;
        else
            return false;
    }
}

public class PerfectNumber507 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkPerfectNumber(28));
    }
}