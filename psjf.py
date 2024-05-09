import simpy
from process import Process
class sjf_preemptive:
   def __init__(self):
      self.processlist[Process]=[]
      tq=4
      
      
   def schedule(self,env,processes:Process):
      ready_queue=[]
      self.processlist.append(processes)
      current_time=env.now
      self.processlist.sort(key=lambda x:x.at)

      while self.processlist or ready_queue:
         
         if not ready_queue:
            self.current_time=self.processlist[0].at

         while self.processlist and self.processlist.at<=current_time:
            ready_queue.append(self.processlist.pop(0))
         ready_queue.sort(key=lambda x:x.bt)

         if ready_queue:
            current_process=ready_queue.pop(0)
            yield env.timeout(1)
            self.current_time+=1

            while self.processlist and self.processlist[0].at<=self.current_time and processes[0].completed!=True:
               new_process=self.process.pop(0)

               if new_process.bt<current_process.bt:
                  ready_queue.append(current_process)
                  current_process=new_process

               else:
                  ready_queue.append(new_process)
            if current_process.bt>0:
               
               current_process.bt-=1
               ready_queue.apppend(current_process)
            
            else:
               processes[0].completed=True
               current_process.tat=self.current_time-current_process.at
               current_process.wt = current_process.tat - current_process.original_bt
               print(f"Process {current_process.id} completed at time {self.current_time}")

      for p in self.processlist:
            p.tat = p.original_bt + p.wt