
import random


class RandomizedSet:

    def __init__(self):
        self.liss, self.mapp = [], {}

    def insert(self, val: int) -> bool:
        if val in self.mapp:
            return False
        else:
            self.liss.append(val)
            self.mapp[val] = len(self.liss)-1
            return True

    def remove(self, val: int) -> bool:
        if val in self.mapp:

            self.liss[self.mapp[val]] = self.liss[-1]
            self.mapp[self.liss[-1]] = self.mapp[val]
            self.liss.pop()
            del self.mapp[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.liss)
