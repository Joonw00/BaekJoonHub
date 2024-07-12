import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        // 문자열 입력 받기
        String str = scan.nextLine();
        String str2 = scan.nextLine();

        int B = 0, Y = 0, G = 0, R = 0;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == 'B') {
                B++;
            } else if (c == 'Y') {
                Y++;
            } else if (c == 'G') {
                G++;
            } else if (c == 'R') {
                R++;
            }
        }

        for (int i = 0; i < str2.length(); i++) {
            char c = str2.charAt(i);
            if (c == 'B') {
                B--;
            } else if (c == 'Y') {
                Y--;
            } else if (c == 'G') {
                G--;
            } else if (c == 'R') {
                R--;
            }
        }
        int sumOfAbs = Math.abs(B) + Math.abs(Y) + Math.abs(G) + Math.abs(R);
        System.out.println(sumOfAbs / 2);
    }
}
