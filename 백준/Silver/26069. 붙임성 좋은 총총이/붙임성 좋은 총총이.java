import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        // Array
        ArrayList<String> dance = new ArrayList<>();
        dance.add("ChongChong");

        for (int i = 0; i < N; i++) {
            String str1 = scanner.next();
            String str2 = scanner.next();

            if (dance.contains(str2) && !dance.contains(str1)) {
                dance.add(str1);
            }
            if (dance.contains(str1) && !dance.contains(str2)) {
                dance.add(str2);
            }
        }
        System.out.println(dance.size() );

    }
}