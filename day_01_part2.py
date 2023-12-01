from common import read_input

lines = read_input(1)

def l2n(s):
    r=""
    for i in range(len(s)):
        if s[i:i+1] in "0123456789": r+=s[i]
        elif s[i:i+4] == "zero": r+="0"
        elif s[i:i+3] == "one": r+="1"
        elif s[i:i+3] == "two": r+="2"
        elif s[i:i+5] == "three": r+="3"
        elif s[i:i+4] == "four": r+="4"
        elif s[i:i+4] == "five": r+="5"
        elif s[i:i+3] == "six": r+="6"
        elif s[i:i+5] == "seven": r+="7"
        elif s[i:i+5] == "eight": r+="8"
        elif s[i:i+4] == "nine": r+="9"
    if r: return int(r[0]+r[-1])
    return 0

s = 0
for l in lines: s+= l2n(l)
print(s)