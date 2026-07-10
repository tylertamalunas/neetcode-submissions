class Solution:

    def encode(self, strs: List[str]) -> str:
        # use number and delimiter prefixed to each string
        encoded_str = ""
        for s in strs:
            length = str(len(s))
            encoded_str += f"{length}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # 2 pointers, right pointer moves until it finds delimiter, then sets length to decode as number between pointers
        # move pointers to right+1 and new left+length
        # decoded string is chars between the pointers
        # repeat until end
        
        decoded_str = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            decoded_str.append(s[i:j])
            i = j
        return decoded_str