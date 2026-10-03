import matplotlib.pyplot as plt

requests = [20, 50, 100, 150, 500]

# Data for concurrency 1, 2, 4, 8, 16

response_time = {
    1:  [12.05, 11.70, 11.44, 11.15, 12.90],
    2:  [19.57, 18.81, 17.52, 18.10, 20.88],
    4:  [31.25, 33.03, 29.96, 31.23, 33.02],
    8:  [56.43, 71.52, 54.88, 56.77, 60.66],
    16: [89.09, 108.95, 110.04, 117.31, 118.48]
}

throughput = {
    1:  [82.00, 84.61, 86.58, 88.71, 76.80],
    2:  [97.63, 104.68, 112.46, 109.07, 95.08],
    4:  [120.09, 116.40, 130.77, 126.63, 120.10],
    8:  [123.38, 82.59, 141.20, 137.70, 130.93],
    16: [117.06, 128.39, 134.94, 130.62, 132.93]
}

cpu = {
    1:  [0.01, 0.01, 0.01, 0.01, 0.01],
    2:  [0.01, 0.01, 0.01, 0.01, 0.01],
    4:  [0.01, 0.01, 0.02, 0.01, 0.01],
    8:  [0.01, 0.01, 0.02, 0.01, 0.01],
    16: [0.01, 0.02, 0.01, 0.01, 0.01]
}

memory = {
    1:  [19.24, 19.28, 22.76, 22.83, 22.98],
    2:  [19.24, 19.28, 22.78, 22.84, 23.02],
    4:  [19.24, 19.29, 22.80, 22.86, 23.08],
    8:  [19.25, 22.74, 22.81, 22.89, 23.14],
    16: [19.27, 22.75, 22.83, 22.94, 23.28]
}


def make_graph(data, ylabel, title, filename):
    plt.figure()

    for concurrency in data:
        plt.plot(
            requests,
            data[concurrency],
            marker='o',
            label=f'{concurrency} concurrent'
        )

    plt.xlabel("Total Requests")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


make_graph(
    response_time,
    "Average Response Time (ms)",
    "Total Requests vs Average Response Time",
    "comparison_response_time.png"
)

make_graph(
    throughput,
    "Throughput (requests/sec)",
    "Total Requests vs Throughput",
    "comparison_throughput.png"
)

make_graph(
    cpu,
    "CPU Usage (%)",
    "Total Requests vs CPU Usage",
    "comparison_cpu.png"
)

make_graph(
    memory,
    "Memory Usage (MiB)",
    "Total Requests vs Memory Usage",
    "comparison_memory.png"
)

print("All comparison graphs generated successfully.")
