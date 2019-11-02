#include <iostream>
#include <vector>
using namespace std;

const int MAX = 9;
int d_exp[MAX];
int list[MAX];
int str[MAX] = { 0, };
bool vst[16777216];
bool ch[MAX];
int N, M;

// 그냥 거듭제곱 함수
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
	// M개 만큼 뽑은 경우 탈출 하는 조건
	if (D == M) {
		int temp = 0;

		// 앞에서, 가능한 모든 경우의 수 만큼의 크기를 가진 vst 배열을 미리 선언해 두었다.
		// 이미 나온 경우의 수는 다음과 같이 계산한다.

		// 아래 for문을 돌리게 되면, 중복 되는 경우는 서로 같은 temp 값을 갖는다.
		for (int i = 0; i < M; i++) {
			temp += my_pow(8, i) * d_exp[str[i]];
		}

		// 이때 vst[temp] 값에 접근하여 true 가 아닐 경우, true로 바꾸어 중복 처리를 하고 출력한다. 
		if (!vst[temp]) {
			vst[temp] = true;
			for (int i = 0; i < M; i++)
				printf("%d ", list[str[i]]);
			printf("\n");
		}

		return;
	}


	// M개 보다 덜 뽑은 경우, for 문 안에서 순서대로 뽑고 재귀 함수로 실행한 뒤, 복원한다.
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

	scanf("%d %d", &N, &M);

	// 이후 N개의 정수 값을을 list 배열에 저장
	for (int i = 1; i <= N; i++) {
		scanf("%d", &list[i]);
	}

	// list 오름차순정렬
	for (int i = 1; i <= N - 1; i++) {
		for (int j = i + 1; j <= N; j++) {
			if (list[j] < list[i]) {
				swap(list[i], list[j]);
			}
		}
	}


	// 나중에 동일 값을 구분하기 위해, 각 숫자의 제곱수 설정
	// 예) N개의 정수 값이 각각 {10, 15, 15, 20, 20, 20}
	// 이 들어왔을 경우, d_exp는 {0, 1, 1, 2, 2, 2}
	for (int i = 2; i <= N; i++) {
		if (list[i] != list[i - 1])
			d_exp[i] = d_exp[i - 1] + 1;
		else
			d_exp[i] = d_exp[i - 1];
	}

	// 탐색 시작
	dfs(0);

	return 0;
}