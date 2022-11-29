class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        # returns a string containing all lowercase letters
        alpha=string.ascii_lowercase

        subTable = {}
        idx = 0
        for i in key:
            if i not in subTable and i != " ":
                subTable[i] = alpha[idx]
                idx += 1
        # print(subTable)

        decodedMsg = ""
        for i in message:
            if i != " " and i in subTable:
                decodedMsg += subTable[i]
            else:
                decodedMsg += " "
        return decodedMsg