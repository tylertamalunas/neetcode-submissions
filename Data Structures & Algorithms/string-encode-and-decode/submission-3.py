class Solution:

    def encode(self, strs: List[str]) -> str:
        # [hello, hi]
        encoded_string = ""
        for s in strs:
            length = str(len(s))
            encoded_string += f"{length}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # "5#hello2#hi"
        decoded_string = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_string.append(s[i:j])
            i = j

        return decoded_string