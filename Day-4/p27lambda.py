def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()
print(type(x))
for z in x:
  print(z)