import sys
n = sys.stdin.readline()
dict = {}
for i in sys.stdin.read():
    i = str(i).upper()
    if i in dict:
        dict[i] += 1
    else:
        if ord(i) >= 65 and ord(i) <= 90:
            dict[i] = 1
    
dict2 = {}
for key in sorted(dict.items(), key=lambda x: x[0]):
    dict2[key[0]] = key[1]
    
for key in sorted(dict.items(), key=lambda x: x[1],reverse=True):
    print(key[0] + ": " + str(key[1]))