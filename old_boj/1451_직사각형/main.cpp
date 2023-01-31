#include <iostream>

using namespace std;
typedef long long ll;
string square[52] = { "", };
int sums[52][52] = { {0, }, };

ll cal(int x1, int y1, int x2, int y2) { // 네모칸의 위치, 시작점 1(x, y)는 1씩 적게 받는다
	return sums[y2][x2] - sums[y2][x1] - sums[y1][x2] + sums[y1][x1];
}

int main() {
	int n, m; cin >> n >> m;

	for (int i = 0; i < 52; i++)
		square[0] += '0';
	for (int i = 0; i < 52; i++)
		square[i] = square[0];

	for (int i = 1; i <= n; i++) {
		cin >> square[i];
		square[i] = '0' + square[i] + '0';

		for (int j = 1; j <= m; j++) 
			sums[i][j] = (int)(square[i][j] - '0');
	}

	for (int i = 1; i <= n; i++) 
		for (int j = 1; j <= m; j++) 
			sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + sums[i][j];// sums[i][j] == i, j칸까지의 합

	//i가 x축 j가 y축
	ll biggest_sum = 0LL;
	ll tester = 0LL;
	for (int j = 1; j < n; j++) 
		for (int i = 1; i < m; i++) {
			tester = cal(0, 0, i, j);
			tester *= cal(0, j, i, n);
			tester *= cal(i, 0, m, n);
			if (tester > biggest_sum) {
				biggest_sum = tester;
			}
			tester = cal(0, 0, i, j);
			tester *= cal(0, j, m, n);
			tester *= cal(i, 0, m, j);
			if (tester > biggest_sum) {
				biggest_sum = tester;
			}
		}

	for (int j = n; j == n; j++) // j 값 고정
		for (int i = 1; i < m - 1; i++) {
			//세로로 나누는 경우
			for (int i2 = i + 1; i2 < m; i2++) {
				tester = cal(0, 0, i, j);
				tester *= cal(i, 0, i2, n);
				tester *= cal(i2, 0, m, n);
				if (tester > biggest_sum) {
					biggest_sum = tester;
				}
			}
			//가로로 나누는 경우
			for (int j2 = 1; j2 < n; j2++) {
				tester = cal(0, 0, i, j);
				tester *= cal(i, 0, m, j2);
				tester *= cal(i, j2, m, n);
				if (tester > biggest_sum) {
					biggest_sum = tester;
				}
			}
		}
	for (int j = n; j == n; j++)  // 위와 같지만 가로로만 나눌 수 있는 경우
		for (int i = m - 1; i == m - 1; i++) 
			for (int j2 = 1; j2 < n; j2++) {
				tester = cal(0, 0, i, j);
				tester *= cal(i, 0, m, j2);
				tester *= cal(i, j2, m, n);
				if (tester > biggest_sum) {
					biggest_sum = tester;
				}
			}

	for (int i = m; i == m; i++)  // i값 고정
		for (int j = 1; j < n - 1; j++) {
			//세로로 나누는 경우
			for (int i2 = 1; i2 < m; i2++) {
				tester = cal(0, 0, i, j);
				tester *= cal(0, j, i2, n);
				tester *= cal(i2, j, m, n);
				if (tester > biggest_sum) {
					biggest_sum = tester;
				}
			}
			//가로로 나누는 경우
			for (int j2 = j + 1; j2 < n; j2++) {
				tester = cal(0, 0, i, j);
				tester *= cal(0, j, m, j2);
				tester *= cal(0, j2, m, n);
				if (tester > biggest_sum) {
					biggest_sum = tester;
				}
			}
		}
	for (int i = m; i == m; i++) // 위와 같지만 세로로만 나눌 수 있는 경우
		for (int j = n - 1; j == n - 1; j++) 
			for (int i2 = 1; i2 < m; i2++) {
				tester = cal(0, 0, i, j);
				tester *= cal(0, j, i2, n);
				tester *= cal(i2, j, m, n);
				if (tester > biggest_sum) {
					biggest_sum = tester;
				}
			}

	cout << biggest_sum;
}
