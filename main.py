import simpy
import random
from process import Process
from fcfs import FCFS
from sjf import SJFNonPreemptive
from roundRobin import RoundRobin
from psjf import SJFPreemptive

def generate_processes(num_processes):
    processes = []
    for i in range(num_processes):
       at = random.randint(0, 10)  # Random Arrival Time
       bt = random.randint(1, 11)   # Random Burst Time
       processes.append(Process(pid=i, at=at, bt=bt))
    return processes

def main():
    num_processes = random.randint(1, 100)
    processes = generate_processes(num_processes=num_processes)

    psjfList = []
    rrList = []
    sjfList = []
    fcfsList = []

    env = simpy.Environment()
    Psjf = SJFPreemptive()
    Fcfs = FCFS()
    roundRobin = RoundRobin()
    Sjf = SJFNonPreemptive()

    for process in processes:
        if process.bt <= 2:  # Real time processes
            psjfList.append(process)
        elif process.bt <= 5:  # Interactive processes
            rrList.append(process)
        elif process.bt <= 8:  # System processes
            sjfList.append(process)
        else:  # Batch processes
            fcfsList.append(process)

    psjfList = Psjf.schedule(env, psjfList)
    Psjf.state()

    rrList = roundRobin.schedule(env, rrList)
    roundRobin.state()

    sjfList = Sjf.schedule(env, sjfList)
    Sjf.state()

    fcfsList = Fcfs.schedule(env, fcfsList)
    Fcfs.state()

    print("Real time processes:\n")
    for p in psjfList:
        if p.completed:
           print(f"Process {p.pid}: Arrival Time = {p.at}, Burst Time = {p.bt}")

    print("Interactive processes:")
    for p in rrList:
        if p.completed:
           print(f"Process {p.pid}: Arrival Time = {p.at}, Burst Time = {p.bt}")

    print("System processes:")
    for p in sjfList:
        if p.completed:
           print(f"Process {p.pid}: Arrival Time = {p.at}, Burst Time = {p.bt}")

    print("Batch processes:")
    for p in fcfsList:
        if p.completed:
           print(f"Process {p.pid}: Arrival Time = {p.at}, Burst Time = {p.bt}")

    for p in processes:
        if not p.completed:
           print(f"Process {p.pid}: Arrival Time = {p.at}, Burst Time = {p.bt}")

if __name__ == "__main__":
    main()


    





