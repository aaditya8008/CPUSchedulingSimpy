# PreemptiveSJF.py
import simpy

class PreemptiveSJF:
    def __init__(self, env, processes):
        self.env = env
        self.processes = processes
        self.current_time = 0

    def run(self):
        while self.processes:
            shortest_job = min(self.processes, key=lambda x: x.bt)
            if shortest_job.at <= self.current_time:
                remaining_time = shortest_job.bt
                self.processes.remove(shortest_job)
                while remaining_time > 0:
                    yield self.env.timeout(1)
                    self.current_time += 1
                    remaining_time -= 1
                    # Check if a shorter job arrived while executing the current one
                    if any(p.at <= self.current_time for p in self.processes):
                        break
                shortest_job.tat = self.current_time - shortest_job.at
                shortest_job.wt = shortest_job.tat - shortest_job.bt
            else:
                self.current_time = shortest_job.at

