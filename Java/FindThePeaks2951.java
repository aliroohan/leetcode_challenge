import java.util.ArrayList;
import java.util.List;

public class FindThePeaks2951 {
    public static void main(String[] args) {
        int[] mountain = {1, 2, 3, 2, 1};
        FindThePeaks2951 obj = new FindThePeaks2951();
        List<Integer> peaks = obj.findPeaks(mountain);
        System.out.println(peaks);
    }


    public List<Integer> findPeaks(int[] mountain) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 1; i < mountain.length - 1; i++){
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]){
                arr.add(i);
            }
        }
        return arr;
    }
}