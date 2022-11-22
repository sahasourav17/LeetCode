class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        l = sentence.strip().split()
        # print(l)
        
        for word in l:
            check = True
            ans = any(char.isdigit() for char in word)
            
            if ans:
                continue
            elif word.startswith('-') or word.endswith('-'):
                continue
            elif word.count('-') > 1 or word.count('.') > 1 or word.count('!') > 1:
                continue
            
            for i in range(len(word)-1):
                if word[i] in ".,!":
                    check = False
                elif word[i] == '-':
                    if not word[i-1].isalpha() or not word[i+1].isalpha():
                        check = False
                if not check:
                    break
            if check:
                count += 1
        return count