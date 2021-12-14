#include <iostream>
#include <vector>
#include <random>

#define SWAP(a, b, temp) temp = a, a = b, b = temp
using namespace std;

void show(int* a, int n, vector<int> what) {
	int wi = 0;
	for (int i = 0; i < n; i++) {
		if (wi < what.size() && i == what[wi]) {
			cout << '[' << a[i] << ']' << ' ';
			wi++;
		}
		else {
			cout << a[i] << ' ';
		}
	}
	cout << endl;
}

vector<int> mapper(int start, int h, int end) {
	vector<int> ans;
	while (start < end) {
		ans.push_back(start);
		start += h;
	}
	return ans;
}

void insertsort(int* a, vector<int> mapped) {
	int temp;
	for (int i = 0; i < mapped.size(); i++) {
		for (int j = i; j > 0; j--) {
			if (a[mapped[j]] < a[mapped[j - 1]]) {
				SWAP(a[mapped[j]], a[mapped[j - 1]], temp);
			}
		}
	}
}

void shellsort(int* a, int n, int h_th) {
	int h = 1;
	while (h <= n) h *= h_th;
	h /= h_th;

	while (h > 0) {
		cout << h << "-th insert sort \n";
		for (int i = 0; i < h; i++) {
			insertsort(a, mapper(i, h, n));
			show(a, n, mapper(i, h, n));
		}
		cout << endl;
		h /= h_th;
	}
}

int main() {
	random_device rd;
	mt19937 gen(rd());

	uniform_int_distribution<int> size(10, 10);//배열 사이즈
	uniform_int_distribution<int> dis(0, 99);//들어가는 수 랜덤으로 뽑기
	uniform_int_distribution<int> th(2, 2);//간격(제곱수로 사용)

	int a[20] = { 0, };
	while (1) {
		int S = size(gen);
		int H = th(gen);
		for (int i = 0; i < S; i++) {
			a[i] = dis(gen);
		}
		cout << "size : " << S << ", " << H << "-th\n";
		show(a, S, {});
		shellsort(a, S, H);
    cout << "end?  N(enter 0), Y(else)_\n";
		cin >> S;
		if (S == 0) {
			break;
		}
	}
}