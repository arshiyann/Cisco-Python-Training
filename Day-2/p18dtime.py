import time
pin = 1234
count = 0

file = open('pin_history.log','a')
while(count <3):
  upin = input(f'Enter User Pin: ')
  count+=1
  if int(upin) ==pin:
    file.write(f'Succeed - Pin Matched - {count}')
    file.write(f'Pin Entry Time is {time.ctime()}\n')
    break
  else:
    file.write(f'Failed - Wrong User Input Pin:{upin}')
    file.write(f'Pin Entry Time is {time.ctime()}\n')
if count>=3:
   file.write(f'Blocked Your Card Input Limit Crossed')
   print("Sorry Your Card Is Blocked")
file.close()