class Codec:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)

        while i < n:
            j = i 
            while j < n and s[j] != "#":
                j += 1
            length = int(s[i: j]) # j is at # char
            val = s[j + 1: j+ 1 + length]
            result.append(val)
            i = j + 1 + length
        
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))