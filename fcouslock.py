import time
from playsocund import playsond

def focus_timer(minutes):
   seconds = minutes * 60
    while seconds > 0:
      print(f"Remaining time: {seconds // 60} minute(s) {seconds % 60} second(s)")
      time.sleep(1)
      seconds -= 1
    print("Time's up!")
    # playsound('alarm_sound.mp3') # 计时结束播放的音效，确保该文件放在工作目录中
    
if _name_ == '_main_':
  focus_timer(25) # 设置专注时间
