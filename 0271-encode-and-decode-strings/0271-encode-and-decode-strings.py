class Codec:
    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result
        

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1: j+1+ length]

            output.append(word)
            i = j + 1 + length

        return output

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))