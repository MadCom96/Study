#include <iostream>
#include <vector>

using namespace std;

int min(int a, int b) {
	if (a > b) return b;
	else return a;
}
int main() {
	int n;
	cin >> n;
	
	vector<int> bigbang;
	int a = 0;
	int i = 1, j, sub;
	while (a < n) {
		a = 0;
		sub = 1;
		for (j = i; j <= 2 * i - 1; j++) {
			a += j;
			a -= sub++;
		}
		for (j = 2 * i - 2; j >= i; j--) {
			a += j;
			a -= sub--;
		}
		bigbang.push_back(a);
		i++;
	}
	int bigind = 1;
	vector<int> sol;
	sol.push_back(0); sol.push_back(1);
	for (int i = 2; i <= n; i++) {
		int mini = i;
		if (bigbang[bigind + 1] == i) {
			bigind++;
			mini = 1;
		}
		else {
			for (int j = bigind; j > 0; j--) {
				if (mini > sol[bigbang[j]] + sol[i - bigbang[j]]) {
					mini = sol[bigbang[j]] + sol[i - bigbang[j]];
				}
			}
		}
		sol.push_back(mini);
	}
	cout << sol[n];
}