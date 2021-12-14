#include <iostream>
#include <math.h>
#include <cstdlib>

#define SWAP(x, y, temp) ((temp) = (x), (x) = (y), (y) = (temp))

using namespace std;
int SIZE;
bool fc[1000] = {false,};

void print(int* list){
  for(int i = 0; i < SIZE; i++){
    if (fc[i]) cout << '(' << list[i] << ") ";
    else cout << list[i] << ' ';
  }
  cout << endl << endl;
}

int partition(int* list, int begin, int end){
  int L = begin;
  int R = end;
  int P = rand() % (end - begin + 1);
  int temp;
  P += begin;
  cout << "피봇 " << list[P] << endl;
  while(L < R){
    while(L < end && list[L] <= list[P]) {
      ++L;
    }
    while(R >= L && list[R] > list[P]){
      --R;
    }
    if (L < R){
      cout << list[L]<<' '<< list[R]<<"교환\n";
      if(R == P){ P = L; }
      SWAP(list[L], list[R], temp);
      print(list);
    }
  }
  cout << "R과 피봇 교환, R = "<< list[R] << endl;
  SWAP(list[R], list[P], temp);
  return R;
}

// 퀵 정렬
void quick_sort(int* list, int begin, int end){
  if (begin < end){
    int q = partition(list, begin, end);
    fc[q] = true;
    print(list);
    quick_sort(list, begin, q - 1);
    quick_sort(list, q + 1, end);
  }
}

int main(){
  srand(time(NULL));
  
  cout << "1000 이하의 사이즈 입력 >> ";
  cin >> SIZE;
  
  bool numcheck[1001] = {false, };
  int list[1000] = {0, };
  
  for(int i = 0; i < SIZE; i++){
    while(1){
      int a = rand() % SIZE + 1;
      if (!numcheck[a]) {
        numcheck[a] = true;
        list[i] = a;
        break;
      }
    }
  }
  print(list);
  quick_sort(list, 0, SIZE - 1);
  
  for(int i = 0; i < SIZE; i++){
    if (list[i] != i + 1){
      cout << "실패!";
      return 0;
    }
  }
  cout << "성공!";
  return 0;
}