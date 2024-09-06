import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] dp = new int[100001];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 1;
        dp[3] = 1;
        for (int j = 0; j < 100001; j++) {
            if (j + 2 <= 100000)
                dp[j + 2] = (dp[j + 2] + dp[j]) % 1000000009;
            if (j + 4 <= 100000)
                dp[j + 4] = (dp[j + 4] + dp[j]) % 1000000009;
            if (j + 6 <= 100000)
                dp[j + 6] = (dp[j + 6] + dp[j]) % 1000000009;
        }

        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int N = scanner.nextInt();
            System.out.println(dp[N]);
        }
    }
}