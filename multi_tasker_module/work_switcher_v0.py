import time
from subprocess import check_call 
import pynotify

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return


def work_switcher(key_word):
   string='Sir, I think you need to work on the Bengali ' + key_word + ' now'
   sendmessage(" Please switch now", string)
   check_call(['espeak' , string ])
   main()

def main():
 while True:   
   time.sleep(10)
   local_time=time.localtime(time.time())
   hours=local_time.tm_hour 
   minutes=local_time.tm_min  
   #print hours
   if hours==21:
    if minutes>15:
    
      list = ['website', 'evaluation', 'clusters']
      i=0
      while True:
       if i==len(list)-1:
          i=0
       key_word = list[i]
       
       work_switcher(key_word)
       i=i+1
   else:
      main()

if __name__ =='__main__':
    main()
