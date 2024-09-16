import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int[] balloon = new int[N];
        for (int i = 0; i < N; i++) {
            balloon[i] = scanner.nextInt();
        }
        int[] done = new int[N];
        int nowIdx = 0;
        for (int i = 0; i < N - 1; i++) {
            done[nowIdx] = 1; // 현재 풍선을 터트리고
            System.out.print((nowIdx + 1) + " ");
            int temp = balloon[nowIdx];
            for (int j = 0; j < Math.abs(temp); j++) { // 풍선의 숫자 만큼 이동, j로 카운트
                if (temp > 0) {
                    nowIdx += 1;
                    if (nowIdx >= N) {
                        nowIdx -= N;
                    }
                    while (done[nowIdx] == 1) {
                        nowIdx += 1;
                        if (nowIdx >= N) {
                            nowIdx -= N;
                        }
                    }
                }
                if (temp < 0) {
                    nowIdx -= 1;
                    if (nowIdx < 0) {
                        nowIdx += N;
                    }
                    while (done[nowIdx] == 1) {
                        nowIdx -= 1;
                        if (nowIdx < 0) {
                            nowIdx += N;
                        }
                    }
                }
            }

        }

        System.out.print(nowIdx + 1);

    }
}
