from process import Process

class FCFS:
    def __init__(self):
        self.processList = []

    def schedule(self, env):
        processes = self.processList
        processes.sort(key=lambda x: x.at)  # Sort by arrival time

        current_time = env.now

        for p in processes:
            if current_time < p.at:
                current_time = p.at

            remaining_time = p.bt - (env.now - p.at)
            if remaining_time > 0:
                yield env.timeout(min(remaining_time, p.bt))
                current_time += min(remaining_time, p.bt)

            p.completed = True
            p.tat = current_time - p.at
            p.wt = p.tat - p.bt
            print(f"Process {p.pid} completed at time {current_time}")

    def state(self):
        print("Pid\tBt\tAt\tTat\tWt\tCompleted")
        for p in self.processList:
            print(f"{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{p.wt}\t{p.completed}")
      
    

 