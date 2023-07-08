package test;

import java.util.*;

public class Solution {
	static int n;
	static char[][] field;
	static int[][] nums;
	static boolean[][] checked;
	
	static int[] dy = {-1, -1, -1, 0, 1, 1, 1, 0};
	static int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1};
	
	public static boolean isin(int y, int x) {
		return 0 <= y && y < n && 0 <= x && x < n;
	}
	
	public static void numcheck() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (field[i][j] == '*') {
					for (int d = 0; d < 8; d++) {
						int yy = i + dy[d];
						int xx = j + dx[d];
						if(isin(yy, xx) && field[yy][xx] != '*') {
							nums[yy][xx] += 1;
						}
					}
				}
			}
		}
	}
	
	public static int counter() {
		int ans = 0;
		// 0먼저 체크 
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				if (checked[y][x] || field[y][x] == '*') continue;
				if (nums[y][x] == 0) {
					bfs(y, x);
					ans += 1;
				}
			}
		}
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				if (checked[y][x] || field[y][x] == '*') continue;
				ans += 1;
			}
		}
		return ans;
	}
	
	public static int bfs(int y, int x) {
		checked[y][x] = true;
		int ans = 1;
		
		Queue<int[]> q = new LinkedList<int[]>();
		q.offer(new int[] {y, x});
		while (!q.isEmpty()) {
			int[] now = q.poll();
			for (int d = 0; d < 8; d++) {
				int yy = now[0] + dy[d];
				int xx = now[1] + dx[d];
				if (!isin(yy, xx) || field[yy][xx] == '*' || checked[yy][xx]) continue;
				if (nums[yy][xx] == 0)
					q.offer(new int[] {yy, xx});
				ans += 1;
				checked[yy][xx] = true;
			}
		}
		return ans;
	}
	
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int TC = sc.nextInt();
		for (int test_case = 1; test_case <= TC; test_case++) {
			n = sc.nextInt();
			field = new char[n][n];
			nums = new int[n][n];
			checked = new boolean[n][n];
			
			for (int i = 0; i < n; i++) {
				String s = sc.next();
				for (int j = 0; j < n; j++) {
					field[i][j] = s.charAt(j);
				}
			}
			
			numcheck();
			int ans = counter();
			System.out.printf("#%d %d\n", test_case, ans);
		}
	}
}