import sys



def runProg():
    res = []
    line = sys.stdin.readline()
    while line:
        m,n = line.split()
        res.append(int(m)*int(n)-1)
        line = sys.stdin.readline()

    return res


def main():
    res = runProg()
    for i in res:
        print(i)


if __name__ == "__main__":
    main()
