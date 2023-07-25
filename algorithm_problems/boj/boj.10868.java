package algo;

import java.util.Scanner;

public class Main {
	static int n, m;
	static int[] arr;
	static int[] tree;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		
		arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		tree = new int[n * 4];
		init(0, n - 1, 1);
		
		while (m-- > 0) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			System.out.println(getMin(0, n - 1, 1, a - 1, b - 1));
		}
	}
	
	static int init(int start, int end, int node) {
		if(start == end) return tree[node] = arr[start];
		int mid = (start + end) / 2;

		return tree[node] = Math.min(init(start, mid, node * 2),
				init(mid + 1, end, node * 2 + 1));
	}
	
	static int getMin(int start, int end, int node, int left, int right) {
		if (left > end || right < start) return Integer.MAX_VALUE;
		if (left <= start && end <= right) return tree[node];
		int mid = (start + end) / 2;
		return Math.min(
				getMin(start, mid, node * 2, left, right),
				getMin(mid + 1, end, node * 2 + 1, left, right));
		
	}
}