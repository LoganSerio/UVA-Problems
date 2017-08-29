#include <stdio.h>
int main() 
{
	int cnt,ox,oy,x,y;
	while(scanf("%d",&cnt)==1&&cnt)
	{
		scanf("%d %d",&ox,&oy);
		while(cnt--)
		{
			scanf("%d %d",&x,&y);
			if (x == ox||y == oy)
				printf("divisa\n");
			else if (x > ox && y > oy)
				printf("NE\n");
			else if (x > ox && y < oy)
				printf("SE\n");
			else if (x < ox && y > oy)
				printf("NO\n");
			else
				printf("SO\n");
		}
	}
	return 0;
}
