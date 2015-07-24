import time
from subprocess import check_call 
import pynotify

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return


def work_switcher(key_word):
   string='Sir, I think you need to work on  ' + key_word + ' now'
   sendmessage(" Please switch now", string)
   check_call(['espeak' , string ])
   main()

def main():
 while True:   
   time.sleep(10)
   local_time=time.localtime(time.time())
   hours=local_time.tm_hour 
   minutes=local_time.tm_min  

   i=0
   print hours
   print time_array[i]
   if int(hours)==int(time_array[i]):
      print 'Yes'
      event=event_array[i]
      work_switcher(event)
      i=i+1
   else:
      main()

if __name__ =='__main__':
    f=open('schedule.txt')
    time_array=[]
    event_array=[]
    for line in f:
       line=line.split('\n')[0]
       time_in_hours=line.split(':')[0]
       event=line.split(':')[1]
       time_array.append(time_in_hours)
       event_array.append(event)
    main()
