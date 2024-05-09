import simpy
import random
from process import Process
from fcfs import FCFS
from sjf import sjf_nonpreemtive
from roundRobin import RoundRobin
pid =0
def generate_processes(num_processes):
    processes=[]

    for i in range(num_processes):
       at=random.randint(0,10)     #Random Arrival Time
       bt=random.randint(1,20)     #Random Burstt  Time
       processes.append(Process(pid=pid,at=at,bt=bt))

def main():
    num_processes=random.randint(1,10)
    psjfList=generate_processes(num_processes=num_processes)

    num_processes=random.randint(1,10)
    rrList=generate_processes(num_processes=num_processes)

    num_processes=random.randint(1,10)
    sjfList=generate_processes(num_processes=num_processes)

    num_processes=random.randint(1,10)
    fcfsList=generate_processes(num_processes=num_processes)

    env=simpy.Environment()
    fcfs=FCFS()
    roundRobin=RoundRobin()

    

    

