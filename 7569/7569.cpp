#include <iostream>
#include <queue>

using namespace std;
int M, N, H;
int boxes[100][100][100];
int check[100][100][100];
int dx[6] = { 1,0,-1,0,0,0 };
int dy[6] = { 0,1,0,-1,0,0 };
int dz[6] = { 0,0,0,0,1,-1 };
struct pos {
   int x;
   int y;
   int z;
};

queue<pos> q;

int main() {
   scanf("%d %d %d", &M, &N, &H);
   for (int i = 0; i < H; i++) {
      for (int j = 0; j < N; j++) {
         for (int k = 0; k < M; k++) {
            scanf("%d", &boxes[i][j][k]);
            if (boxes[i][j][k] == 1) {
               q.push({ k, j, i});
               check[i][j][k] = 1;
            }
         }
      }
   }

   while (!q.empty()) {
      int tx = q.front().x;
      int ty = q.front().y;
      int tz = q.front().z;

      q.pop();
      for (int i = 0; i < 6; i++) {
         int nx = tx + dx[i];
         int ny = ty + dy[i];
         int nz = tz + dz[i];

         if (nx < 0 || ny < 0 || nz < 0)
            continue;
         if (nx >= M || ny >= N || nz >= H)
            continue;
         if (check[nz][ny][nx] != 0 || boxes[nz][ny][nx] == -1)
            continue;
         check[nz][ny][nx] = check[tz][ty][tx] + 1;
         q.push({ nx,ny,nz });
      }
   }
   int latest = 0;
   for (int i = 0; i < H; i++) {
      for (int j = 0; j < N; j++) {
         for (int k = 0; k < M; k++) {
            if (boxes[i][j][k] == 0 && check[i][j][k] == 0) {
               cout << -1;
               return 0;
            }
            if (latest < check[i][j][k])
               latest = check[i][j][k];
         }
      }
   }
   cout << latest - 1;

   return 0;
}