#include <iostream>
#include <vector>
using namespace std;

const int MAX = 9;
int list[MAX];
int str[MAX];
bool* vst;
bool ch[MAX];
int N, M;

unsigned long long my_pow(unsigned long long base, int exp) { 
	unsigned long long res = 1; 
	while (exp) { 
		if (exp & 1) res *= base; 
		exp >>= 1; 
		base *= base; 
	} 
	return res; 
}

void dfs(int D) {
	if (D == M) {
		for (int i = 0; i < M; i++)
			printf("%d ", list[str[i]]);
		printf("\n");
		return;
	}
	for (int i = 1; i <= N; i++) {
		if (!ch[i]) {
			ch[i] = true;
			str[D] = i;
			dfs(D + 1);
			ch[i] = false;
		} 
	}
	
}


int main() {
	scanf("%d %d",&N, &M);
	vst = new bool[my_pow(MAX, M)];
	for (int i = 1; i <= N; i++) {
		scanf("%d", &list[i]);
	}
	for (int i = 1; i <= N - 1; i++) {
		for (int j = i + 1; j <= N; j++) {
			if (list[j] < list[i]) {
				swap(list[i], list[j]);
			}
		}
	}
	dfs(0);
	delete[] vst;
	return 0;
}