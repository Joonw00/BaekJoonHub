import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();	
		int m = sc.nextInt();
		int r = sc.nextInt();
		int[][] arr = new int[n][m];
		for(int row =0; row<n; row++){
			for(int column = 0; column<m; column++){
				arr[row][column] = sc.nextInt();
			}
		}

		int count = Math.min(n, m) / 2;

		for(int layer=0; layer<count; layer ++){
			int cycle = (n-layer*2) *2 + (m-layer*2) * 2 -4;
			int totalRotate = r % cycle;
			for(int rotate = 0; rotate<totalRotate; rotate++){
				int temp = arr[layer][layer];
				// 상단
				for(int column = layer; column<m-1-layer; column++){
					arr[layer][column] = arr[layer][column+1];
				}
				// 우측
				for(int row = layer; row<n-1-layer; row++){
					arr[row][m-layer-1] = arr[row+1][m-layer-1];
				}

				// 하단
				for(int column = m-1-layer; column>layer; column--){
					arr[n-layer-1][column] = arr[n-layer-1][column-1];
				}


				// 좌측
				for(int row = n-layer-1; row>layer; row--){
					arr[row][layer] = arr[row-1][layer];
					if(row == layer+1) arr[row][layer] = temp; // 시작점은 따로..... 1줄이면 쓸 일 없을 수도ㅛ.
				}
			}
		}
		for(int row = 0; row<n; row++){
			for(int column=0;column<m;column++){
				System.out.print(arr[row][column] + " ");
			}
			System.out.println();
		}
	}
}
