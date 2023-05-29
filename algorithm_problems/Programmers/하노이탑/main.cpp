#include <iostream>
#include <string>
#include <vector>

using namespace std;
void hanoi(int n, int start, int work, int target, vector<vector<int>>& answer) {
	if (n == 1) {
		vector<int> a(2);
		a[0] = start;
		a[1] = target;
    cout << n <<"블록 : " << start << " -> " << target << endl;
		answer.push_back(a);
	}
	else {
		hanoi(n - 1, start, target, work, answer);
		vector<int> a(2);
		a[0] = start;
		a[1] = target;
    cout << n <<"블록 : " << start << " -> " << target << endl;
		answer.push_back(a);
		hanoi(n - 1, work, start, target, answer);
	}
}
vector<vector<int>> solution(int n) {
	vector<vector<int>> answer;
	hanoi(n, 1, 2, 3, answer);
	return answer;
}

int main() {
	int n; cin >> n;
	solution(n);
}