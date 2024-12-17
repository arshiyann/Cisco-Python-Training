class box:
    bid = 101
    @classmethod
    def fx(cls):
        print(cls.bid)
        cls.bid = 202
        cls.bname = 'B1'

h = box.bid

print(h)