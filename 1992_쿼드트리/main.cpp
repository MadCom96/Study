#include <iostream>

using namespace std;

char qt[64][64] = { {0,}, };

bool check(int y, int x, int size) {
	char standard = qt[y][x];
	for (int i = 0; i < size; i++) 
		for (int j = 0; j < size; j++) 
			if (standard != qt[y + i][x + j])
				return false;
	return true;
}

void sol(int y, int x, int size) {
	if (check(y, x, size)) {
		cout << qt[y][x];
	}
	else {
		cout << '(';
		size /= 2;
		sol(y, x, size);
		sol(y, x + size, size);
		sol(y + size, x, size);
		sol(y + size, x + size, size);
		cout << ')';
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n; cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> qt[i][j];

	sol(0, 0, n);
}