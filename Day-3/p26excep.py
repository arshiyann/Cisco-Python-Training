import sys

try:
    n = input('Enter n Value: ')
    if n<100:
        raise ValueError("Value Is Greater Than 100!")
except Exception:
    print(sys.exc_info())
else:
    print(f'Given n Value is: {n} - {int(n) + 100}')
for v in [1,2,3,4]:
    print("test messege: "+str(v))
print('End of the line')