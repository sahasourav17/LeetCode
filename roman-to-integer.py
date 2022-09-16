def RomanToInt(s):
    n = len(s)
    ans = 0
    d = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    for i in range(n-1):
        if d[s[i+1]] > d[s[i]]:
            ans -= d.get(s[i])
        else:
            ans += d.get(s[i])
    ans += d.get(s[n-1])
    return ans

s  = input()
print(RomanToInt(s))


