# round_robin.py
import simpy

class RoundRobin:
    
    def __init__(self, env, processes, quantum):
        self.env = env
        self.processes = processes
        self.quantum = quantum
        self.current_time = 0

    def run(self):
        
        ready_queue = []

        while self.processes or ready_queue:
            
            while self.processes and self.processes[0].at <= self.current_time:
                ready_queue.append(self.processes.pop(0))

            if ready_queue:
                process = ready_queue.pop(0)

                if process.bt > self.quantum:
                    self.current_time += self.quantum
                    process.bt -= self.quantum
                    ready_queue.append(process)
                else:
                    self.current_time += process.bt
                    process.tat = self.current_time - process.at
                    process.wt = process.tat - process.bt
                    yield self.env.timeout(process.bt)
                    
            else:
                self.current_time += 1  # Idle CPU time


