class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        fhalf, shalf = 0, 0
        s.lower()
        for i, letter in enumerate(s):
            if letter in {'a', 'e', 'i', 'o', 'u'}:
                if i < len(s)//2:
                    fhalf += 1
                else:
                    shalf += 1

        return fhalf == shalf
