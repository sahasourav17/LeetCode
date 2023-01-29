class Solution:
    def groupAnagrams(self, strs):
        finalGroup = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # print(finalGroup)
            if sorted_word in finalGroup:
                finalGroup[sorted_word].append(word)
            else:
                finalGroup[sorted_word] = [word]

        return [val for val in finalGroup.values()]