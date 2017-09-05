#include <stdio.h>
int main() {
	int n,cnt;
	scanf("%d",&n);
	for (int i = 1; i <= n; i++) {
		scanf("%d",&cnt);
		int tmp;
		int max = 0;
		char line[1024];
		while (fgets(line,1024,stdin)) {
			while (sscanf(line,"%d",&tmp)!=EOF) {
				if (tmp > max)
					max = tmp;
			}
			printf("Case %d: %d\n",i,max);
		}
	}
	return 0;
}
