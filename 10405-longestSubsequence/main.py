import sys
def getInput():
    lines = sys.stdin.readlines()
    for i in range(0,len(lines),2):
        first = lines[i].strip("\n")
        second = lines[i+1].strip("\n")
        print(GCS(first,second,len(first),len(second)))
        

def GCS(f,s,m,n):
    matrix = [[None] * (n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or  j== 0:
                matrix[i][j] = 0

            elif f[i-1] == s[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
                
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return matrix[i][j]

def main():
    getInput()

if __name__ == "__main__":
    main()
