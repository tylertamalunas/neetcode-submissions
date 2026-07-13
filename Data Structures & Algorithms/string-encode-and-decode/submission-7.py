class Solution:

    def encode(self, strs: List[str]) -> str:
        # count length of string, then add the length and a delimiter to the front of string 
        encoded_str = ""
        for s in strs:
            length = str(len(s))
            encoded_str += f"{length}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # 2 pointers, right finds delimiter, chars between them becomes the int for how many chars to pull out.
        # move pointers, left after right, then right X after left pointer, chars between are the word
        decoded_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_str.append(s[i:j])
            i = j
        return decoded_str