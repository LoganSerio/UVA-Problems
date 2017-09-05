#include <stdio.h>
int main() {
	int a,b,c;
	while(scanf("%d %d",&a,&b)!=EOF) {
		if (a<0&&b<0)
			break;
		else {
			c = 0;
			if (a<b) {
				c=b-a;
				if (c > 50)
					c = (a+1)+(99-b);
				printf("%d\n",c);	
			}
			else {
				c = a-b;
				if (c > 50)
					c = (99-a)+(b+1);
				printf("%d\n",c);
			}		
		}
	}
	return 0;
}
