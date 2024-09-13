import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        Stack<Long> stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            int a = scanner.nextInt();
            long b = scanner.nextInt();
            if (a == 1) {
                stack.push(b);
            } else {
                if (!stack.empty()) {
                    long k = stack.pop();
                    stack.push(Math.max(k - b, 0));
                }
            }
        }

        long ans = 0;
        long compare = 0;
        if (!stack.empty()) {
            compare = stack.peek();
            while (!stack.empty()) {
                long now = stack.pop();
                if (now >= compare) {
                    ans += compare;
                } else {
                    compare = now;
                    ans += now;
                }
            }
        }

        System.out.print(ans);
    }
}
