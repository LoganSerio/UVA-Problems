import sys

vowels = ['A','a','E','e','I','i','O','o','U','u']

for words in sys.stdin:
    t = ''
    l = len(words)
    i = 0
    while i < l:
        if words[i].isalpha():
            start = words[i]
            if start in vowels:
                t = t + start 
            i = i + 1
            while words[i].isalpha():
                t = t + words[i]
                i = i + 1
            if not start in vowels:
                t = t + start
            t = t + 'ay'
        else:
            t = t + words[i]
            i = i + 1
    print(t, end="")