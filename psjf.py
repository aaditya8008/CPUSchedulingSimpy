from process import Process

class SJF_Preemptive:
    def __init__(self):
        self.processList = []

    def schedule(self, env):
        processes = self.processList
        processes.sort(key=lambda x: x.at)  # Sort by arrival time

        current_time = env.now
        ready_queue = []

        while processes or ready_queue:
            if not ready_queue:
                current_time = processes[0].at

            while processes and processes[0].at <= current_time:
                ready_queue.append(processes.pop(0))

            if ready_queue:
                current_process = min(ready_queue, key=lambda x: x.bt)
                ready_queue.remove(current_process)

                if current_process.bt > 0:
                    yield env.timeout(1)
                    current_time += 1
                    current_process.bt -= 1

                    if current_process.bt == 0:
                        current_process.completed = True
                        current_process.tat = current_time - current_process.at
                        current_process.wt = current_process.tat - current_process.bt
                        print(f"Process {current_process.pid} completed at time {current_time}")
                    else:
                        ready_queue.append(current_process)

        for p in self.processList:
            p.tat = p.bt + p.wt  # Update turnaround time using burst time and waiting time

    def state(self):
        print("Pid\tBt\tAt\tTat\tWt\tCompleted")
        for p in self.processList:
            print(f"{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{p.wt}\t{p.completed}")
