/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

 public class GuessTheNumberHigherLower374  extends GuessGame {
    public int guessNumber(int n) {
        int start = 1;
        int end = n;
        int mid = start + (end - start) / 2;
        while (guess(mid) != 0){
            if (guess(mid) == -1){
                end = mid - 1;
            } else {
                start = mid + 1;
            }
            mid = start + (end - start) / 2;
        }
        return mid;
    }
}