from process import Process

class SJF_NonPreemptive:
    def __init__(self):
        self.processList = []
        
    def schedule(self, env):
        processes = self.processList
        processes.sort(key=lambda x: x.at)  # Sort by arrival time
        
        current_time = env.now
        
        while processes:
            current_process = min(processes, key=lambda x: x.bt)
            processes.remove(current_process)
            yield env.timeout(current_process.bt)
            current_time += current_process.bt
            
            current_process.completed = True
            current_process.tat = current_time - current_process.at
            current_process.wt = current_process.tat - current_process.bt
            print(f"Process {current_process.pid} completed at time {current_time}")

    def state(self):
        print("Pid\tBt\tAt\tTat\tWt\tCompleted")
        for p in self.processList:
            print(f"{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{p.wt}\t{p.completed}")
