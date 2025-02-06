class Codec:
    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += str(len(s)) + "#" + s
        
        return output
        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != "#":
                j += 1
            
            length = int(s[i: j])
            output.append(s[j + 1: j + 1 + length])
            i = j + 1 + length 
        
        return output

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))