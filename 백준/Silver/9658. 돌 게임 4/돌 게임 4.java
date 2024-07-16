import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[1002];

        arr[1] = 0;
        arr[2] = 1;
        arr[3] = 0;
        arr[4] = 1;

        for (int i = 5; i <= 1001; i++) {
            if (arr[i - 1] == 1 && arr[i - 3] == 1 && arr[i - 4] == 1) {
                arr[i] = 0;
            } else {
                arr[i] = 1;
            }
        }

        if (arr[n] == 1) {
            System.out.println("SK");
        } else {
            System.out.println("CY");
        }

    }
}
