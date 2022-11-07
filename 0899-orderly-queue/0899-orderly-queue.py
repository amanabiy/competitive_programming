class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        cba
        bac
        acb
        
        baaca
        aacab
        aaabc
        
        abcabcaa
        abcabaac
        abcaaabc
        abaacabc
        aaabcabc
        aaabcabc
        aaababcc
        aaaabbcc
        
        1000 * (klogk) * n
        
        dddddbb
        ddddbbd
        dddbbdd
        ddbbddd
        dbbdddd
        bbddddd
        
                
          
        kLetters -
        processed - [a, a, b, b, a, a, c, c]
        
        kLetters - bbb
        processed - [a, a, a, a, b, b, c, c]
        
        (nlogk) * k


        abbcabbcaa
        bbcabbcaaa
        bcabbcaaab
        bcbbcaaaba
        cbbcaaabab
        cbcaaababb
        ccaaababbb
        aaababbbcc


        cca -> in my choice so if i choose a it's not going to be possible so I only have to choose those I haven't processed yet
        
        
        collect the smaller ones from the beggining to the end and then do that until you can't anymore
        
        remainder = bc
        
        """
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))
        

        
        