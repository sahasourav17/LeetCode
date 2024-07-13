# Time Complexity: O(n.log(n))
# Space Complexity: O(n)

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        stack = deque()

        # sorting indices based on their positions
        indices.sort(key=lambda x: positions[x])

        for curr_idx in indices:
            if directions[curr_idx] == "R":
                stack.append(curr_idx)
            else:
                while stack and healths[curr_idx] > 0:
                    top_idx = stack.pop()
                    # CASE-1: top robot survives, current robot is destroyed
                    if healths[top_idx] > healths[curr_idx]:
                        healths[top_idx] -= 1
                        healths[curr_idx] = 0
                        stack.append(top_idx)
                    # CASE-2: current robot survives, top robot is destroyed
                    elif healths[top_idx] < healths[curr_idx]:
                        healths[curr_idx] -= 1
                        healths[top_idx] = 0
                    # CASE-3: both robots are destroyed as their health same
                    else:
                        healths[top_idx] = 0
                        healths[curr_idx] = 0

        return [healths[idx] for idx in range(n) if healths[idx] > 0]
