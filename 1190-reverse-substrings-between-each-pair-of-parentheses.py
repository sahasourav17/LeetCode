# Time Complexity: O(n^2)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for curr_char in s:
            # print(f"result: {result}")
            if curr_char == "(":
                open_parentheses_indices.append(len(result))
                # print(f"open: {open_parentheses_indices}")
            elif curr_char == ")":
                start = open_parentheses_indices.pop()
                # print(f"close: {open_parentheses_indices}")
                result[start:] = result[start:][::-1]
            else:
                result.append(curr_char)
        return "".join(result)
