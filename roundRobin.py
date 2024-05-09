from process import Process
import simpy

class RoundRobin:
    def __init__(self):  
        self.processList = []  
        self.tq = 8

    def schedule(self, env, processes: Process):
        self.processList.append(processes)
        current_time = env.now  
        
        while self.processList:
            for process in self.processList:
                if process.at <= current_time and not process.completed:
                    if process.bt > self.tq:
                        current_time += self.tq
                        process.bt -= self.tq
                    else:
                        current_time += process.bt
                        process.tat = current_time - process.at
                        process.wt = process.tat - process.bt
                        process.completed = True
                    yield env.timeout(process.bt)
        
        return self.processList

    def state(self):
        print("Pid\tBt\tAt\tTat\tWt\tCompleted")
        for p in self.processList:
            print(f"{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{p.wt}\t{p.completed}")
