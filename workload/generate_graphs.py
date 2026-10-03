import matplotlib.pyplot as plt

concurrency = [1, 2, 4, 8, 16]

response_time = [13.44, 19.64, 32.70, 59.85, 114.38]
throughput = [73.84, 100.89, 120.19, 128.17, 128.28]
cpu = [0.02, 0.01, 0.01, 0.01, 0.01]
memory = [24.03, 24.05, 24.08, 24.12, 24.29]


# Graph 1: Response Time
plt.figure()
plt.plot(concurrency, response_time, marker='o')
plt.xlabel("Concurrent Requests")
plt.ylabel("Average Response Time (ms)")
plt.title("Concurrent Requests vs Average Response Time")
plt.grid(True)
plt.savefig("response_time.png")
plt.close()


# Graph 2: Throughput
plt.figure()
plt.plot(concurrency, throughput, marker='o')
plt.xlabel("Concurrent Requests")
plt.ylabel("Throughput (requests/sec)")
plt.title("Concurrent Requests vs Throughput")
plt.grid(True)
plt.savefig("throughput.png")
plt.close()


# Graph 3: CPU
plt.figure()
plt.plot(concurrency, cpu, marker='o')
plt.xlabel("Concurrent Requests")
plt.ylabel("CPU Usage (%)")
plt.title("Concurrent Requests vs CPU Usage")
plt.grid(True)
plt.savefig("cpu_usage.png")
plt.close()


# Graph 4: Memory
plt.figure()
plt.plot(concurrency, memory, marker='o')
plt.xlabel("Concurrent Requests")
plt.ylabel("Memory Usage (MiB)")
plt.title("Concurrent Requests vs Memory Usage")
plt.grid(True)
plt.savefig("memory_usage.png")
plt.close()


print("All 4 graphs generated successfully.")
