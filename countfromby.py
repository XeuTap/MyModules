class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


g = CountFromBy(0, 1)
g.increase()
g.increase()
g.increase()
g.increase()
print(g)
b = CountFromBy()
b.increase()
b.increase()
b.increase()
b.increase()
print(b)
