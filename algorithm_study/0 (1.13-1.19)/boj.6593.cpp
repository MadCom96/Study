// 진짜 신기한 문제... 중복해서 bfs에 넣는 것을 막아준다.

#include <iostream>
#include <queue>
using namespace std;

int dz[] = {1, -1, 0, 0, 0, 0};
int dy[] = {0, 0, 1, -1, 0, 0};
int dx[] = {0, 0, 0, 0, 1, -1};

char building[30][30][30] = {{{0, }, }, };
queue< pair< pair<int, int>, pair<int, int> > > bfs;

void append4(int& l, int& r, int& c, int t) {
    bfs.push(make_pair(make_pair(l, r), make_pair(c, t)));
}

int main() {
    while(1) {
        int L, R, C;
        cin >> L >> R >> C;

        if (L == 0 && R == 0 && C == 0)
            break;
        else {
            fill(&building[0][0][0], &building[29][29][30], 7);
            bfs = queue< pair< pair<int, int>, pair<int, int> > > ();
        }

        bool sNotFound = true;
        for (int l = 0; l < L; l++) {
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    cin >> building[l][r][c];
                    if (sNotFound && building[l][r][c] == 'S') {
                        sNotFound = false;
                        append4(l, r, c, 0);
                    }
                }
            }
        }
        int ans = -1;
        while (!bfs.empty()) {
            int z = bfs.front().first.first;
            int y = bfs.front().first.second;
            int x = bfs.front().second.first;
            int t = bfs.front().second.second;
            bfs.pop();
            
            if (building[z][y][x] == 'E') {
                ans = t;
                break;
            }

            for (int i = 0; i < 6; i++) {
                int zz = z + dz[i];
                int yy = y + dy[i];
                int xx = x + dx[i];

                if ((-1 < zz && zz < L) && (-1 < yy && yy < R) && (-1 < xx && xx < C)) {
                    if (building[zz][yy][xx] == '.') {
                        building[zz][yy][xx] = '#'; // 중복하여 넣기 방지
                        append4(zz, yy, xx, t + 1);
                    } else if (building[zz][yy][xx] == 'E') {
                        append4(zz, yy, xx, t + 1);
                    }
                }
            }
        }
        if (ans == -1)
            cout << "Trapped!\n";
        else
            cout << "Escaped in " << ans << " minute(s).\n";
    }
}