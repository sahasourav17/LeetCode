class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = {i: {"inward": 0, "outward": 0} for i in range(1, n + 1)}
    
        for a, b in trust:
            trust_counts[a]["outward"] += 1
            trust_counts[b]["inward"] += 1

        # print(trust_counts)
        for person in range(1, n + 1):
            if trust_counts[person]["outward"] == 0 and trust_counts[person]["inward"] == n - 1:
                return person
        return -1

# Time Complexity: O(N)
