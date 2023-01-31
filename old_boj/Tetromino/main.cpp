#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

int xs[] = {0, 0, 1, 1, 0, 0};
int ys[] = {0, 1, 1, 0, 0, 1};

void show(vector<vector<int>> t, int size) {
  cout.setf(ios::right); 
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cout << setw(6) << t[i][j];
		}
		cout << endl;
	}
}

bool check(int size, int x, int y, vector<vector<int>>& t) { 
	for (int i = x; i < x + size; i++) {
		for (int j = y; j < y + size; j++) { 
			if (t[i][j] != 0) return false;
		} 
	} 
	return true; 
}

void sol(int size, int x, int y, vector<vector<int>>& t, int& cnt) { 
	cnt++; 
	int s = size / 2; 
  for(int i = 0; i < 4; i++){
    if(check(s, x + s * xs[i], y + s * ys[i], t))
      t[x + s - 1 * xs[i + 2]][y + s - 1 * ys[i + 2]] = cnt;
  }
	if (size == 2) return;
  for(int i = 0; i < 4; i++){
    sol(s, x + s * xs[i], y + s * ys[i], t, cnt);
  }
}


int main() {
	int k, x, y;
  cout << "배열 사이즈를 입력하시오.\n 2의 (입력)승 으로 크기가 설정됩니다. \n(최대입력 7)\n";
	cin >> k;
  cout << "빈칸의 위치를 x, y 순으로 입력하시오.\n 왼쪽 가장 아래가 1 1입니다.\n";
  cin >> x >> y;
	vector<int> tilex(128, 0);
	vector<vector<int>> tile(128, tilex);
	int size = pow(2, k);

	int tilename = 0;
	tile[size - y][x - 1] = -1;
	
	sol(size, 0, 0, tile, tilename);
	show(tile, size);
}