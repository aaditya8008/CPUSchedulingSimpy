class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at  # Arrival Time
        self.bt = bt  # Burst Time
        self.wt = 0   # Waiting Time
        self.tat = 0  # Turnaround Time
        self.completed = False
