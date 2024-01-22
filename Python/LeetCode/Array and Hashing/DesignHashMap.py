class MyHashMap:

    def __init__(self):
        self.Map = [0]*1000000

    def put(self, key: int, value: int) -> None:
        self.Map[key]=value

    def get(self, key: int) -> int:
        return self.Map[key] if self.Map[key] else -1

    def remove(self, key: int) -> None:
        self.Map[key]=0




hash = MyHashMap()
hash.put(1, 1)
hash.put(2, 2)

print(hash.get(1))

print(hash.get(3))

hash.put(2, 1)

print(hash.get(2))

hash.remove(2)

print(hash.get(2))








# try frequency array to implement this.