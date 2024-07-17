import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        while (true) {
            int t = scan.nextInt();
            if (t == 0)
                break;
            float tall = 0;
            String name = "";
            for (int i = 0; i < t; i++) {
                String n = scan.next();
                float h = scan.nextFloat();
                if (h > tall) {
                    tall = h;
                    name = n;
                } else if (h == tall) {
                    name = name + " " + n;
                }
            }
            System.out.println(name);
        }
    }
}
