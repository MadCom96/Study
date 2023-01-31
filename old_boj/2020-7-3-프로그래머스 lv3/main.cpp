#include <iostream>
//제출부분
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class trio {
public:
	string first;
	int second;
	int third;//고유번호
	
};
trio make_trio(string f, int s, int t) {
	trio a;
	a.first = f;
	a.second = s;
	a.third = t;
	return a;
}

bool comp1(pair<string, int> a, pair<string, int> b) {
	return a.second > b.second;
}
bool comp2(trio a, trio b) {
	return a.second > b.second;
}

void push1(vector<pair<string, int>>& g_rank, string s, int a) {
	bool flag = false;
	for (int i = 0; i < g_rank.size(); i++) {
		if (g_rank[i].first == s) {
			flag = true;
			g_rank[i].second += a;
			break;
		}
	}

	if (flag) return;
	else {
		g_rank.push_back(make_pair(s, a));
		return;
	}
}
void push2(vector<trio>& g_rank, string s, int a, int i) {
	g_rank.push_back(make_trio(s, a, i));
}

vector<int> solution(vector<string> genres, vector<int> plays) {
	vector<int> answer;
	vector<pair<string, int>> rank;
	vector<trio> totaldata;
	for (int i = 0; i < plays.size(); i++) {
		push1(rank, genres[i], plays[i]);
		push2(totaldata, genres[i], plays[i], i);
	}
	sort(rank.begin(), rank.end(), comp1);
	sort(totaldata.begin(), totaldata.end(), comp2);

	for (int i = 0; i < rank.size(); i++) {
		int cnt = 2;
		for (int j = 0; j < totaldata.size() && cnt; j++) {
			if (totaldata[j].first == rank[i].first) {
				cnt--;
				answer.push_back(totaldata[j].third);
			}
		}
	}

	return answer;
}

//제출부분 끝
int main() {
	solution({ "classic", "pop", "classic" ,"classic" ,"pop" }, { 500, 600, 150, 800, 2500 });
}