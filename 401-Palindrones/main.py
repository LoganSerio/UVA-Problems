import sys

for line in sys.stdin.readlines():
    #compare ith element and len-i element
    isPalindrome = True
    isMirrored = True
    length = len(line)
    for i in range(0,length//2): 
        if line[i] != line[length-i-1]:
            isPalindrome = False
        if not (line[i] == 'A' and line[length-i-1] == 'A') or (line[i] == 'E' and line[length-i-1] == '3') or (line[i] == 'H' and line[length-i-1] == 'H') or (line[i] == 'I' and line[length-i-1] == 'I') or (line[i] == 'J' and line[length-i-1] == 'L') or (line[i] == 'L' and line[length-i-1] == 'J') or (line[i] == 'M' and line[length-i-1] == 'M') or (line[i] == 'O' and line[length-i-1] == 'O') or (line[i] == 'S' and line[length-i-1] == '2') or (line[i] == 'T' and line[length-i-1] == 'T') or (line[i] == 'U' and line[length-i-1] == 'U') or (line[i] == 'V' and line[length-i-1] == 'V') or (line[i] == 'W' and line[length-i-1] == 'W') or (line[i] == 'X' and line[length-i-1] == 'X') or (line[i] == 'Y' and line[length-i-1] == 'Y') or (line[i] == 'Z' and line[length-i-1] == '5') or (line[i] == '1' and line[length-i-1] == '1') or (line[i] == '2' and line[length-i-1] == 'S') or (line[i] == '3' and line[length-i-1] == 'E') or (line[i] == '5' and line[length-i-1] == 'Z') or (line[i] == '8' and line[length-i-1] == '8'):
            isMirrored = False
    if isPalindrome:
        if isMirrored:
            print(line + "-- is a mirrored palindrome.")
        else:
            print(line + "-- is a palindrome.")
            
    else:
        if isMirrored:
            print(line + "-- is a mirrored string.")
        else:
            print(line + "-- is not a palindrome.")
            
            