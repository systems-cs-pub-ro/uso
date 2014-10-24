#include <stdlib.h>
#include <stdio.h>

#include "utils/utils.h"
#include "sum/sum.h"

#define N 10

int main(void)
{
    int v[N] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum;

    pretty_print_vect(v, N);
    sum = vect_sum(v, N);

    printf("\nSum is: ");
    pretty_print_int(sum);
    puts("");

    return 0;
}
