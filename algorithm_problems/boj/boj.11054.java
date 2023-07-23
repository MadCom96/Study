import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	static int n;
	static int[] nums;
	static int[] dp;
	static int[] dpreversed;
	static int[] lis;
	
	static int lower_bound(int num, int size) {
		// 찾는 수보다 작은 
		int l = 0;
		// 찾는 수보다 크거나 같은 
		int r = size - 1;
		int m = (l + r) / 2;
		while (l != r) {
			m = (l + r) / 2;
			if (num > lis[m]) {
				l = m + 1;
			}
			else {
				r = m;
			}
		}
		return r;
	}
	
//	1 2 4 5 search 3 -> 1 2 3 5
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		nums = new int[n];
		
		dp = new int[n];
		dpreversed = new int[n];
		
		for (int i = 0; i < n; i++) {
			nums[i] = sc.nextInt();
		}
				
//		LIS 수행
		lis = new int[n];
		int idx = 0;
		lis[idx++] = nums[0];
		dp[0] = 1;

		for (int i = 1; i < n; i++) {
			if (nums[i] > lis[idx - 1]) {
				lis[idx++] = nums[i];
			}

			else {
				int tmp = lower_bound(nums[i], idx);
				lis[tmp] = nums[i];
			}
			dp[i] = idx;
		}
//		LIS 배열 뒤에서부터 수행
		lis = new int[n];
		idx = 0;
		lis[idx++] = nums[n - 1];
		dpreversed[n - 1] = 1;
		for (int i = n - 2; i >= 0; i--) {
			if(nums[i] > lis[idx - 1]) {
				lis[idx++] = nums[i];
			}
			else {
				int tmp = lower_bound(nums[i], idx);
				lis[tmp] = nums[i];
			}
			dpreversed[i] = idx;
		}

		int longest = 0;
		for (int i = 0; i < n; i++) {
			int len = dp[i] + dpreversed[i] - 1;
			if (len > longest)
				longest = len;
		}
		System.out.println(longest);
	}

}
