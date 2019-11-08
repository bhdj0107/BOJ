#include <iostream>
#include <queue>

using namespace std;
bool change[1001][1001];
int check[1001];
int a, b;
int N, M;

queue<pair<int, int>> q;
int main() {
	scanf("%d %d", &a, &b);
	scanf("%d %d", &N, &M);
	int t1, t2;
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &t1, &t2);
		change[t1][t2] = true;
		change[t2][t1] = true;
	}
	for (int i = 1; i <= N; i++) {
		if (change[a][i]) {
			q.push(make_pair(a, i));
		}
	}
	check[a] = 1;
	while (!q.empty()) {
		int n1 = q.front().first;
		int n2 = q.front().second;
		q.pop();
		if (check[n2] != 0)
			continue;
		for (int i = 1; i <= N; i++) {
			if (change[n2][i]) {
				check[n2] = check[n1] + 1;
				q.push(make_pair(n2, i));
			}
		}
	}

	check[b] == 0 ? cout << -1 : cout << check[b] - 1;
}