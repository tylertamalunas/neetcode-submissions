class Solution:

    def encode(self, strs: List[str]) -> str:
        # count length and add delimiter
        encrypted_str = ""
        for s in strs:
            encrypted_str += str(len(s)) + '#' + s
        return encrypted_str

    def decode(self, s: str) -> List[str]:
        # 2pointer 
        decrypted_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decrypted_str.append(s[i:j])
            i = j
        return decrypted_str