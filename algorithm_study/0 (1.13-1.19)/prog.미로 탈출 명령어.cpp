#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#define SHORTEST(x, y, r, c) (abs((x)-(r))+abs((y)-(c)))

using namespace std;

string shortestPath(int x, int y, int r, int c) {
    string sp = "";
    int repeat;
    if (r > x) {
        repeat = r - x;
        while (repeat--){
            sp = sp + 'd';
        }
    }
    if (y > c) {
        repeat = y - c;
        while (repeat--){
            sp = sp + 'l';
        }
    }
    if (y < c) {
        repeat = c - y;
        while (repeat--){
            sp = sp + 'r';
        }
    }
    if (r < x) {
        repeat = x - r;
        while (repeat--){
            sp = sp + 'u';
        }
    }
    return sp;
}

string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";

// 1. k - 최단거리 가 2의 배수가 아니면 impossible
//  1.1 k - 최단거리가 음수여도 impossible
    int shortestL = abs(x - r) + abs(y - c);
    if (k - SHORTEST(x, y, r, c) < 0 || (k - SHORTEST(x, y, r, c)) % 2 == 1)
        return "impossible";

// 2. 딴길 = (k - 최단거리) / 2
// 3. 출발지점의 가장 아래 죄표(1)로 이동 - if k == 최단거리: 목표지점으로 이동
    while(1){
        if (x + 1 > n)
            break;
        ++x;
        answer = answer + 'd';
        --k;
        if (k == SHORTEST(x, y, r, c))
            return answer + shortestPath(x, y, r, c);
    }
    
// 4. (1)에서 가장 왼쪽 좌표(2)로 이동 - if k == 최단거리: 목표지점으로 이동
    while(1) {
        if (y - 1 < 1)
            break;
        --y;
        answer = answer + 'l';
        --k;
        if (k == SHORTEST(x, y, r, c))
            return answer + shortestPath(x, y, r, c);
    }

// 5. (2)에서 rl 반복. (2보다 항상 가로가 길어서 예외 없음). - if k == 최단거리: 목표지점으로 이동.
    while(1) {
        answer = answer + "rl";
        k -= 2;
        if (k == SHORTEST(x, y, r, c))
            return answer + shortestPath(x, y, r, c);
    }
    return answer;
}


int main() {
    // cout << solution(23, 38, 3, 17, 20, 2, 1692) << endl;
    cout << solution(3, 4, 2, 3, 3, 1, 5) << endl;
    // cout << solution(6, 10, 4, 6, 4, 9, 1786) << endl;
    // cout << solution(6, 47, 6, 24, 3, 9, 1176) << endl;
    // cout << solution(6, 30, 2, 24, 5, 22, 1759) << endl;
    // cout << solution(42, 16, 19, 10, 22, 14, 1942) << endl;
    // cout << solution(40, 22, 29, 3, 27, 12, 374) << endl;
    // cout << solution(27, 14, 8, 13, 4, 6, 2419) << endl;
    // cout << solution(17, 36, 3, 10, 1, 8, 1294) << endl;
    // cout << solution(3, 10, 1, 7, 3, 1, 1589) << endl;
}
