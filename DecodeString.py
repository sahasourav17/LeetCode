class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for ch in s:

            # inserting element to the stack, if it is not equal to ']'
            if ch != ']':
                stack.append(ch)
            # if we found any ']' then
            else:
                innerStr =""
                """
                    we will pop element from the stack and add to the innerStr
                    until we found any '['

                """
                while stack[-1] != '[':
                    innerStr = stack.pop() + innerStr

                # This pop is required for removing '['
                stack.pop()

                """
                    finding the digit
                """
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                """
                    adding the result into the stack
                """
                stack.append(int(k)*innerStr)

        return "".join(stack)