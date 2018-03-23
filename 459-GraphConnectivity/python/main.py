import sys
#i need to add each line to list an mark which ones connect
testcases = sys.stdin.readline().rstrip('\n')
print(testcases)
for i in range(0,int(testcases)):
    letter = sys.stdin.readline().rstrip('\n')
    if not letter: 
        letter = sys.stdin.readline().rstrip('\n')
    #print(letter)
    letIndex = ord(letter) - 64
    print(letIndex)
    lst = []
    for x in range(0,letIndex):
        lst.append(x)
    #for case in sys.stdin.readlines():
    case = sys.stdin.readline()
    while case != 
        if not case.strip():
            break
        lineList = list(case.rstrip('\n'))
        print(lineList)
        for x in range(0,len(lineList)):
            lineList[x] = lst[ord(lineList[x])-65] #set vals in lineList equal to their lst counterparts         
        changeVal = lst[lineList[0]] 
        for let in range(0,len(lineList)): #iterates over the lineList
            if lineList[let] != changeVal: #if the value in lineList is not equal to the change value
                for x in range(0,len(lst)): #iterate lst 
                    if lst[x] == lineList[let]: 
                        lst[x] = changeVal
    print(len(set(lst)))