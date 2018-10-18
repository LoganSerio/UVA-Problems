import sys

i = 1
for word in sys.stdin.readlines():
    lang = "UNKNOWN"
    word = word.strip('\n')
    if word == "#":
        break
    if word == "HELLO":
        lang = "ENGLISH"
    elif word == "HOLA":
        lang = "SPANISH"
    elif word == "HALLO":
        lang = "GERMAN"
    elif word == "BONJOUR":
        lang = "FRENCH"
    elif word == "CIAO":
        lang = "ITALIAN"
    elif word == "ZDRAVSTVUJTE":
        lang = "RUSSIAN"

    print("Case " + str(i) + ": " + lang)
    i+=1