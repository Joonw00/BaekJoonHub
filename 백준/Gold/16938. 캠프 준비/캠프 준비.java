import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int L = scanner.nextInt();
        int R = scanner.nextInt();
        int X = scanner.nextInt();

        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        Arrays.sort(A);
        int ans = 0;
        for (int subset = 1; subset < (1 << N); subset++) {
            int sum = 0;
            int count = 0;
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                if ((subset & (1 << i)) != 0) {
                    sum += A[i];
                    count += 1;
                    min = Math.min(min, A[i]);
                    max = Math.max(max, A[i]);
                }
            }

            if (sum < L || sum > R || max - min < X || count < 2) {
                continue;
            }
            ans++;

        }
        System.out.println(ans);

    }
}
