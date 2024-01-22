import string
import secrets


# alphabet = string.ascii_letters + string.digits
# random_string = ''.join(secrets.choice(alphabet) for i in range(6))
# print(alphabet)
# print(random_string)

class Codec:

    totiny, tolong = {}, {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in Codec.totiny:

            alphabet = string.ascii_letters + string.digits
            random_string = ''.join(secrets.choice(alphabet) for i in range(6))

            tostore = f'http://tinyurl.com/{random_string}'

            Codec.totiny[longUrl] = tostore
            Codec.tolong[tostore] = longUrl

            return Codec.totiny[longUrl]

        else:
            return Codec.totiny[longUrl]

    def decode(self, shortUrl: str) -> str:
        return Codec.tolong[shortUrl]


"""
https://leetcode.com/problems/design-tinyurl 

http://tinyurl.com/4e9iAk
"""


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# res2 = codec.encode('https://leetcode.com/problems/design-tinyurl')
# res3 = codec.decode(res2)
# print(res3)
