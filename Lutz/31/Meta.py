import sys


class Meta:
    def __getattribute__(self, item):
        sys.stdout.write(item)

    def __setattr__(self, key, value):
        sys.stdout.write(str(value))

print(Meta())
a = Meta()
print(a)
a.att = 123
print(a.att)
