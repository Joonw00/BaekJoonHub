import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        String S = scan.next();

        ArrayList<Integer> results = new ArrayList<>();
        String target = "long";
        int length = target.length();
        int count = 0;

        for (int i = 0; i < N + 1 - length; i++) {
            if (S.substring(i, i + length).equals(target)) {
                count++;
                i += length - 1;
            } else { // 연속돼서 long이 아니라면
                if (count > 0) {
                    if (count > 1) {
                        results.add(count);
                    }
                    count = 0;
                }
            }
        }
        if (count > 0) {
            results.add(count);
        }
        int ans = 1;

        for (int i = 0; i < results.size(); i++) {
            int total = results.get(i);
            int temp = 0;
            for (int j = 0; j <= total / 2; j++) {
                // j, total - 2*j 이항계수
                int a = total - 2 * j;
                int b = j;

                long permutation = permutation(a + b, a, b);
                temp += permutation;
            }
            ans *= temp;
        }
        System.out.println(ans);

    }

    public static long permutation(int n, int aCount, int bCount) {
        long numerator = factorial(n);
        long denominator = factorial(aCount) * factorial(bCount);
        return numerator / denominator;
    }

    public static long factorial(int n) {
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
