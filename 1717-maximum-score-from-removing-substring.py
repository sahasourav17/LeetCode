class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_gain = 0
        sequence = [('ab', x), ('ba', y)]
        if x < y:
            sequence[0],sequence[1] = sequence[1],sequence[0]
        
        for (c1, c2), gain in sequence:
            stack = []
            for char in s:
                if stack and stack[-1] == c1 and char == c2:
                    stack.pop()
                    total_gain += gain
                else:
                    stack.append(char)
                
                s = stack
        return total_gain
