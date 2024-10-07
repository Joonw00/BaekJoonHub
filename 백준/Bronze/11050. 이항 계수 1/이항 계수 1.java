import java.util.*;

public class Main {
    public static int factorial(int n) {
        if (n == 1 || n == 0)
            return 1;
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int ans = factorial(n) / (factorial(n - k) * factorial(k));
        System.out.print(ans);

    }
}
