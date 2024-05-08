from process import Process
import simpy
class FCFS:
 
 def  __init__(self):  
    self.processList[Process]=[]
    self.tq=16

 
 def schedule(self,env,processes:Process):
   
   self.processList.append(processes)
   self.processList.sort(key=lambda x:x.at)

   current_time=env.now

   for p in self.processList:
     
     if current_time<p.at:
       current_time=p.at

     else:
       current_time+=p.bt
       p.tat=current_time=p.ar
       p.wt=p.tat-p.bt
     yield env.timeout(p.br)

   return self.processList
 
 
 def state(self):
    print("Pid\tBt\tAt\tTat\tWt\tCompleted")
    for p in self.processes:
            print(f"{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{p.wt}\t{p.complete}")
     

       
    

 