class Solution:

    def encode(self, strs: List[str]) -> str:
        # add add salt # and length of string to encoded message
        encoded_msg = ""
        for s in strs:
            encoded_msg += str(len(s)) + "#" + s
        return encoded_msg

    def decode(self, s: str) -> List[str]:
        # 2 points. one moves until it finds the salt #, then it reads the chars between the pointers and sets that as the lengrth of the word
        # then it sets the points to the same spot and same+length. 
        # the letters between is the word
        decoded_msg = []
        i = 0
        while i < len(s):
            k = i
            while s[k] != '#':
                k += 1
            length = int(s[i:k])
            print(length)
            i = k + 1
            k = i + length
            decoded_msg.append(s[i:k])
            i = k
        return decoded_msg
