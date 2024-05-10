# nonpreemptive_sjf.py
import simpy

class NonPreemptiveSJF:
    def __init__(self, env, processes):
        self.env = env
        self.processes = processes
        self.current_time = 0

    def run(self):
        self.processes.sort(key=lambda x: x.at)
        while self.processes:
            available_processes = [p for p in self.processes if p.at <= self.current_time]
            if available_processes:
                shortest_job = min(available_processes, key=lambda x: x.bt)
                self.current_time += shortest_job.bt
                shortest_job.tat = self.current_time - shortest_job.at
                shortest_job.wt = shortest_job.tat - shortest_job.bt
                self.processes.remove(shortest_job)
                yield self.env.timeout(shortest_job.bt)
            else:
                self.current_time = min(p.at for p in self.processes)

