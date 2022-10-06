class Solution:
    def isValid(self, s: str) -> bool:
            pairs = {
                "(": ")",
                "{": "}",
                "[": "]"
            }

            l = []

            for ch in s:
                if ch in pairs:
                    l.append(ch)

                elif l:
                    if ch == pairs[l[-1]]:
                        l.pop()

                    else:
                        return False

                else:
                    return False

            return l == []
