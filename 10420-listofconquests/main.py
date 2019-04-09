import sys

lines = int(sys.stdin.readline())
countries = {}
for i in range(0,lines):
    line = sys.stdin.readline().strip()
    sentence = line.split()
    if sentence[0] in countries:
        countries[sentence[0]] += 1
    else:
        countries[sentence[0]] = 1
order = []
for country in countries:
    order.append(country)
order.sort()
for x in order:
    print(x + ' ' + str(countries.get(x)))
    
