import simpy
import random
from process import Process
from fcfs import FCFS
from sjf import sjf_nonpreemtive
from roundRobin import RoundRobin
def generate_processes(num_processes):
    processes=[]
    

