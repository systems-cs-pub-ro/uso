#include <stdlib.h>

#include "sum.h"
#include "add/add.h"

int vect_sum(int *v, int len)
{
    int i, s = 0;

    for (i = 0; i < len; i++)
        s = add(s, v[i]);

    return s;
}
