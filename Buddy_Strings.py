class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or set(s) != set(goal): return False
        if s == goal:
            return len(s) - len(set(s)) >= 1
        else:
            idx = []
            diff = 0
            for i in range(len(s)):
                if s[i] != goal[i]:
                    diff += 1
                    idx.append(i)
                if diff > 2:
                    return False
            return s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]]





