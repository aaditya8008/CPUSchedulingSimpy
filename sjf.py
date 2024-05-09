import simpy
from process import Process
class sjf_nonpreemtive:
    def __init__(self):
      self.processlist[Process]=[]
      tq=12
    def schedule(self,env, processes: Process):
        ready_queue = []
        self.processlist.append(processes)
        current_time = env.now
        self.processlist.sort(key=lambda x: x.at)
        while self.processlist or ready_queue:
            if not ready_queue:
                current_time = self.processlist[0].at
            while self.processlist and self.processlist[0].at <= current_time and processes[0].completed!=True:
                ready_queue.append(self.processlist.pop(0))
            ready_queue.sort(key=lambda x: x.bt)

            if ready_queue:
                current_process = ready_queue.pop(0)
                yield env.timeout(current_process.bt)  
                current_time += current_process.bt
                processes[0].completed=True
                current_process.tat = current_time - current_process.at
                current_process.wt = current_process.tat - current_process.original_bt
                print(f"Process {current_process.id} completed at time {current_time}")

        for p in self.processlist:
            p.tat = p.original_bt + p.wt