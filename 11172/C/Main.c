#include <stdio.h>
int main() 
{
	int count,i,first,second;
	while(scanf("%d", &count)==1) 
	{
		for(i=0;i<count;i++)
		{
			scanf("%d %d",&first, &second);
			if (first>second)
				printf(">\n");
			else if(first<second)
				printf("<\n");
			else
				printf("=\n");
		}
	}
	return 0;
}
