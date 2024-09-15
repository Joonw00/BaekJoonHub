import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int[][] rectangles = new int[N][2];

        for (int i = 0; i < N; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            rectangles[i][0] = a;
            rectangles[i][1] = b;
        }
        int[][] dp = new int[N][2];
        // 0: a가 가로, 1 : b가 가로
        dp[0][0] = rectangles[0][0];
        dp[0][1] = rectangles[0][1];
        for (int i = 1; i < N; i++) {
            dp[i][0] = Math.max(dp[i - 1][0] + rectangles[i][0] + Math.abs(rectangles[i][1] - rectangles[i - 1][0]),
                    dp[i - 1][1] + rectangles[i][0] + Math.abs(rectangles[i][1] - rectangles[i - 1][0]));
            dp[i][1] = Math.max(dp[i - 1][0] + rectangles[i][1] + Math.abs(rectangles[i][0] - rectangles[i - 1][1]),
                    dp[i - 1][1] + rectangles[i][1] + Math.abs(rectangles[i][0] - rectangles[i - 1][0]));
        }
        int ans = Math.max(dp[N - 1][0], dp[N - 1][1]);
        System.out.println(ans);

    }
}
