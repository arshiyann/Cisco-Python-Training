import sys

print("one")
print("Two")
print("Three")

try:
    fobj = open('Invalifd_file','r')
except Exception:
    print((sys.exc_info()))
else:
    s = fobj.read()
    print(s)
    fobj.close()

for v in [1,2,3]:
    print(v)
print("End of The Line")