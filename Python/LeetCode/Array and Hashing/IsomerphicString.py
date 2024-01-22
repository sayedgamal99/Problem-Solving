def isIsomorphic(s: str, t: str) -> bool:
        hs, ht = {},{}
        for one,two in zip(s,t):
            if ((one in hs)and(hs[one]!= two)):
                return False

            hs[one] = two
            if ((two in ht)and(ht[two]!= one)):
                return False
            ht[two] = one
        print(hs,ht)
        return True
