package test;

import java.util.*;

public class Solution {
	static int n;
	static int[][] map;
	static boolean[][] visited;
	
	static int[] dy = {0, 0, 1, -1};
	static int[] dx = {1, -1, 0, 0};
	
	static int[] sp;
	static int[] ep;
	
	public static int bfs() {
		Queue<int[]> q = new LinkedList<int[]>();
		q.offer(sp);
		visited[sp[0]][sp[1]] = true;
		
		int time = 0;
		while (!q.isEmpty()) {
			int size = q.size();
			while(size-- != 0) {
				int[] now = q.poll();
				for (int d = 0; d < 4; d++) {
					int yy = now[0] + dy[d];
					int xx = now[1] + dx[d];
					if (!isin(yy,xx)) continue;
					if (yy == ep[0] && xx == ep[1]) return time + 1;
					if (visited[yy][xx]) continue;
					
					if (map[yy][xx] == 1) continue;
					else if (map[yy][xx] == 2 && (time+1) % 3 != 0) {
						q.offer(now.clone());
					}
					else {
						q.offer(new int[] {yy, xx});
						visited[yy][xx] = true;
						// 왜 여기만 visited?
					}
				}
			}
			++time;
		}
		return -1;
	}
	
	public static boolean isin(int y, int x) {
		return 0 <= y && y < n && 0 <= x && x < n;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int TC = sc.nextInt();
		for (int test_case = 0; test_case < TC; test_case++) {
			n = sc.nextInt();
			map = new int[n][n];
			visited = new boolean[n][n];
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			sp = new int[2];
			sp[0] = sc.nextInt();
			sp[1] = sc.nextInt();
			
			ep = new int[2];
			ep[0] = sc.nextInt();
			ep[1] = sc.nextInt();
			
			int ans = bfs();
			System.out.printf("#%d %d\n", test_case + 1, ans);
		}
	}
}