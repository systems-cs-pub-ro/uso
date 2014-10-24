#include <stdlib.h>
#include <stdio.h>
#include <quadmath.h>

int main(void)
{
	__float128 r = 2.0q;
	char buf[128] = {0};

	quadmath_snprintf(buf, sizeof buf, "%Qe", sqrtq(r));
	printf("Square root of 2 is: %s\n", buf);

	return 0;
}
