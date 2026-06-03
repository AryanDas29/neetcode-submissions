class Solution:


    # input: ["Hello", "World"]
    # output: 5#hello5#world
    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = s + str(len(word))
            s = s + "#"
            s = s + word

        return s


    # input: 5#hello5#world
    # output:["Hello", "World"]
    def decode(self, s: str) -> List[str]:

        strs = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            word = s[j+1 : j + 1 + length]
            strs.append(word)
            i = j + 1 + length

        return strs
