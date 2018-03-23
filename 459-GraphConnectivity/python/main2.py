import sys
testcases = sys.stdin.readline().rstrip('\n')

inpt = sys.stdin.readlines()
inpt = [i.split('\n',1)[0] for i in inpt]
#inpt = list(filter(None,inpt))
inpt.pop(0)
splits = []
tmplst = []
count = 0
for x in range(0,len(inpt)):
    if inpt[x] == '':
        splits.append(tmplst)
        tmplst = []
        #count += 1
    else:
        tmplst.append(inpt[x])
        if x == len(inpt) - 1:
            splits.append(tmplst)
for i in splits:
    letter = i[0]
    letIndex = ord(letter) - 64
    lst = []
    for x in range(0,letIndex):
        lst.append(x)
    for case in i[1:]:
        lineList = list(case)
        #print(lineList)
        for x in range(0,len(lineList)):
            lineList[x] = lst[ord(lineList[x])-65]
            changeVal = lst[lineList[0]] 
            for let in range(0,len(lineList)): #iterates over the lineList
                if lineList[let] != changeVal: #if the value in lineList is not equal to the change value
                    for x in range(0,len(lst)): #iterate lst 
                        if lst[x] == lineList[let]: 
                            lst[x] = changeVal        
    print(len(set(lst)))
    if not (splits.index(i) == len(splits)-1):
        print()
