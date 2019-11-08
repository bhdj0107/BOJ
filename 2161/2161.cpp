#include <iostream>
#include <queue>
using namespace std;
int N;
queue<int> q;

int main()
{
	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
		q.push(i);
		 
	while(!q.empty()) {
		int temp = q.front();
		printf("%d ", temp);
		q.pop();
		q.push(q.front());
		q.pop();
	}
}