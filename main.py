# main.py
import random
import simpy
from process import Process
from fcfs import FCFS
from psjf import PreemptiveSJF
from sjf import NonPreemptiveSJF
from roundRobin import RoundRobin

def generate_processes(num_processes):
    processes = []
    for i in range(num_processes):
        at = random.randint(0, 10)  # Generate random arrival time between 0 and 10
        bt = random.randint(1, 20)  # Generate random burst time between 1 and 20
        processes.append(Process(i + 1, at, bt))
    return processes

def main():
    num_processes = random.randint(0,20) # Number of processes
    processes = generate_processes(num_processes)
    env = simpy.Environment()

    real_time_processes = [p for p in processes if p.bt <= 4]
    interactive_processes = [p for p in processes if 4 < p.bt <= 8]
    system_processes = [p for p in processes if 8 < p.bt <= 12]
    batch_processes = [p for p in processes if p.bt > 12]

    # First level queue: Preemptive SJF for real-time processes
    psjf_scheduler = PreemptiveSJF(env, real_time_processes.copy())
    

    # Second level queue: Round Robin for interactive processes
    round_robin_scheduler = RoundRobin(env, interactive_processes.copy(), quantum=2)
    

    # Third level queue: Non-preemptive SJF for system processes
    sjf_scheduler = NonPreemptiveSJF(env, system_processes.copy())
   

    # Fourth level queue: FCFS for batch processes
    fcfs_scheduler = FCFS(env, batch_processes.copy())
     
    print("\nIndividual  Process Non-Modified Results:")
    print("Level\tPid\tBt\tAt\tTat\tWt")

    for p in processes:
        level = ""
        if p in real_time_processes:
            level = "Real-Time"
        elif p in interactive_processes:
            level = "Interactive"
        elif p in system_processes:
            level = "System"
        elif p in batch_processes:
            level = "Batch"
        print(f"{level.ljust(12)}{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{max(0, p.wt)}")
     
    env.process(psjf_scheduler.run())
    env.process(round_robin_scheduler.run())
    env.process(sjf_scheduler.run())
    env.process(fcfs_scheduler.run())

    env.run()

    # Print results for all processes
    print("\nIndividual  Process Modified Results:")
    print("Level\tPid\tBt\tAt\tTat\tWt")
    for p in processes:
        level = ""
        if p in real_time_processes and real_time_processes:
            level = "Real-Time"
        elif p in interactive_processes and interactive_processes:
            level = "Interactive"
        elif p in system_processes and system_processes:
            level = "System"
        elif p in batch_processes and batch_processes:
            level = "Batch"
        print(f"{level.ljust(12)}{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{max(0, p.wt)}")  # Adjusted for negative waiting time

    # Calculate and print average waiting time, turnaround time, and completion time for each queue
    print("\nAverage Metrics per Queue:")
    print("Queue\tAvg. Waiting Time\tAvg. Turnaround Time\tAvg. Completion Time")
    
    queues = {
        "Real-Time": real_time_processes,
        "Interactive": interactive_processes,
        "System": system_processes,
        "Batch": batch_processes
    }
    
    for queue, processes_in_queue in queues.items():
     if(processes_in_queue):
        total_waiting_time = sum(max(0, p.wt) for p in processes_in_queue)  # Adjusted for negative waiting time
        total_turnaround_time = sum(p.tat for p in processes_in_queue)
        total_completion_time = sum(p.at + p.tat for p in processes_in_queue)
        avg_waiting_time = total_waiting_time / len(processes_in_queue)
        avg_turnaround_time = total_turnaround_time / len(processes_in_queue)
        avg_completion_time = total_completion_time / len(processes_in_queue)
        print(f"{queue.ljust(12)}{avg_waiting_time:.2f}\t\t\t{avg_turnaround_time:.2f}\t\t\t{avg_completion_time:.2f}")

if __name__ == "__main__":
    main()

    





