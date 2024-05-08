class Process:
    def __init__(self,pid,at,bt):
        self.pid=pid
        self.at=at
        self.bt=bt
        self.wt=0
        self.tat=0
        self.timeQuantum=0
        self.priority=0
        self.queue="None"
        self.add=False
        self.complete=False