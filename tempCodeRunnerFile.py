print("Results:")
    print("Pid\tBt\tAt\tTat\tWt")
    for p in processes:
        print(f"{p.pid}\t{p.bt}\t{p.at}\t{p.tat}\t{p.wt}")