#include <stdio.h>

#define MAX (100 + 20)

int T;
int N, L;
int MAP[MAX][MAX];
int TMAP[MAX][MAX];

void input()
{
	scanf("%d %d", &N, &L);

	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < N; c++)
		{
			scanf("%d", &MAP[r][c]);
			TMAP[c][r] = MAP[r][c];
		}
	}
}

int abs(int a, int b)
{
	return (a > b) ? a - b : b - a;
}

int isFlat(int* arr, int start, int end)
{
	int value = arr[start];
	for (int i = start + 1; i <= end; i++)
		if (value != arr[i]) return 0;

	return 1;
}

int check(int* arr)
{
	int inverse[MAX] = { 0 };
	int visit[MAX] = { 0 };
	int visit_inverse[MAX] = { 0 };

	for (int i = 0; i < N; i++) inverse[i] = arr[N - i - 1];

	for (int i = 0; i < N - 1; i++)
	{
		if (arr[i] == arr[i + 1]) continue; /* 1) 높이가 같으면 continue */
		if (abs(arr[i], arr[i + 1]) > 1) return 0; /* 2) 높이의 차가 2 이상이면 flase */
		if (arr[i] > arr[i + 1]) /* 3) i + 1이 작을 때, */
		{
			if (i + L == N) return 0; /* 경사로의 범위가 N을 넘으면 false */
			if (isFlat(arr, i + 1, i + L) == 0) return 0; /* i + 1 ~ i + L 까지 평평한지 체크 */

			for (int k = i + 1; k <= i + L; k++) visit[k] = 1; /* 경사로 설치 */
		}
	}

	/* inverse 경사로 설치를 위해 visit inverse */
	for (int i = 0; i < N; i++) visit_inverse[i] = visit[N - i - 1];

	for (int i = 0; i < N - 1; i++)
	{
		/* 1) ~ 3) */
		if (inverse[i] == inverse[i + 1]) continue;
		if (abs(inverse[i], inverse[i + 1]) > 1) return 0;
		if (inverse[i] > inverse[i + 1])
		{
			if (i + L == N) return 0;
			if (isFlat(inverse, i + 1, i + L) == 0) return 0;

			for (int k = i + 1; k <= i + L; k++) /* 이미 설치된 경사로면 false */
				if (visit_inverse[k]) return 0;
		}
	}

	return 1;
}

int main(void)
{
	// scanf("%d", &T);
	T = 1;
	for (int tc = 1; tc <= T; tc++)
	{
		int sum;

		input();

		sum = 0;
		for (int i = 0; i < N; i++)
		{
			sum += check(MAP[i]);
			sum += check(TMAP[i]);
		}

		printf("%d\n", sum);
	}

	return 0;
}