#include <iostream>
#include <queue>


using namespace std;
int N,M;
queue<pair<int, int>> q;
char field[100][100];
int c_field[100][100];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int main()
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%s",&field[i]);
	}
	
	q.push(make_pair(0,0));
	c_field[0][0] = 1;
	while(!q.empty()){
		int tx = q.front().first;
		int ty = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = tx + dx[i];
			int ny = ty + dy[i];
			if (nx < 0 || nx >= M || ny < 0 || ny >= N)
				continue;
			if (field[ny][nx] == '0' || c_field[ny][nx] != 0)
				continue;
			q.push(make_pair(nx, ny));
			c_field[ny][nx] = c_field[ty][tx] + 1;
		}
	}

	printf("%d", c_field[N-1][M-1]); 
}