class Solution:
    def countTime(self, time: str) -> int:
        h1,h2,m1,m2 = 1,1,1,1
        if time[4] == '?':
            m2 = 10
        if time[3] == '?':
            m1 = 6
        if time[1] == '?':
            if time[0] == '2':
                h2 = 4
            elif time[0] == '?':
                h2 = 1
            else:
                h2 = 10
        if time[0] == '?':
            if time[1] <= '3':
                h1 = 3
            elif time[1] == '?':
                h1 = 24
            else:
                h1 = 2
        return h1*h2*m1*m2