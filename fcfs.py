# fcfs.py
import simpy

class FCFS:

    def __init__(self, env, processes):
        self.env = env
        self.processes = processes
        self.current_time = 0

    def run(self):

        self.processes.sort(key=lambda x: x.at)  # Sort processes by arrival time
        
        for p in self.processes:
            if self.current_time < p.at:
                # Handle idle CPU time
                self.current_time = p.at
            else:
                # Execute the process
                self.current_time += p.bt
                p.tat = self.current_time - p.at
                p.wt = p.tat - p.bt
            yield self.env.timeout(p.bt)

            


    

 