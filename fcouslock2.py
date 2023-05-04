import time

minutes = int(input("Enter the number of minutes to focus: "))
seconde = minutes * 60

while seconds:
  mins, secs = divmode(seconde, 60)
  timer = '{:02d}:{:02d}'.format(mins, secs)
  print(timer, end = "\r")
  time.sleep(1)
  seconds -= 1
  
print("Time's up!")
