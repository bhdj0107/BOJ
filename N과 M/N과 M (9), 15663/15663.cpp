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

// �׳� �ŵ����� �Լ�
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
	// M�� ��ŭ ���� ��� Ż�� �ϴ� ����
	if (D == M) {
		int temp = 0;

		// �տ���, ������ ��� ����� �� ��ŭ�� ũ�⸦ ���� vst �迭�� �̸� ������ �ξ���.
		// �̹� ���� ����� ���� ������ ���� ����Ѵ�.

		// �Ʒ� for���� ������ �Ǹ�, �ߺ� �Ǵ� ���� ���� ���� temp ���� ���´�.
		for (int i = 0; i < M; i++) {
			temp += my_pow(8, i) * d_exp[str[i]];
		}

		// �̶� vst[temp] ���� �����Ͽ� true �� �ƴ� ���, true�� �ٲپ� �ߺ� ó���� �ϰ� ����Ѵ�. 
		if (!vst[temp]) {
			vst[temp] = true;
			for (int i = 0; i < M; i++)
				printf("%d ", list[str[i]]);
			printf("\n");
		}

		return;
	}


	// M�� ���� �� ���� ���, for �� �ȿ��� ������� �̰� ��� �Լ��� ������ ��, �����Ѵ�.
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

	// ���� N���� ���� ������ list �迭�� ����
	for (int i = 1; i <= N; i++) {
		scanf("%d", &list[i]);
	}

	// list ������������
	for (int i = 1; i <= N - 1; i++) {
		for (int j = i + 1; j <= N; j++) {
			if (list[j] < list[i]) {
				swap(list[i], list[j]);
			}
		}
	}


	// ���߿� ���� ���� �����ϱ� ����, �� ������ ������ ����
	// ��) N���� ���� ���� ���� {10, 15, 15, 20, 20, 20}
	// �� ������ ���, d_exp�� {0, 1, 1, 2, 2, 2}
	for (int i = 2; i <= N; i++) {
		if (list[i] != list[i - 1])
			d_exp[i] = d_exp[i - 1] + 1;
		else
			d_exp[i] = d_exp[i - 1];
	}

	// Ž�� ����
	dfs(0);

	return 0;
}