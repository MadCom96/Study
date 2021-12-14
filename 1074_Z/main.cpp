#include <iostream>
using namespace std;
int r, c;
int Zx[] = { 0, 1, 0, 1 };
int Zy[] = { 0, 0, 1, 1 };

void DaC(int size, int x, int y, bool isin, int& cnt) {
	if (!isin) cnt += size * size;
	else {
		if (size == 1) {
			if (x == r && y == c) {
				cout << cnt;
				exit(0);
			}
			else
				cnt += 1;
		}
		else {
			size /= 2;
			int goal = 0;
			if (x <= r && x + size > r) goal += 0;
			else goal += 1;
			if (y <= c && y + size > c) goal += 0;
			else goal += 2;
			for (int i = 0; i < 4; i++) {
				if (i == goal)
					DaC(size, x + Zx[i] * size, y + Zy[i] * size, true, cnt);
				else
					DaC(size, x + Zx[i] * size, y + Zy[i] * size, false, cnt);
			}
		}
	}
}

int main() {
	int N;
	cin >> N >> c >> r;
	int size = 1;
	for (int i = 0; i < N; i++) {
		size *= 2;
	}
	int cnt = 0;
	DaC(size, 0, 0, true, cnt);
}