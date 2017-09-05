#include <stdio.h>
int main() {
	int testCases,inputCases;
	int caseNumber = 1;
	scanf("%d",&testCases);
	while (testCases--) {
		scanf("%d",&inputCases);
		int max = 0;
		int tmp;
		while (inputCases--) {
			scanf("%d",&tmp);
			if (max < tmp)
				max = tmp;	
		}
		printf("Case %d: %d\n",caseNumber++,max);
	}
	return 0;
}
