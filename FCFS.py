burst_times = list(map(int, input("Enter burst times: ").split()))
waiting_times = [0]

for i in range(1, len(burst_times)):
    waiting_times.append(waiting_times[i-1] + burst_times[i-1])

average_waiting = sum(waiting_times) / len(waiting_times)

print("Waiting times:", waiting_times)
print("Average waiting time:", average_waiting)