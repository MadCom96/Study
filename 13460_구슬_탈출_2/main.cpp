#include <iostream>
#include <vector>
#include <queue>
#define firstMoved board[first->y + diry[dir]][first->x + dirx[dir]]
#define secondMoved board[second->y + diry[dir]][second->x + dirx[dir]]
using namespace std;
typedef struct {
	int x;
	int y;
} at;

string board[10] = { "", };
// up left down right
int dirx[] = { 0, -1, 0, 1 }; 
int diry[] = { -1, 0, 1, 0 };
// simulation recording
queue<at> Rat;
queue<at> Bat;
queue<int> len;

int move(at R, at B, int dir) {
	bool stopped1 = false;
	bool stopped2 = false;
	at* first = &R;
	at* second = &B;
	if (dir == 0) {
		if (R.x == B.x && B.y < R.y) {
			first = &B;
			second = &R;
		}
	}
	else if (dir == 1) {
		if (R.y == B.y && B.x < R.x) {
			first = &B;
			second = &R;
		}
	}
	else if (dir == 2) {
		if (R.x == B.x && B.y > R.y) {
			first = &B;
			second = &R;
		}
	}
	else if (dir == 3) {
		if (R.y == B.y && B.x > R.x) {
			first = &B;
			second = &R;
		}

	}
		
	while (true) { // first move
		if (firstMoved == 'O') {
			first->x += dirx[dir];
			first->y += diry[dir];
			stopped1 = true;
			break;
		}
		if (firstMoved == '#') {
			stopped1 = true;
			break;
		}
		first->x += dirx[dir];
		first->y += diry[dir];
	}
	while (true) { // second move
		if (secondMoved == 'O') {
			second->x += dirx[dir];
			second->y += diry[dir];
			stopped2 = true;
			break;
		}
		if (secondMoved == '#') {
			stopped2 = true;
			break;
		}
		if (second->x + dirx[dir] == first->x && second->y + diry[dir] == first->y) {
			stopped2 = true;
			break;
		}
		second->x += dirx[dir];
		second->y += diry[dir];
	
	}
	//both stoepped
	if (board[B.y][B.x] == 'O') // if b's out, failed whatever
		return -1;
	if (board[R.y][R.x] == 'O') // if r's out while b's not, successed whatever
		return 1;
	// both are not escaped, keep going
	Rat.push(R);
	Bat.push(B);
	return 0;
}

int main() {
	int n, m; // vertical, horizontal,, 3~10
	cin >> n >> m;
	for (int i = 0; i < n; i++) 
		cin >> board[i];

	at R{ 0, 0 };
	at B{ 0, 0 };

	//find R, B 
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < m; j++) {
			if (board[i][j] == '#' || board[i][j] == '.') {
				continue;
			}
			else if (board[i][j] == 'R') {
				R.x = j;
				R.y = i;
				board[i][j] = '.';
			}
			else if (board[i][j] == 'B') {
				B.x = j;
				B.y = i;
				board[i][j] = '.';
			}
		}

	int result = 0;
	int l;
	Rat.push(R);
	Bat.push(B);
	len.push(0);
	while (!Rat.empty()) {
		R = Rat.front(); Rat.pop();
		B = Bat.front(); Bat.pop();
		l = len.front(); len.pop();
		l += 1;
		if (l > 10) {
			cout << -1;
			return 0;
		}
		for (int i = 0; i < 4; i++) {
			int result = move(R, B, i);
			if (result == 1) {
				cout << l;
				return 0;
			}
			if (result == 0) {
				len.push(l);
			}
		}
	}
}