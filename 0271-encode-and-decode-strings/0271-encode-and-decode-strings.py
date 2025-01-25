class Codec:
    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for s in strs:
            length = len(s)
            result += str(length) + "#" + s
        
        return result
        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i: j])
            word = s[j+1: j + 1 + length]
            output.append(word)

            i = j + 1 + length 
        
        return output

        

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))