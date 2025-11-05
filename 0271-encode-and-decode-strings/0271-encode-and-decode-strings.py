class Codec:
    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        print(result)
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 # i for outer, j to form the strings

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))