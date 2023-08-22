class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = ""
        while columnNumber != 0:
            columnNumber -= 1
            letters += chr(ord('A') + (columnNumber % 26))
            columnNumber = columnNumber // 26
        return letters[::-1]
