// 수열 정렬
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void printV(vector<int> a){
    for (int i = 0; i < a.size(); i++){
        cout << a[i] << ' ';
    }
    cout << '\n';
}

int main() {
    int n;
    vector<int> a;
    vector< pair<int, int> > pairs;
    
    cin >> n;
    a.resize(n);
    pairs.resize(n);
    
    for (int i = 0; i < n; i++){
        cin >> a[i];
        pairs[i] = make_pair(a[i], i);
    }
    
    sort(pairs.begin(), pairs.end());
    
    vector<int> ans(n);
    for (int i = 0; i < n; i++){
        ans[pairs[i].second] = i;
    }
    
    printV(ans);
}