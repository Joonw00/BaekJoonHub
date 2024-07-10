import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        while (true) {
            String input = scan.nextLine();
            int ans = 0;
            if (input.equals("#")) {
                break;
            }
            for (int i = 0; i < input.length(); i++) {
                char t = input.charAt(i);
                if (t == 'a' || t == 'e' || t == 'i' || t == 'o' || t == 'u' || t == 'A' || t == 'E' || t == 'I'
                        || t == 'O' || t == 'U') {
                    ans++;
                }
            }
            System.out.println(ans);
        }

    }

}
