class Solution2 {
    public int maximumWealth(int[][] accounts) {
        int max = sum(accounts[0]);
        for (int [] n: accounts){
            if (max < sum(n)) {
                max = sum(n);
            }
        }
        return max;
    }
    int sum(int[] num){
        int total = 0;
        for (int n: num){
            total += n;
        }
        return total;
    }
}
public class RichestCostumerWealth1672 {
    public static void main(String[] args) {
        Solution2 sol = new Solution2();
        int [][] arr = {{1,2,3},{3,2,1}};
        System.out.println(sol.maximumWealth(arr));
    }
}
