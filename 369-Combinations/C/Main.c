#include <stdio.h>
int fac(int);
int main()
{
	int a,b,c;
	while (scanf("%d %d",&a,&b)!=EOF && (a!=0&&b!=0))
	{	
		c = fac(a)/(fac(a-b)*fac(b));
		printf("%d things taken %d at a time is %d exactly\n",a,b,c);	
	}
}
int fac(int num)
{
	if (num == 0 || num == 1)
		return 1;
	else
		return num*fac(num-1);
}
