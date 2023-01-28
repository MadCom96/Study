#include <iostream>
#include <iomanip> // setw
#include <algorithm> // max
#include <cmath> // log10()

#define endl '\n'

using namespace std;

int cells[50][5] = {{0, }, };
int startNum[5001] = {1, };
int sNcheck = 0;
int highestNum = 0;

int start_number_square(int nth_sq){
    if (sNcheck < nth_sq) {
        int n_th_odd;
        for (sNcheck += 1; sNcheck <= nth_sq; ++sNcheck) {
            n_th_odd = 1 + 2 * (sNcheck - 1);
            startNum[sNcheck] = n_th_odd * n_th_odd + 1;
        }
        --sNcheck;
    }
    return startNum[nth_sq];
}

int fillCell(int r, int c) {
    int n_th_square = max(abs(r), abs(c));

    int ans = start_number_square(n_th_square);

    int length_line = n_th_square * 2;
    int n_th_line = -1;
    if (c == n_th_square && r != n_th_square)
        n_th_line = 0;
    else if (r == -n_th_square && c != n_th_square)
        n_th_line = 1;
    else if (c == -n_th_square && r != -n_th_square)
        n_th_line = 2;
    else if (r == n_th_square && c != -n_th_square)
        n_th_line = 3;
    
    ans += length_line * n_th_line;
    switch (n_th_line)
    {
    case 0:
        ans += (n_th_square - 1) - r;
        break;
    case 1:
        ans += (n_th_square - 1) - c;
        break;
    case 2:
        ans += r - (-n_th_square + 1);
        break;
    case 3:
        ans += c - (-n_th_square + 1);
        break;
    default:
        break;
    }

    if (highestNum < ans)
        highestNum = ans;
    return ans;
}

int main() {
    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    for (int r = r1; r <= r2; r++) {
        for (int c = c1; c <= c2; c++) {
            cells[r-r1][c-c1] = fillCell(r, c);
        }
    }
    int leng = log10(highestNum);
    for (int r = r1; r <= r2; r++) {
        for (int c = c1; c <= c2; c++) {
            cout << setw(leng+1) << cells[r-r1][c-c1] << ' ';
        }
        cout << endl;
    }
}