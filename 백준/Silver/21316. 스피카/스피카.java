import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int[][] star = new int[12][2];

        List<List<Integer>> near = new ArrayList<>();
        for (int i = 0; i < 13; i++) {
            near.add(new ArrayList<>());
        }
        for (int i = 0; i < 12; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            star[i][0] = x;
            star[i][1] = y;

            near.get(x).add(y);
            near.get(y).add(x);
        }

        int[] line = new int[12];
        for (int i = 0; i < 12; i++) {
            line[star[i][0] - 1] += 1;
            line[star[i][1] - 1] += 1;
        }

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 12; i++) {
            if (line[i] == 3) {
                list.add(i + 1);
            }
        }

        for (int i = 0; i < list.size(); i++) {
            int t = list.get(i);
            // t별과 연결된 별 3개를 찾음
            List<Integer> connectedStars = near.get(t);

            // 연결된 벼를의 선분 수를 합함
            int nearLine = 0;
            for (int j = 0; j < connectedStars.size(); j++) {
                nearLine += line[connectedStars.get(j) - 1];
            }

            // 합이 6이면 t출력
            if (nearLine == 6) {
                System.out.println(t);
            }
        }

    }
}
