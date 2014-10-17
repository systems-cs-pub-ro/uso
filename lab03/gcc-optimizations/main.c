#include <stdlib.h>
#include <stdio.h>

#define MAX_ITER 100000000 /* 100 million */
#define N 4

int main(void)
{
    int i, j;
    long v[N] = {1, 2, 3, 4};
    long w[N] = {4, 3, 2, 1};

    for (i = 0; i < MAX_ITER; ++i)
        for (j = 0; j < N; ++j)
            v[j] += w[j];

    return 0;
}
