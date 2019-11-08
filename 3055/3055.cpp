#include <iostream>
#include <queue>

using namespace std;
int R, C;
char field[50][50];
int water[50][50];
int vst[50][50];
int x, y;


struct pos {
	int x;
	int y;
};

struct wat {
	int x;
	int y;
	int t;
};

queue<wat> q;

pos Dp, Sp;

void water_bfs() {
	while (!q.empty()) {
		int tx = q.front().x;
		int ty = q.front().y;
		int tt = q.front().t;
		q.pop();

		if (tx < 0 || tx >= C || ty < 0 || ty >= R)
			continue;
		if (water[ty][tx] != 0 || field[ty][tx] == 'X' || field[ty][tx] == 'D')
			continue;
		water[ty][tx] = tt;
		q.push({ tx + 1, ty, tt + 1 });
		q.push({ tx, ty + 1, tt + 1 });
		q.push({ tx - 1, ty, tt + 1 });
		q.push({ tx, ty - 1, tt + 1 });
	}
}
void route_bfs() {
	while (!q.empty()) {
		int tx = q.front().x;
		int ty = q.front().y;
		int tt = q.front().t;
		q.pop();
		if (tx < 0 || tx >= C || ty < 0 || ty >= R)
			continue;
		if (vst[ty][tx] != 0 || field[ty][tx] == 'X' || (water[ty][tx] - 1 <= tt && water[ty][tx] != 0))
			continue;
		vst[ty][tx] = tt;
		q.push({ tx + 1, ty, tt + 1 });
		q.push({ tx, ty + 1, tt + 1 });
		q.push({ tx - 1, ty, tt + 1 });
		q.push({ tx, ty - 1, tt + 1 });
	}
}
int main() {
	scanf("%d %d", &R, &C);

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			char temp = getchar();
			if (temp == '\n') {
				j--;
				continue;
			}
			field[i][j] = temp;
		}
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (field[i][j] == '*') {
				q.push({ j, i, 1 });
			}
			if (field[i][j] == 'D') {
				Dp.x = j;
				Dp.y = i;
			}
			if (field[i][j] == 'S') {
				Sp.x = j;
				Sp.y = i;
			}
		}
	}
	water_bfs();
	q.push({ Sp.x, Sp.y, 0 });
	route_bfs();

	vst[Dp.y][Dp.x] == 0 ? cout << "KAKTUS" : cout << vst[Dp.y][Dp.x];

	return 0;
}
