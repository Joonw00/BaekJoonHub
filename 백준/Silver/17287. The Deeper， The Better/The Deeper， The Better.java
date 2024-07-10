import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        int ans = 0;

        int temp = 0;

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '[') {
                temp += 3;
            } else if (c == '{') {
                temp += 2;
            } else if (c == '(') {
                temp += 1;
            } else if (c == ')') {
                temp -= 1;
            } else if (c == '}') {
                temp -= 2;
            } else if (c == ']') {
                temp -= 3;
            } else {
                ans = temp > ans ? temp : ans;
            }
        }

        System.out.println(ans);
    }

}
