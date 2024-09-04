import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int x1 = scanner.nextInt();
            int y1 = scanner.nextInt();
            int x2 = scanner.nextInt();
            int y2 = scanner.nextInt();
            int x3 = scanner.nextInt();
            int y3 = scanner.nextInt();
            int x4 = scanner.nextInt();
            int y4 = scanner.nextInt();

            int x5 = Math.max(x1, x3);
            int x6 = Math.min(x2, x4);
            int x = x6 - x5;
            if (x < 0) {
                x = 0;
            }

            int y5 = Math.max(y1, y3);
            int y6 = Math.min(y2, y4);
            int y = y6 - y5;
            if (y < 0) {
                y = 0;
            }
            int total = (x2 - x1) * (y2 - y1);
            System.out.println(total - x * y);

        }
    }
}