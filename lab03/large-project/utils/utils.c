#include <stdlib.h>
#include <stdio.h>

void pretty_print_int(int n)
{
    printf("integer: %d", n);
}

void pretty_print_vect(int *v, int len)
{
    int i;

    printf("{vector:\n\t{\n");

    for (i = 0; i < len; i++) {
        printf("\t\t");
        pretty_print_int(v[i]);
        printf(",\n");
    }

    printf("\t}\n}");
}
