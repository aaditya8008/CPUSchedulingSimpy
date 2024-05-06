import simpy

def process(env, name, bt, at, wt, tat, out):
    yield env.timeout(at)
    start_time = env.now
    yield env.timeout(bt)
    end_time = env.now
    wt[name] = start_time
    tat[name] = end_time

def main():
    n = int(input("Enter number of processes: "))
    bt = [0] * n
    at = [0] * n
    wt = [0] * n
    tat = [0] * n

    for i in range(n):
        print("For p{}".format(i + 1))
        bt[i] = int(input("Burst time: "))
        at[i] = int(input("Arrival Time: "))

    env = simpy.Environment()
    for i in range(n):
        env.process(process(env, i, bt[i], at[i], wt, tat, None))

    env.run()

    sum_w = sum(wt)
    sum_t = sum(tat)

    print("Average waiting time:", sum_w / n)
    print("Average turn around time:", sum_t / n)

if __name__ == "__main__":
    main()
