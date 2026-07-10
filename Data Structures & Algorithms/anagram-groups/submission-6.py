class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort word, if that key exists add to dictionary value list otherwise create new key:val pair
        answer = {}

        for word in strs:
            new_word = "".join(sorted(word))
            if new_word in answer:
                answer[new_word].append(word)
            else:
                answer[new_word] = [word]
        result = []
        for value in answer.values():
            result.append(value)
        return result
            