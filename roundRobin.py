class RoundRobin:
    def __init__(self, tq=2):
        self.processList = []
        self.tq = tq

    def schedule(self, env):
        processes = self.processList
        current_time = env.now

        while processes:
            current_process = processes.pop(0)
            if current_process.bt > 0:
                if current_process.bt > self.tq:
                    yield env.timeout(self.tq)
                    current_time += self.tq
                    current_process.bt -= self.tq
                    processes.append(current_process)
                else:
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
