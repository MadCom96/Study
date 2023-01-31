#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

class myIntStack{
	vector<int> storage;
	int size;
	int top;
public:
	myIntStack(){
		top = 0;
	}
	void init(int n){
		size = n;
		storage = vector<int>(size);
	}

	int pop(){
		int ans = storage[--top];
		storage[top] = 0;
		return ans;
	}
	void push(int a){
		storage[top] = a;
		top += 1;
	}
	// 실수없는 프로그램이니까 예외처리따위 하지않는다.
	int layerValue(int i){
		if(i > top)
			return 0;
		else
			return storage[i];
	}
};

class simulator{
	myIntStack a;
	myIntStack b;
	myIntStack c;
	myIntStack* from;
	myIntStack* to;
	int size;
	int width;
	string format;

public:
	simulator(int size){
		a.init(size);
		b.init(size);
		c.init(size);
		this->size = size;
		width = log10(size);
		for (int i = 0; i < size; i++){
			a.push(size - i);
		}
	}

	void move(int fromInt, int toInt){
		if (fromInt == 1){
			from = &a;
		}else if (fromInt == 2){
			from = &b;
		}else if (fromInt == 3){
			from = &c;
		}
		
		if (toInt == 1){
			to = &a;
		}else if (toInt == 2){
			to = &b;
		}else if (toInt == 3){
			to = &c;
		}

		to->push(from->pop());
	}
	void show(){
		for(int i = size - 1; i >= 0; i--){
			cout << setw(width) << a.layerValue(i);
			cout << " | ";
			cout << setw(width) <<  b.layerValue(i);
			cout << " | ";
			cout << setw(width) <<  c.layerValue(i);
			cout << "\n";
		}
		cout << "\n";
	}
};

void hanoi(int n, int from, int extra, int to, simulator& s){
	if(n == 1) {
		cout << n << "블록: " << from << "->" << to << endl;
		s.move(from, to);
		s.show();
	}
	else {
		hanoi(n - 1, from, to, extra, s);
		cout << n << "블록: " << from << "->" << to << endl;
		s.move(from, to);
		s.show();
		hanoi(n - 1, extra, from, to, s);
	}
}

int main(){
	int n; cin >> n;
	simulator s = simulator(n);
	s.show();
	hanoi(n, 1, 2, 3, s);
}
